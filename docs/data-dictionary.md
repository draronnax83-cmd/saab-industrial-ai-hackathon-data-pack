# Data Dictionary

This document describes the synthetic data model for the Saab Industrial AI Hackathon challenge kit. It covers field conventions, allowed values, entity relationships, and the boundary between the **Operational Co-pilot** and **Fleet & Coastal-Infrastructure Resilience** packs.

All records are fictional, non-classified and non-operational. The data is designed for prototypes, demonstrations, explainable reasoning, and user-experience experimentation only.

## Shared conventions

### Identifier conventions

All identifiers are stable, human-readable strings. Preserve them when extending or importing the data.

| Prefix | Entity | Example |
|---|---|---|
| `PLT-` | Co-pilot platform | `PLT-001` |
| `CPT-` | Co-pilot compartment | `CPT-002` |
| `SYS-` | Co-pilot installed system | `SYS-002` |
| `TASK-` | Co-pilot work task | `TASK-001` |
| `INFO-` | Co-pilot information object | `INFO-APR-INST-REV-D` |
| `CFG-RULE-` | Co-pilot configuration rule | `CFG-RULE-001` |
| `ISS-` | Co-pilot historical issue | `ISS-001` |
| `RPT-TPL-` | Co-pilot report template | `RPT-TPL-CONFIG-CLOSE` |
| `COP-SCN-` | Co-pilot scenario | `COP-SCN-001` |
| `AST-` | Resilience asset | `AST-BASE-001` |
| `DEP-` | Resilience dependency | `DEP-021` |
| `HE-` | Resilience health event | `HE-004` |
| `SPR-` | Resilience spare/support item | `SPR-004` |
| `CAP-` | Resilience capability | `CAP-003` |
| `SCN-` | Resilience scenario | `SCN-001` |

Do not reuse an ID for a different record. New records should use the same prefix and the next unused number, except where an identifier deliberately includes a meaningful revision suffix.

### Common metadata

Each JSON file begins with a `dataset` object.

| Field | Meaning |
|---|---|
| `name` | Human-readable dataset title |
| `version` | Dataset version, currently `0.1.0` |
| `classification` | Synthetic, non-classified, non-export-controlled handling statement |
| `fictionalisation_notice` | Explicit reminder that names, values, relationships and outcomes are invented |
| `generated_for` | Intended challenge track or hackathon use |
| `source_files` | Optional list of related files used by the dataset |

### General status and evidence principles

- Treat all numerical values as **synthetic demonstration values**, not engineering limits or operational metrics.
- Preserve `source`/evidence IDs in UI output. A recommendation without a visible record, rule, document, scenario or event reference should be shown as uncertain.
- When essential context is missing, use an **insufficient data / human review required** state rather than inventing an answer.
- Teams may add derived fields and records, but should not overwrite the canonical input data without preserving provenance.

## Resilience pack

Path: `data/resilience/`

The resilience pack models a fictional system of systems: maritime platforms, fixed sensors, bases, depots, maintenance facilities, communications nodes, logistics nodes, typed dependencies, health events, spares, abstract capabilities and disruption scenarios.

### assets.json

Top-level array: `assets`

| Field | Type | Definition | Typical values |
|---|---|---|---|
| `asset_id` | string | Unique asset identifier | `AST-PLT-001` |
| `name` | string | Fictional display name | `NMS Skarven` |
| `asset_type` | string | Asset category | See allowed values below |
| `domain` | string | Functional domain | `maritime`, `surveillance`, `support`, `logistics`, `communications` |
| `status` | string | Current synthetic availability state | See allowed values below |
| `health_score` | number | Synthetic technical-health indicator, 0.00–1.00 | `0.86` |
| `readiness_score` | number | Synthetic readiness indicator, 0.00–1.00 | `0.80` |
| `criticality` | string | Relative importance in the fictional network | `medium`, `high`, `critical` |
| `support_location_id` | string/null | Primary support asset ID, if applicable | `AST-BASE-001` |
| `primary_role` | string | Plain-language role in the fictional system | `coastal_surveillance` |
| `location` | object | Diagrammatic latitude, longitude and label | `{ "latitude": 58.0, ... }` |
| `notes` | string | Synthetic context note | Free text |

