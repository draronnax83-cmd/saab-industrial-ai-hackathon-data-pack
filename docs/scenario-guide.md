# Scenario Guide

Use this guide to turn the synthetic datasets into a focused, evidence-backed demo during the 10-hour sprint. It is written for participants, mentors and judges.

The JSON scenario files contain the canonical machine-readable facts. This guide explains how to use them: choose a scenario, apply its temporary injects, show the resulting decision problem, cite the evidence, and demonstrate a useful response.

## How to use scenarios

1. Choose **one challenge track** and one recommended starting scenario.
2. Load the canonical data for that track. Do not overwrite it.
3. Treat scenario `injects` as temporary overlays, such as a changed asset status, a missing test result, an unavailable spare or a selected obsolete document.
4. Show the initial state, then the injected/degraded state.
5. Explain your result using the required record IDs.
6. Propose a human-reviewable action, including its trade-off or limitation.

Teams may use rules, direct filtering, RAG, graph analysis, deterministic calculations, LLMs or a hybrid approach. A prototype is not required to reproduce the baseline scoring model, but it must be clear about its assumptions and evidence.

## Demo standard

A strong 3–5 minute demo follows this structure:

1. **Context** — Who is the user and what decision are they trying to make?
2. **Evidence** — Which records, documents, links, events or rules are relevant?
3. **Change** — What scenario inject or mismatch has occurred?
4. **Reasoning** — How did the prototype identify impact, a workflow gate or a constraint?
5. **Action** — What should the user do next?
6. **Trade-off** — What remains uncertain, degraded, delayed or dependent on human review?

Do not present fictional output as real operational advice. If data is missing, contradictory or incomplete, show **insufficient data — request review**.

# Resilience scenarios

Use `data/resilience/` and `data/resilience/scenarios.json`.

The resilience track asks teams to reason across a fictional system of systems: assets, dependencies, health events, spares, abstract capability indices and disruption scenarios.

## Recommended first scenario

Start with **`SCN-004` — Regional Communications Relay Disruption**.

It has an intuitive story, a compact data scope, visible map/graph potential, and several valid mitigation choices. It is well suited to a Lovable dashboard: show a relay outage, affected paths, an abstract capability effect, fallback choices and confidence-aware degraded mode.

## SCN-001 — Northhaven Support Base Unavailable for Seven Days

| Item | Guidance |
|---|---|
| Primary question | “What degrades when the primary support base is unavailable for seven days, and what should be protected first?” |
| Key affected records | `AST-BASE-001`, `AST-COMMS-001`, `AST-DEP-001`, `AST-MNT-001`, `AST-PLT-001`, `DEP-021`, `DEP-023`, `HE-004`, `HE-009` |
| Main reasoning challenge | Trace direct and cascading effects across basing, maintenance, distribution and coordination dependencies |
| Expected capability focus | `CAP-003` Maritime Response Readiness; `CAP-004` Distributed Support and Sustainment; optionally `CAP-005` Operational Coordination Continuity |
| Useful visual | Dependency graph or impact list showing Northhaven as a high-centrality support node |
| Credible action | Activate `AST-BASE-002` as partial alternate support; pre-position selected critical stock; defer lower-priority maintenance |
| Trade-off to show | Eastgate is an alternate, not a full replacement: it has reduced capacity and constrained contingency throughput |

A good prototype distinguishes between an asset that has failed and an asset that is still technically available but cannot be supported, supplied, coordinated or restored efficiently.

## SCN-002 — Coastal Sensor Chain Degradation

| Item | Guidance |
|---|---|
| Primary question | “How should support and maintenance be prioritised when a degraded sensor fails while connectivity redundancy is already reduced?” |
| Key affected records | `AST-SNS-002`, `AST-SNS-003`, `AST-COMMS-003`, `AST-MNT-002`, `HE-002`, `HE-003`, `HE-006`, `DEP-015`, `DEP-016`, `DEP-017` |
| Main reasoning challenge | Separate direct sensor loss from communications and specialist-maintenance constraints |
| Expected capability focus | `CAP-001` Coastal Situational Awareness; optionally `CAP-002` Subsurface Detection Continuity and `CAP-005` Operational Coordination Continuity |
| Useful visual | Capability comparison before/after, plus a maintenance-priority panel |
| Credible action | Prioritise Eastreach diagnosis/calibration; defer or resequence planned Southbank maintenance; route priority reporting through primary relays |
| Trade-off to show | Deferring planned maintenance can protect near-term continuity but increases later maintenance exposure; a substitute may restore only partial contribution |

