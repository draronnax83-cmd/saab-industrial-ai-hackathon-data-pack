#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / "data" / "resilience"
COP = ROOT / "data" / "copilot"

errors: list[str] = []
warnings: list[str] = []


def load_json(path: Path) -> dict:
    try:
        with path.open(encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        errors.append(f"Missing file: {path.relative_to(ROOT)}")
        return {}
    except json.JSONDecodeError as exc:
        errors.append(
            f"Invalid JSON: {path.relative_to(ROOT)} "
            f"(line {exc.lineno}, column {exc.colno}): {exc.msg}"
        )
        return {}


def ids(records: list[dict], key: str) -> set[str]:
    result = set()
    for index, record in enumerate(records):
        value = record.get(key)
        if not value:
            errors.append(f"Missing {key} in record #{index + 1}")
        elif value in result:
            errors.append(f"Duplicate {key}: {value}")
        else:
            result.add(value)
    return result


def check_ref(source: str, value: str | None, valid: set[str], target: str):
    if value is not None and value not in valid:
        errors.append(f"{source}: unresolved reference '{value}' → {target}")


def check_refs(source: str, values: list[str] | None, valid: set[str], target: str):
    for value in values or []:
        check_ref(source, value, valid, target)


def check_record_count(manifest: dict, path: str, actual: int):
    for pack in manifest.get("challenge_packs", []):
        for file_info in pack.get("files", []):
            if file_info.get("path") == path and "record_count" in file_info:
                expected = file_info["record_count"]
                if expected != actual:
                    errors.append(
                        f"{path}: manifest count {expected}, actual count {actual}"
                    )


# ---------- Load manifest ----------
manifest = load_json(ROOT / "manifest.json")

# ---------- Resilience ----------
assets_doc = load_json(RES / "assets.json")
deps_doc = load_json(RES / "dependencies.json")
events_doc = load_json(RES / "health-events.json")
spares_doc = load_json(RES / "spares.json")
caps_doc = load_json(RES / "capabilities.json")
geo_doc = load_json(RES / "locations.geojson")
res_scen_doc = load_json(RES / "scenarios.json")

assets = assets_doc.get("assets", [])
deps = deps_doc.get("dependencies", [])
events = events_doc.get("events", [])
spares = spares_doc.get("spares", [])
caps = caps_doc.get("capabilities", [])
features = geo_doc.get("features", [])
res_scenarios = res_scen_doc.get("scenarios", [])

asset_ids = ids(assets, "asset_id")
dep_ids = ids(deps, "dependency_id")
event_ids = ids(events, "event_id")
spare_ids = ids(spares, "spare_id")
cap_ids = ids(caps, "capability_id")
res_scenario_ids = ids(res_scenarios, "scenario_id")

for dep in deps:
    ref = dep.get("dependency_id", "<unknown dependency>")
    check_ref(ref, dep.get("source_asset_id"), asset_ids, "assets.asset_id")
    check_ref(ref, dep.get("target_asset_id"), asset_ids, "assets.asset_id")
    check_refs(ref, dep.get("alternate_asset_ids"), asset_ids, "assets.asset_id")

for event in events:
    ref = event.get("event_id", "<unknown event>")
    check_ref(ref, event.get("asset_id"), asset_ids, "assets.asset_id")
    check_refs(ref, event.get("affected_dependency_ids"), dep_ids, "dependencies.dependency_id")

for spare in spares:
    ref = spare.get("spare_id", "<unknown spare>")
    check_ref(ref, spare.get("stocking_asset_id"), asset_ids, "assets.asset_id")
    check_refs(ref, spare.get("primary_supported_asset_ids"), asset_ids, "assets.asset_id")
    check_refs(ref, spare.get("associated_dependency_ids"), dep_ids, "dependencies.dependency_id")
    check_refs(ref, spare.get("substitute_spare_ids"), spare_ids, "spares.spare_id")

for cap in caps:
    ref = cap.get("capability_id", "<unknown capability>")
    for contribution in cap.get("contributions", []):
        check_ref(ref, contribution.get("asset_id"), asset_ids, "assets.asset_id")
        check_refs(ref, contribution.get("dependency_ids"), dep_ids, "dependencies.dependency_id")

for feature in features:
    source = f"locations feature {feature.get('id', '<unknown>')}"
    asset_id = feature.get("properties", {}).get("asset_id")
    check_ref(source, asset_id, asset_ids, "assets.asset_id")
    if feature.get("id") != asset_id:
        errors.append(f"{source}: feature id does not match properties.asset_id")

for scenario in res_scenarios:
    ref = scenario.get("scenario_id", "<unknown resilience scenario>")
    check_refs(ref, scenario.get("primary_affected_assets"), asset_ids, "assets.asset_id")
    check_refs(ref, scenario.get("primary_affected_dependencies"), dep_ids, "dependencies.dependency_id")

    for event_id in scenario.get("initial_conditions", {}).get("assume_existing_health_events", []):
        check_ref(ref, event_id, event_ids, "health-events.event_id")

    for asset_id in scenario.get("initial_conditions", {}).get("available_alternates", []):
        check_ref(ref, asset_id, asset_ids, "assets.asset_id")

    for inject in scenario.get("injects", []):
        if "target_asset_id" in inject:
            check_ref(ref, inject["target_asset_id"], asset_ids, "assets.asset_id")
        if "target_spare_id" in inject:
            check_ref(ref, inject["target_spare_id"], spare_ids, "spares.spare_id")

    for action in scenario.get("possible_actions", []):
        check_refs(
            f"{ref} action {action.get('action_id', '<unknown>')}",
            action.get("target_asset_ids"),
            asset_ids,
            "assets.asset_id",
        )
        check_refs(
            f"{ref} action {action.get('action_id', '<unknown>')}",
            action.get("related_spare_ids"),
            spare_ids,
            "spares.spare_id",
        )

    for impact in scenario.get("expected_impacts", {}).get("capability_trend", []):
        check_ref(ref, impact.get("capability_id"), cap_ids, "capabilities.capability_id")

# ---------- Co-pilot ----------
systems_doc = load_json(COP / "systems.json")
tasks_doc = load_json(COP / "tasks.json")
info_doc = load_json(COP / "information-objects.json")
rules_doc = load_json(COP / "configuration-rules.json")
issues_doc = load_json(COP / "issue-history.json")
templates_doc = load_json(COP / "report-templates.json")
cop_scen_doc = load_json(COP / "scenarios.json")

platforms = systems_doc.get("platforms", [])
compartments = systems_doc.get("compartments", [])
systems = systems_doc.get("systems", [])
tasks = tasks_doc.get("tasks", [])
info_objects = info_doc.get("information_objects", [])
rules = rules_doc.get("rules", [])
issues = issues_doc.get("issues", [])
templates = templates_doc.get("templates", [])
cop_scenarios = cop_scen_doc.get("scenarios", [])

platform_ids = ids(platforms, "platform_id")
compartment_ids = ids(compartments, "compartment_id")
system_ids = ids(systems, "system_id")
task_ids = ids(tasks, "task_id")
info_ids = ids(info_objects, "information_object_id")
rule_ids = ids(rules, "rule_id")
issue_ids = ids(issues, "issue_id")
template_ids = ids(templates, "template_id")
cop_scenario_ids = ids(cop_scenarios, "scenario_id")

for compartment in compartments:
    check_ref(
        compartment.get("compartment_id", "<unknown compartment>"),
        compartment.get("platform_id"),
        platform_ids,
        "platforms.platform_id",
    )

for system in systems:
    ref = system.get("system_id", "<unknown system>")
    check_ref(ref, system.get("platform_id"), platform_ids, "platforms.platform_id")
    check_ref(ref, system.get("compartment_id"), compartment_ids, "compartments.compartment_id")

for task in tasks:
    ref = task.get("task_id", "<unknown task>")
    check_ref(ref, task.get("platform_id"), platform_ids, "platforms.platform_id")
    check_ref(ref, task.get("compartment_id"), compartment_ids, "compartments.compartment_id")
    check_ref(ref, task.get("system_id"), system_ids, "systems.system_id")
    check_refs(ref, task.get("required_document_ids"), info_ids, "information_objects.information_object_id")
    check_refs(ref, task.get("post_task_requirements"), task_ids, "tasks.task_id")
    check_ref(ref, task.get("report_template_id"), template_ids, "report_templates.template_id")

for info in info_objects:
    ref = info.get("information_object_id", "<unknown information object>")
    check_refs(ref, info.get("related_drawing_ids"), info_ids, "information_objects.information_object_id")
    check_refs(ref, info.get("safety_note_ids"), info_ids, "information_objects.information_object_id")

for rule in rules:
    ref = rule.get("rule_id", "<unknown configuration rule>")
    conditions = rule.get("conditions", {})
    for key in (
        "required_information_object_ids",
        "disallowed_information_object_ids",
    ):
        check_refs(ref, conditions.get(key), info_ids, "information_objects.information_object_id")

    for key in (
        "trigger_tasks",
        "required_task_sequence",
        "then_require",
    ):
        check_refs(ref, conditions.get(key), task_ids, "tasks.task_id")

    for key in (
        "hardware_installation_task_id",
        "software_update_task_id",
        "acceptance_test_task_id",
        "inspection_task_id",
        "rework_task_id",
        "functional_test_task_id",
    ):
        if key in conditions:
            check_ref(ref, conditions.get(key), task_ids, "tasks.task_id")

    check_refs(ref, rule.get("evidence_to_display"), set(
        list(system_ids) + list(task_ids) + list(info_ids) + list(rule_ids)
    ), "system/task/information/rule ID")

for issue in issues:
    ref = issue.get("issue_id", "<unknown issue>")
    check_ref(ref, issue.get("platform_id"), platform_ids, "platforms.platform_id")
    check_ref(ref, issue.get("compartment_id"), compartment_ids, "compartments.compartment_id")
    check_ref(ref, issue.get("system_id"), system_ids, "systems.system_id")
    check_ref(ref, issue.get("related_task_id"), task_ids, "tasks.task_id")
    check_ref(ref, issue.get("related_rule_id"), rule_ids, "configuration_rules.rule_id")
    check_refs(ref, issue.get("related_information_object_ids"), info_ids, "information_objects.information_object_id")

for template in templates:
    ref = template.get("template_id", "<unknown template>")
    for item in template.get("checklist_items", []):
        if "related_rule_id" in item:
            check_ref(ref, item["related_rule_id"], rule_ids, "configuration_rules.rule_id")
        check_refs(ref, item.get("related_rule_ids"), rule_ids, "configuration_rules.rule_id")
        if "related_information_object_id" in item:
            check_ref(
                ref,
                item["related_information_object_id"],
                info_ids,
                "information_objects.information_object_id",
            )

for scenario in cop_scenarios:
    ref = scenario.get("scenario_id", "<unknown co-pilot scenario>")
    context = scenario.get("entry_context", {})
    check_ref(ref, context.get("platform_id"), platform_ids, "platforms.platform_id")
    check_ref(ref, context.get("compartment_id"), compartment_ids, "compartments.compartment_id")
    check_ref(ref, context.get("system_id"), system_ids, "systems.system_id")
    check_ref(ref, context.get("task_id"), task_ids, "tasks.task_id")

    for inject in scenario.get("injects", []):
        if "information_object_id" in inject:
            check_ref(ref, inject["information_object_id"], info_ids, "information_objects.information_object_id")
        if "task_id" in inject:
            check_ref(ref, inject["task_id"], task_ids, "tasks.task_id")

    all_copilot_ids = (
        platform_ids
        | compartment_ids
        | system_ids
        | task_ids
        | info_ids
        | rule_ids
        | issue_ids
        | template_ids
    )
    check_refs(
        ref,
        scenario.get("required_evidence_record_ids"),
        all_copilot_ids,
        "co-pilot canonical record ID",
    )

# ---------- Manifest record counts ----------
check_record_count(manifest, "data/resilience/assets.json", len(assets))
check_record_count(manifest, "data/resilience/dependencies.json", len(deps))
check_record_count(manifest, "data/resilience/health-events.json", len(events))
check_record_count(manifest, "data/resilience/spares.json", len(spares))
check_record_count(manifest, "data/resilience/capabilities.json", len(caps))
check_record_count(manifest, "data/resilience/locations.geojson", len(features))
check_record_count(manifest, "data/resilience/scenarios.json", len(res_scenarios))
check_record_count(manifest, "data/copilot/tasks.json", len(tasks))
check_record_count(manifest, "data/copilot/information-objects.json", len(info_objects))
check_record_count(manifest, "data/copilot/configuration-rules.json", len(rules))
check_record_count(manifest, "data/copilot/issue-history.json", len(issues))
check_record_count(manifest, "data/copilot/report-templates.json", len(templates))
check_record_count(manifest, "data/copilot/scenarios.json", len(cop_scenarios))

# ---------- Result ----------
print("Cross-file validation complete.")
print(f"Errors: {len(errors)}")
print(f"Warnings: {len(warnings)}")

if warnings:
    print("\\nWARNINGS")
    for message in warnings:
        print(f"- {message}")

if errors:
    print("\\nERRORS")
    for message in errors:
        print(f"- {message}")
    sys.exit(1)

print("\\nPASS: All checked JSON/GeoJSON files parsed and all checked references resolved.")