Allowed `asset_type` values:

```text
subsurface_platform
surface_patrol_platform
maritime_support_platform
coastal_sensor
underwater_sensor
naval_base
spares_depot
maintenance_facility
communications_relay
communications_gateway
logistics_node
```

Allowed `status` values:

```text
available
limited_availability
degraded
unavailable
in_maintenance
```

### dependencies.json

Top-level array: `dependencies`

Each dependency means that the `source_asset_id` relies on, exchanges with, or is constrained by the `target_asset_id` under the stated dependency type.

| Field | Type | Definition |
|---|---|---|
| `dependency_id` | string | Unique dependency identifier |
| `source_asset_id` | string | Asset that depends on or interacts with the target |
| `target_asset_id` | string | Supporting, enabling or connected asset |
| `dependency_type` | string | Nature of the relationship |
| `direction` | string | Relationship directionality |
| `criticality` | string | Importance of this specific link |
| `effect_if_lost` | string | Plain-language synthetic effect of dependency loss |
| `degradation_factor` | number | Synthetic 0.00–1.00 impact modifier |
| `redundancy` | string | Availability of alternate paths |
| `alternate_asset_ids` | string array | Potential alternate assets, if any |
| `rationale` | string | Synthetic explanation of the relationship |

Allowed `dependency_type` values:

```text
communications
maintenance_support
supply_support
basing
logistics_transport
sensor_data
power_and_site_services
coordination
```

Allowed `direction` values:

```text
source_requires_target
bidirectional
```

Allowed `redundancy` values:

```text
none
partial
full
```

### health-events.json

Top-level array: `events`

Health events represent known conditions before or during a scenario. They are not telemetry; they are curated synthetic context records.

| Field | Type | Definition |
|---|---|---|
| `event_id` | string | Unique health-event identifier |
| `asset_id` | string | Affected asset |
| `event_type` | string | Type of maintenance, degradation or readiness event |
| `title` | string | Short display title |
| `status` | string | Workflow state of the event |
| `severity` | string | Relative severity |
| `reported_at` | ISO 8601 timestamp | When the synthetic event was reported |
| `expected_resolution_at` | ISO 8601 timestamp/null | Expected resolution time, if known |
| `health_score_before` | number | Synthetic health score before the event |
| `health_score_current` | number | Synthetic current health score |
| `readiness_before` | number | Synthetic readiness before the event |
| `readiness_current` | number | Synthetic current readiness |
| `operational_effect` | string | Abstract consequence in the fictional system |
| `affected_dependency_ids` | string array | Linked dependency IDs |
| `recommended_initial_action` | string | Suggested starting point, not a mandatory decision |
| `confidence` | number | Confidence in the synthetic event assessment, 0.00–1.00 |
| `scenario_tags` | string array | Search and grouping tags |

Allowed `event_type` values:

```text
scheduled_maintenance
corrective_maintenance
component_fault
sensor_degradation
communications_degradation
logistics_constraint
site_service_disruption
inspection_finding
readiness_update
```

Allowed event `status` values:

```text
scheduled
open
in_progress
monitoring
under_review
closed
```

### spares.json

Top-level array: `spares`