A good prototype makes confidence visible. A degraded fallback link is not equivalent to full redundancy.

## SCN-003 — Critical Spare Shortage During Platform Recovery

| Item | Guidance |
|---|---|
| Primary question | “Which platform should receive the available interim spare, and why?” |
| Key affected records | `SPR-004`, `SPR-011`, `AST-PLT-001`, `AST-PLT-003`, `AST-MNT-001`, `AST-LOG-001`, `HE-001`, `HE-004`, `HE-010`, `DEP-028`, `DEP-029` |
| Main reasoning challenge | Make a transparent allocation decision using stock, reservation, lead time, facility capacity and capability contribution |
| Expected capability focus | `CAP-003` Maritime Response Readiness; `CAP-004` Distributed Support and Sustainment; optionally `CAP-002` Subsurface Detection Continuity |
| Useful visual | Side-by-side allocation comparison for `AST-PLT-001` versus `AST-PLT-003` |
| Credible action | Allocate the interim item to the selected higher-impact recovery; re-prioritise reserved inventory; use the logistics-support platform for priority movement |
| Trade-off to show | The interim substitute has limited duration/assurance; allocating it to one platform leaves the other unavailable |

A good prototype does not treat this only as a stock-out. The core problem is allocation, timing and restoration capacity.

## SCN-004 — Regional Communications Relay Disruption

| Item | Guidance |
|---|---|
| Primary question | “How do we maintain coordination when a regional relay is unavailable and the fallback gateway is already degraded?” |
| Key affected records | `AST-COMMS-002`, `AST-COMMS-001`, `AST-COMMS-003`, `AST-BASE-002`, `AST-SNS-002`, `AST-PLT-002`, `HE-003`, `HE-007`, `DEP-015`, `DEP-032`, `SPR-006`, `SPR-012` |
| Main reasoning challenge | Identify affected relay paths, increased concentration risk and the difference between preferred and time-bounded backup power |
| Expected capability focus | `CAP-005` Operational Coordination Continuity; optionally `CAP-001` Coastal Situational Awareness and `CAP-003` Maritime Response Readiness |
| Useful visual | Network path view with normal, unavailable and degraded links; confidence-aware status labels |
| Credible action | Restore with preferred backup power; use portable power as time-bounded mitigation; reroute priority traffic through Northhaven; label non-priority traffic as degraded mode |
| Trade-off to show | Rerouting through Northhaven improves near-term continuity but creates a more concentrated single-point-of-failure risk |

A good prototype makes the confidence and duration of fallback options visible rather than simply turning an asset from red to green.

# Co-pilot scenarios

Use `data/copilot/` and `data/copilot/scenarios.json`.

The co-pilot track asks teams to support a fictional technician, engineer or configuration controller in selecting applicable information, identifying mismatches, completing tasks safely and drafting traceable reports.

## Recommended first scenario

Start with **`COP-SCN-001` — APR-220 Revision-D Procedure Mismatch**.

It is the fastest route to a compelling demo: select a platform, compartment, system and task; show the wrong document; explain why it is inapplicable; block the task; and surface the correct revision with evidence.

## COP-SCN-001 — APR-220 Revision-D Procedure Mismatch

| Item | Guidance |
|---|---|
| Participant question | “Can I use the open procedure to replace the interface module on this rack?” |
| Entry context | `PLT-001` → `CPT-002` → `SYS-002` → `TASK-001` |
| Inject | Select `INFO-APR-INST-REV-B` and `INFO-APR-DWG-REV-B` |
| Key evidence | `SYS-002`, `TASK-001`, `CFG-RULE-001`, `INFO-APR-INST-REV-B`, `INFO-APR-INST-REV-D`, `ISS-001` |
| Expected outcome | Block task start; reject revision-B documents; show revision-D procedure and drawing; explain bracket, route, torque and clearance differences |
| Credible action | Retrieve current documents, restart task review and optionally request configuration-controller review |
| Trade-off/limitation | The system should not approve work based only on matching system type; model and configuration effectivity matter |

A successful demo cites the record IDs and makes the reason for the block understandable to a technician.

## COP-SCN-002 — Sensor Rack Closure With Missing Post-Maintenance Test

