# Operational Co-pilot — Quickstart

Build a fictional maintenance and configuration-control co-pilot for naval production and support. The goal is not a generic chatbot: build a traceable workflow that helps a technician, engineer or configuration controller select the right information, identify a conflict or missing prerequisite, and choose the next action.

## Start in 20 minutes

### 1. Use this workflow

```text
Platform → Compartment → System → Task → Applicable information → Rule check → Action/report
```

Your application should always show the selected context and the source record IDs behind its answer.

### 2. Open these files first

| File | Why it matters |
|---|---|
| `systems.json` | Platform, compartment, system model and installed configuration revision |
| `tasks.json` | The selected job, required documents, prerequisites and follow-on tasks |
| `information-objects.json` | Procedures, tests, safety notes, checklists and drawing descriptions |
| `configuration-rules.json` | Explicit conditions for warnings, blocked work and evidence requirements |
| `copilot-scenarios.json` | Ready-made demo cases, expected outcomes and evidence IDs |

Use `issue-history.json` for risk hints and lessons learned. Use `report-templates.json` to generate a traceable work, inspection or closure report.

## Recommended first scenario

Start with **COP-SCN-001 — APR-220 Revision-D Procedure Mismatch**.

**Context**

```text
Platform:    PLT-001 / NMS Skarven
Compartment: CPT-002 / Sensor Equipment Bay
System:      SYS-002 / APR-220 sensor-processing rack, configuration revision D
Task:        TASK-001 / Replace acoustic processing rack interface module
```

**Injected problem**

The user selects the obsolete `INFO-APR-INST-REV-B` procedure and `INFO-APR-DWG-REV-B` drawing description.

**Expected outcome**

- Identify that revision-B information is not applicable to configuration revision D.
- Cite `CFG-RULE-001` and show the relevant record IDs.
- Block task start.
- Surface `INFO-APR-INST-REV-D` and `INFO-APR-DWG-REV-D`.
- Explain the synthetic difference: bracket D, harness route D, 95 Nm mounting torque and cooling-clearance check.
- Recommend a practical next action: retrieve the correct work pack and restart pre-task review.

## Example user query

> Can I use the open procedure to replace the interface module on this rack?

A good response is not merely “no.” It should say *why*, show the selected system/configuration, identify the conflicting document revision, cite the rule and provide the next safe workflow step.

## Minimum viable demo

Deliver these five behaviours before adding features:

1. **Context selector** — choose platform, compartment, system and task.
2. **Applicable information panel** — show required procedures, test instructions, safety notes and drawing descriptions.
3. **Rule check** — compare system configuration, selected information object and task against `configuration-rules.json`.
4. **Evidence-backed warning** — show a clear `Blocked`, `Review required`, or `Ready` result with record IDs.
5. **Report draft** — pre-fill a report from the selected context, then visibly mark missing evidence or required next tasks.

A strong demo flow is:

```text
Select TASK-001 → select obsolete revision-B procedure → receive blocked warning → show revision-D procedure → draft installation report → create/link TASK-002 post-maintenance test.
```

## Additional scenarios

| Scenario | What it tests |
|---|---|
| `COP-SCN-002` | Missing post-maintenance test blocks closure of the sensor-rack work package |
| `COP-SCN-003` | Mission-console software update is blocked until matching hardware-update evidence exists |
| `COP-SCN-004` | Revision-E gateway cannot be verified using an obsolete revision-C checklist |

## Data and AI guardrails

- All data is fictional and non-operational.
- Do not invent a procedure, result, revision or approval when the data is missing.
- Return **“insufficient data — request engineering review”** when required evidence is absent.
- Show evidence IDs in answers, warnings and reports.
- AI may assist with retrieval, explanation and drafting; deterministic rules should control applicability and blocking decisions.

## Lovable path

1. Use the JSON files directly for the fastest start, or import them into a team-owned Supabase project.
2. Prompt Lovable to build the platform → compartment → system → task workflow.
3. Require every generated answer to display the supporting task, system, document and rule IDs.
4. Build the first scenario end to end before adding chat, document search, report export or additional features.