| Field | Type | Definition |
|---|---|---|
| `spare_id` | string | Unique spare/support-item identifier |
| `part_number` | string | Fictional part number |
| `name` | string | Fictional item name |
| `part_category` | string | Item category |
| `stocking_asset_id` | string | Depot, base or facility holding the item |
| `primary_supported_asset_ids` | string array | Assets supported by the item |
| `stock_status` | string | Current synthetic stock state |
| `quantity_on_hand` | integer | Available physical synthetic quantity |
| `quantity_reserved` | integer | Quantity already allocated to another demand |
| `reorder_point` | integer | Threshold that triggers a notional replenishment concern |
| `target_stock_level` | integer | Desired synthetic stock level |
| `lead_time_days` | integer | Standard synthetic replenishment lead time |
| `expedite_lead_time_days` | integer | Accelerated synthetic lead time |
| `supply_risk` | string | Relative supply exposure |
| `criticality` | string | Relative operational importance |
| `substitute_available` | boolean | Whether a substitute record exists |
| `substitute_spare_ids` | string array | IDs of possible substitute items |
| `substitution_constraints` | string | Limitations/trade-offs of use |
| `associated_dependency_ids` | string array | Dependencies affected by the item |
| `notes` | string | Additional fictional context |

Allowed `stock_status` values:

```text
in_stock
low_stock
out_of_stock
reserved
in_transit
```

Allowed `supply_risk` values:

```text
low
medium
high
```

### capabilities.json

Top-level array: `capabilities`

Capabilities are abstract indicators for visualising impact. They are **not** real readiness, coverage, mission or force-effectiveness measures.

| Field | Type | Definition |
|---|---|---|
| `capability_id` | string | Unique abstract capability identifier |
| `name` | string | Display name |
| `description` | string | Definition of the abstract capability |
| `domain` | string | Functional domain |
| `unit` | string | Always `capability_index` in this pack |
| `baseline_target_index` | number | Desired synthetic baseline |
| `warning_threshold` | number | Threshold for a strained state |
| `critical_threshold` | number | Threshold for a critical state |
| `primary_risk_drivers` | string array | Common drivers of degradation |
| `recommended_resilience_actions` | string array | Generic synthetic action patterns |
| `contributions` | array | Asset contribution records |

Contribution fields:

| Field | Type | Definition |
|---|---|---|
| `asset_id` | string | Contributing asset |
| `contribution_weight` | number | Relative contribution weight; not required to sum to 1.00 |
| `contribution_role` | string | Plain-language role |
| `minimum_asset_status` | string | Lowest status that can still contribute |
| `dependency_ids` | string array | Dependencies affecting the contribution |
| `degradation_note` | string | Explanation of how contribution may be reduced |

Baseline calculation guidance in `capabilities.json` is optional. Teams may replace it with another transparent approach, provided they cite the assets, dependencies, events, spares and scenario conditions used.

### locations.geojson

Top-level type: GeoJSON `FeatureCollection`

Every feature maps to one record in `assets.json` through `properties.asset_id` and `id`.

| Field | Type | Definition |
|---|---|---|
| `geometry.coordinates` | number array | Diagrammatic WGS84 `[longitude, latitude]` coordinates |
| `properties.asset_id` | string | Matching `assets.asset_id` |
| `properties.name` | string | Fictional asset name |
| `properties.feature_type` | string | Visual category |
| `properties.asset_type` | string | Matching asset type |
| `properties.label` | string | Map label |
| `properties.symbol` | string | Suggested UI icon/category |
| `properties.status` | string | Display state at creation time |
| `properties.diagram_position` | object | Optional `{x, y}` graph-layout position |

Coordinates are intentionally diagrammatic. Do not use them for navigation, distance calculation, operational analysis or inference about real geography.

### Resilience scenarios.json

Top-level array: `scenarios`

| Field | Type | Definition |
|---|---|---|
| `scenario_id` | string | Unique resilience scenario ID |
| `title` / `short_name` | string | Display title and short label |
| `category` | string | Scenario grouping |
| `difficulty` | string | Suggested build/demo complexity |
| `duration_hours` | number | Synthetic scenario duration |
| `narrative` | string | Plain-language scenario framing |
| `initial_conditions` | object | Existing events, alternatives and constraints |
| `injects` | array | State changes applied by the scenario |
| `primary_affected_assets` | string array | Main impacted assets |
| `primary_affected_dependencies` | string array | Main impacted dependency links |
| `expected_impacts` | object | Evaluation anchors and questions |
| `possible_actions` | array | Candidate mitigations with trade-offs |
| `evaluation_anchors` | object | Minimum evidence and valid outcome types |