| Item | Guidance |
|---|---|
| Participant question | “Can I close this maintenance package and return the rack to service?” |
| Entry context | `PLT-001` → `CPT-002` → `SYS-002` → `TASK-003` |
| Inject | Remove or leave blank the accepted test result for `TASK-002`; request closure of `TASK-003` |
| Key evidence | `TASK-001`, `TASK-002`, `TASK-003`, `CFG-RULE-002`, `CFG-RULE-008`, `INFO-APR-TEST-POST-01`, `ISS-002` |
| Expected outcome | Show the replacement → test → closure chain; block closure; identify the missing test result; draft an incomplete report with the evidence gap visible |
| Credible action | Complete or attach accepted evidence for `TASK-002`, then re-attempt closure |
| Trade-off/limitation | The co-pilot must not infer a test result or state that the system is verified without evidence |

A successful demo turns an abstract workflow condition into a clear next step for the user.

## COP-SCN-003 — Mission Console Hardware and Software Update Sequence

| Item | Guidance |
|---|---|
| Participant question | “Apply SW-4.0 to this mission console and prepare it for acceptance.” |
| Entry context | `PLT-002` → `CPT-004` → `SYS-005` → `TASK-009` |
| Inject | Set prior hardware task `TASK-008` to incomplete/planned; request software update `TASK-009` |
| Key evidence | `SYS-005`, `TASK-008`, `TASK-009`, `TASK-010`, `CFG-RULE-004`, `INFO-MCS-INST-REV-C`, `INFO-MCS-SW-UPDATE-REV-C`, `ISS-004` |
| Expected outcome | Block/defer software update; show hardware → software → acceptance-test sequence; surface readiness checklist and correct work package |
| Credible action | Complete hardware installation evidence, then authorise software update and schedule functional acceptance test |
| Trade-off/limitation | A polished UI is not enough: the app must prevent users from bypassing evidence and task sequencing |

A successful demo should show a task timeline or gate view, not only a natural-language warning.

## COP-SCN-004 — SCG-210 Revision-E Checklist Mismatch

| Item | Guidance |
|---|---|
| Participant question | “Mark this gateway configuration as verified using the open checklist.” |
| Entry context | `PLT-002` → `CPT-005` → `SYS-007` → `TASK-011` |
| Inject | Select `INFO-SCG-CHECKLIST-REV-C`; request verified status |
| Key evidence | `SYS-007`, `TASK-011`, `CFG-RULE-005`, `CFG-RULE-008`, `INFO-SCG-CHECKLIST-REV-C`, `INFO-SCG-CONFIG-REV-E`, `INFO-SCG-CHECKLIST-01`, `ISS-005` |
| Expected outcome | Flag obsolete checklist; prevent verified state; show revision-E procedure/checklist and required sign-off evidence; offer review-required closure draft |
| Credible action | Retrieve revision-E checklist, perform configuration read-back and gather required sign-off |
| Trade-off/limitation | A matching model name does not make a checklist applicable; configuration revision and evidence still govern verification |

A successful demo must clearly distinguish **document retrieval** from **document applicability**.

# Evidence and judging guidance

## Minimum traceability

| Track | A recommendation, warning or block should show |
|---|---|
| Co-pilot | `platform_id`, `compartment_id`, `system_id`, `task_id`, applicable `information_object_id`, relevant `rule_id`, and any missing evidence |
| Resilience | `scenario_id`, affected `asset_id` values, relevant `dependency_id` path(s), health-event/spare evidence where used, affected `capability_id`, action and trade-off |

## What judges should reward

- **Operational relevance** — Does the workflow fit the fictional user and decision context?
- **Evidence and traceability** — Can the user see why the system reached its conclusion?
- **Resilience and safety thinking** — Does the prototype expose uncertainty, degraded mode, assumptions and human-review gates?
- **Useful action** — Does it recommend a plausible next step, not merely describe a problem?
- **User experience** — Can a time-pressured operator, technician or planner understand what to do next?
- **Working prototype quality** — Does the demo actually use the supplied data and scenario rather than only a static presentation?

## Valid alternative approaches

Teams are not required to use the provided scoring method, recommended actions or a particular technology. A team may propose a different mitigation or workflow if it:

1. Uses the supplied fictional context.
2. Shows the evidence records and assumptions used.
3. Explains the trade-off.
4. Does not claim real-world authority or invent missing evidence.

## Avoid these failure modes

- Showing an LLM answer with no supporting record IDs.
- Treating a degraded asset or substitute as fully equivalent to normal operation.
- Overwriting canonical data rather than applying a scenario overlay.
- Presenting a “verified” or “complete” status without required evidence.
- Using real operational, technical, customer or sensitive information to enrich the fictional pack.
- Spending the entire sprint on an elaborate model without a usable operator-facing workflow.