Scenario injects may target an `asset_id` or `spare_id` and modify an attribute such as `status`, a capacity modifier, a readiness modifier, quantity, or repair demand. Treat injects as temporary overlays; do not permanently overwrite canonical records.

## Co-pilot pack

Path: `data/copilot/`

The co-pilot pack models a fictional maintenance/support workflow: select a platform, compartment, system and task; retrieve applicable information; apply configuration rules; inspect issue history; and draft a traceable report.

### systems.json

This file contains three arrays: `platforms`, `compartments`, and `systems`.

#### Platforms

| Field | Type | Definition |
|---|---|---|
| `platform_id` | string | Unique platform ID |
| `name` | string | Fictional display name |
| `platform_class` | string | Fictional class or family |
| `platform_type` | string | General platform category |
| `lifecycle_status` | string | Lifecycle state |
| `support_location` | string | Fictional support location name |
| `configuration_baseline` | string | Top-level fictional baseline |
| `notes` | string | Context note |

Allowed `lifecycle_status` values:

```text
refit
in_service
maintenance
```

#### Compartments

| Field | Type | Definition |
|---|---|---|
| `compartment_id` | string | Unique compartment ID |
| `platform_id` | string | Parent platform |
| `name` | string | Fictional compartment name |
| `compartment_type` | string | Space category |
| `deck_or_zone` | string | Diagrammatic local position |
| `space_limit_weight_kg` | number | Synthetic space constraint |
| `space_limit_volume_m3` | number | Synthetic volume constraint |
| `power_budget_kw` | number | Synthetic power budget |
| `environmental_constraints` | string array | Applicable space constraints |
| `notes` | string | Context note |

Allowed `compartment_type` values:

```text
operations_space
sensor_space
machinery_space
electronics_space
```

#### Systems

| Field | Type | Definition |
|---|---|---|
| `system_id` | string | Unique installed-system ID |
| `platform_id` | string | Parent platform |
| `compartment_id` | string | Hosting compartment |
| `system_type` | string | Functional system category |
| `name` | string | Fictional display name |
| `model` | string | Fictional model identifier |
| `configuration_revision` | string | Hardware/configuration revision |
| `software_revision` | string/null | Software or firmware revision where applicable |
| `status` | string | Installation/maintenance state |
| `criticality` | string | Relative task importance |
| `power_kw`, `weight_kg`, `volume_m3` | number | Synthetic resource attributes |
| `maintenance_state` | string | Detailed work state |
| `applicable_document_set` | string | Expected document-set identifier |
| `notes` | string | Context note |

Allowed `system_type` values:

```text
mission_management_console
sensor_processing_rack
cooling_distribution_unit
auxiliary_power_unit
surface_sensor_interface
secure_communications_gateway
auxiliary_cooling_pump
command_information_console
```

### tasks.json

Top-level array: `tasks`

| Field | Type | Definition |
|---|---|---|
| `task_id` | string | Unique task ID |
| `title` | string | Task display title |
| `task_type` | string | Work category |
| `status` | string | Current synthetic workflow state |
| `platform_id`, `compartment_id`, `system_id` | string | Selected context |
| `priority` | string | Relative scheduling importance |
| `risk_category` | string | Synthetic task risk class |
| `estimated_duration_hours` | number | Synthetic planning estimate |
| `planned_start_date` | ISO date | Fictional planned date |
| `required_document_ids` | string array | Applicable information-object IDs |
| `required_document_set` | string | Expected document-set identifier |
| `preconditions` | string array | Conditions before task start/release |
| `required_resources` | string array | Generic role/equipment requirements |
| `post_task_requirements` | string array | Follow-on task IDs |
| `known_config_issue` | boolean | Whether a known configuration risk is seeded |
| `known_config_issue_description` | string | Explanation of the risk |
| `expected_outcome` | string | Desired synthetic result |
| `report_template_id` | string | Report template to use |
| `notes` | string | Context note |

Allowed `task_type` values:

```text
inspection
corrective_maintenance
preventive_maintenance
installation
configuration_verification
post_maintenance_test
software_update
functional_test
```

Allowed task `status` values:

```text
planned
ready_to_start
in_progress
blocked
awaiting_test
complete
deferred
```

### information-objects.json

Top-level array: `information_objects`

Information objects are short, synthetic, text-based substitutes for technical procedures, safety notes, checklists and drawing descriptions. They are intentionally concise to support fast retrieval and explanation during the sprint.

| Field | Type | Definition |
|---|---|---|
| `information_object_id` | string | Unique information-object ID |
| `document_type` | string | Type of information object |
| `title` | string | Display title |
| `revision` | string | Document revision |
| `effective_date` | ISO date | Synthetic effective date |
| `document_set` | string | Related document set |
| `applicable_system_types` | string array | System types within scope |
| `applicable_models` | string array | Models within scope |
| `applicable_configuration_revisions` | string array | Hardware/configuration revisions within scope |
| `applicable_task_types` | string array | Task types within scope |
| `status` | string | Current, obsolete, or other applicability state |
| `summary` | string | Short description |
| `content_text` | string | Search/RAG-ready synthetic content |
| `key_parameters` | object | Synthetic technical or workflow values |
| `related_drawing_ids` | string array | Associated drawing-description IDs |
| `safety_note_ids` | string array | Associated safety-note IDs |
| `keywords` | string array | Search terms |
| `warning` | string | Applicability or safety warning |

Allowed `document_type` values:

```text
maintenance_procedure
installation_procedure
inspection_procedure
test_procedure
configuration_control_procedure
software_update_procedure
safety_note
drawing_description
checklist
```

Common document `status` values:

```text
current
obsolete_for_revision_D
obsolete_for_revision_E
```

Treat `content_text` as the primary RAG/search field. Always combine text retrieval with applicability filtering on model, configuration revision, task type, document set and document status.

### configuration-rules.json

Top-level array: `rules`

Rules provide deterministic synthetic guardrails. Teams can implement them directly, use them as labels for an AI workflow, or combine them with retrieval.

| Field | Type | Definition |
|---|---|---|
| `rule_id` | string | Unique configuration-rule ID |
| `title` | string | Rule display name |
| `rule_type` | string | Rule category |
| `severity` | string | Rule impact level |
| `applies_to` | object | System/model/revision/task applicability context |
| `conditions` | object | Required, disallowed, sequence or threshold conditions |
| `violation_message` | string | Operator-readable warning |
| `required_action` | string | Recommended system response |
| `evidence_to_display` | string array | IDs/fields to show in UI explanation |
| `rationale` | string | Synthetic rationale |
| `test_case_hint` | string | Suggested scenario or test |

Allowed `rule_type` values:

```text
document_applicability
hardware_software_compatibility
mandatory_test
task_sequence
physical_constraint
checklist_applicability
configuration_evidence
```

Allowed rule `severity` values:

```text
info
warning
major
critical
```

### issue-history.json

Top-level array: `issues`

Historical issues provide context, risk hints and examples of what can go wrong. They are not a source of universal rules; use the linked configuration rule and applicable information object as the governing evidence.

| Field | Type | Definition |
|---|---|---|
| `issue_id` | string | Unique issue ID |
| `title` | string | Short finding title |
| `issue_type` | string | Category of deviation or history item |
| `status` | string | Current synthetic issue state |
| `severity` | string | Impact level |
| `reported_date`, `closed_date` | ISO date/null | Synthetic record dates |
| `platform_id`, `compartment_id`, `system_id` | string | Context identifiers |
| `related_task_id` | string | Related task |
| `related_rule_id` | string | Governing configuration rule |
| `related_information_object_ids` | string array | Related information objects |
| `description` | string | What happened |
| `detected_by` | string | Synthetic detection method |
| `root_cause` | string | Synthetic causal explanation |
| `impact` | string | Consequence in the fictional context |
| `immediate_action` | string | Initial containment action |
| `corrective_action` | string | Follow-up control improvement |
| `lesson_learned` | string | Reusable insight |
| `risk_hint` | string | Simple UI prioritisation value |
| `tags` | string array | Search/grouping tags |

Allowed `issue_type` values:

```text
configuration_mismatch
obsolete_document_use
missing_post_maintenance_test
inspection_deviation
rework
incomplete_traceability
software_hardware_mismatch
open_finding
```

Allowed issue `status` values:

```text
open
under_review
corrective_action_in_progress
closed
accepted_with_limitations
```

### report-templates.json

Top-level array: `templates`

Templates define report structures. They should be used to pre-fill context from the selected platform, compartment, system and task; they do not replace evidence collection or review.

| Field | Type | Definition |
|---|---|---|
| `template_id` | string | Unique template ID |
| `template_type` | string | Report category |
| `title` | string | Display title |
| `revision` | string | Template revision |
| `applicable_system_types` | string array | System types within scope |
| `applicable_task_types` | string array | Tasks within scope |
| `applicable_models` | string array | Models within scope |
| `purpose` | string | Intended use |
| `prefill_fields` | string array | Context fields to auto-fill |
| `required_fields` | string array | User/system fields required before completion |
| `checklist_items` | array | Structured checklist entries |
| `structured_fields` | array | Controlled-value or numeric fields |
| `free_text_fields` | array | Narrative fields |
| `required_attachments` | string array | Evidence references required |
| `release_options` | string array | Available closure/release states |
| `required_signoff_roles` | string array | Fictional role requirements |
| `validation_rules` | string array | Human-readable validation guidance |

Allowed `template_type` values:

```text
maintenance_installation_report
inspection_report
test_and_configuration_closure_report
```

### Co-pilot scenarios.json

Top-level array: `scenarios`

| Field | Type | Definition |
|---|---|---|
| `scenario_id` | string | Unique co-pilot scenario ID |
| `title` / `short_name` | string | Display title and short label |
| `category` | string | Scenario grouping |
| `difficulty` | string | Suggested prototype complexity |
| `narrative` | string | Plain-language framing |
| `entry_context` | object | Initial platform, compartment, system and task selection |
| `injects` | array | Selected document, missing evidence or task-state override |
| `must_identify` | string array | Concepts a successful prototype should identify |
| `required_evidence_record_ids` | string array | IDs expected in explanation or traceability view |
| `expected_conceptual_outcomes` | string array | Valid behavioural outcomes |
| `acceptable_actions` | string array | Acceptable response patterns |
| `demo_prompt` | string | Suggested participant demo question |
| `success_criteria` | string array | Evaluation anchors |

Co-pilot scenario injects are temporary test conditions. Examples include selecting an obsolete procedure, removing a test result, setting a prior task to incomplete, or requesting an unsupported verification status.

## Entity relationships

### Resilience relationship map

```text
assets
  ├─< dependencies.source_asset_id
  ├─< dependencies.target_asset_id
  ├─< health_events.asset_id
  ├─< spares.stocking_asset_id
  ├─< spares.primary_supported_asset_ids[]
  ├─< capabilities.contributions[].asset_id
  └─< locations.features[].properties.asset_id

dependencies
  ├─< health_events.affected_dependency_ids[]
  ├─< spares.associated_dependency_ids[]
  ├─< capabilities.contributions[].dependency_ids[]
  └─< scenarios.primary_affected_dependencies[]

assets / dependencies / spares / capabilities
  └─< scenarios injects, affected-record lists, actions and evaluation anchors
```

### Co-pilot relationship map

```text
platforms
  ├─< compartments.platform_id
  ├─< systems.platform_id
  └─< tasks.platform_id

compartments
  ├─< systems.compartment_id
  └─< tasks.compartment_id

systems
  ├─< tasks.system_id
  ├─< issues.system_id
  └─< scenarios.entry_context.system_id

tasks
  ├─< tasks.post_task_requirements[]
  ├─< tasks.required_document_ids[] -> information_objects
  ├─< tasks.report_template_id -> report_templates
  ├─< issues.related_task_id
  └─< scenarios.entry_context.task_id

information_objects
  ├─< configuration_rules conditions and evidence references
  ├─< issue-history related_information_object_ids[]
  └─< report templates checklist references

configuration_rules
  ├─< issue-history.related_rule_id
  ├─< report-template checklist references
  └─< scenario required_evidence_record_ids[]
```

## Cross-pack boundaries

The two packs can be used independently. They use different abstraction levels and should not be treated as a shared operational database.

| Topic | Co-pilot pack | Resilience pack | Boundary |
|---|---|---|---|
| Primary user | Technician, engineer, configuration controller | Planner, operations lead, support/logistics decision-maker | Do not force teams to use both packs |
| Main unit of analysis | Platform → compartment → system → task | Asset → dependency → capability → scenario | IDs are intentionally separate (`PLT-` vs `AST-`) |
| Core question | “What applies, what is missing, and may this work proceed?” | “What changes under disruption, and what action improves resilience?” | Different reasoning models |
| Technical information | Procedures, tests, safety notes, checklists, drawing descriptions | Health events, spares, supply constraints, abstract capability contributions | Do not infer real technical content from either pack |
| Geospatial context | None required | Diagrammatic `locations.geojson` | Co-pilot does not depend on map data |
| Scenario structure | Task-level evidence, applicability and workflow tests | Network-level disruption and mitigation tests | Scenarios are not interchangeable |
| Standards stance | Configuration/support concepts only | Logistics/support-system concepts only | Neither pack claims S3000L or GEIA-STD-0007 conformance |

Optional cross-pack integration is allowed as an advanced feature. For example, a team may show that a resilience spare-shortage scenario changes the priority of a co-pilot maintenance task. Such integration must remain explicitly fictional and must preserve the separate identifiers and evidence chains of both packs.

## Lovable and Supabase import guidance

Teams may use JSON directly, but a relational import commonly uses these table groups:

```text
Resilience:
assets, dependencies, health_events, spares, capabilities,
capability_contributions, scenarios, scenario_injects, locations

Co-pilot:
platforms, compartments, systems, tasks, information_objects,
configuration_rules, issues, report_templates, report_template_checklist_items,
copilot_scenarios, copilot_scenario_injects
```

For Lovable prototypes, preserve canonical IDs as text primary keys. Use array fields as JSONB where speed matters, or normalise them into link tables where a team wants advanced filtering, graph traversal or reporting. A team-owned Supabase project may add users, notes, report instances, chat sessions, embeddings and derived scores without altering the supplied canonical source records.

## Minimum traceability standard

A successful prototype should expose the following when it makes a recommendation or blocks a workflow:

| Challenge | Minimum evidence to show |
|---|---|
| Co-pilot | Selected `platform_id`, `compartment_id`, `system_id`, `task_id`, applicable `information_object_id`, relevant `rule_id`, and any required missing evidence |
| Resilience | Selected `scenario_id`, impacted `asset_id` values, relevant `dependency_id` path(s), health-event/spare evidence where used, capability ID and action trade-off |

If this evidence cannot be shown, the prototype should label the output as a hypothesis or insufficient-data condition rather than a verified result.
