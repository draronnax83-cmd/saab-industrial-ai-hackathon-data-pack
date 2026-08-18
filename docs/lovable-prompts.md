# Lovable Prompt Pack

Use these prompts to accelerate creation of a working prototype in Lovable. Choose one challenge track and start with the **MVP prompt**. Then add only the extensions needed for your demo.

The supplied datasets are fictional and synthetic. Every prototype must preserve visible evidence IDs, distinguish uncertainty from verified facts, and avoid real-world operational claims.

## Before prompting

1. Create a Lovable project.
2. Choose one track: **Resilience** or **Operational Co-pilot**.
3. Use static JSON first, or connect your own Supabase project if you want persistence, filters, report instances, or scenario overlays.
4. Keep canonical seed data read-only in your app. Store edits, notes, scenario overlays and generated reports separately.
5. Copy one prompt at a time. Review the result before asking Lovable to add more.

## Shared guardrail prompt

Paste this first after creating your project.

```text
You are building a hackathon prototype using a fictional, synthetic and non-operational dataset. Do not invent real technical facts, operational information, locations, customers, readiness data or safety procedures.

Every recommendation, warning, risk score, workflow gate or generated report must show the supplied evidence record IDs used. When required evidence is missing, contradictory or outside the provided data, show: “Insufficient data — request human review.”

Do not present the app as a real-world control system. It is a decision-support and workflow demonstration only. Use a calm, professional, high-clarity interface suitable for a time-pressured industrial user. Use status labels and explicit uncertainty; do not rely on colour alone.
```

# Resilience track

Use the files in `data/resilience/`:

```text
assets.json
dependencies.json
health-events.json
spares.json
capabilities.json
locations.geojson
scenarios.json
```

Recommended first scenario: `SCN-004` — Regional Communications Relay Disruption.

## Resilience MVP prompt

```text
Build a responsive web dashboard called “Baltic Resilience Console” for a fictional maritime system-of-systems resilience challenge.

Use the supplied synthetic data files: assets, dependencies, health events, spares, capabilities, locations and scenarios. The primary user is a planner or support decision-maker who needs to understand how a disruption affects abstract capabilities and what actions are available.

Create these core views:
1. Overview: high-level capability cards for CAP-001 to CAP-005, current alerts and a ranked list of high-criticality or degraded assets.
2. Network: an interactive node-link graph of assets and typed dependencies. Use distinct symbols or labels for platforms, sensors, bases, depots, maintenance sites and communications nodes.
3. Scenario: a scenario selector with SCN-001 to SCN-004. When selected, show its injects, affected assets, impacted dependencies, expected capability trend and possible actions.
4. Asset detail: show health, readiness, criticality, supporting dependencies, relevant health events and related spares.

Start with SCN-004. Show AST-COMMS-002 as unavailable, AST-COMMS-003 as degraded/limited, and the affected relay paths. Show a clear degraded-mode confidence label rather than treating fallback connectivity as fully normal.

Every impact, recommendation or warning must show evidence IDs, including scenario_id, asset_id, dependency_id, event_id or spare_id where relevant. Add an “Assumptions and evidence” drawer to each decision card.

Do not claim that the capability scores are real operational measures. Label them “Synthetic capability index.”
```

## Resilience: Supabase setup prompt

Use after connecting Lovable to your own Supabase project.

```text
Create a Supabase-backed data model for a fictional resilience dashboard. Do not delete existing seed data.

Create tables or views for:
- assets
- dependencies
- health_events
- spares
- capabilities
- capability_contributions
- scenarios
- scenario_injects
- scenario_actions
- user_scenario_overlays
- analyst_notes

Use text IDs from the supplied datasets as primary keys for canonical records. Store scenario overlays, analyst notes and derived results in separate tables so canonical seed data remains unchanged.

Add appropriate foreign keys where practical. Add indexes for asset IDs, dependency source/target IDs, scenario IDs and event asset IDs.

Create an initial scenario overlay workflow: a user selects a scenario, applies its injects only in the UI/session or overlay table, and can reset to canonical data. Never permanently overwrite asset health, status, spare quantity or dependency values.

Create basic read/write protections so canonical tables are read-only from the application and only overlay/note tables accept user edits.
```

## Resilience: scenario runner prompt

```text
Add a simple, transparent scenario-analysis engine for the fictional resilience dashboard.

When a scenario is selected:
1. Read scenario injects as temporary overlays.
2. Identify directly affected assets, spares and dependencies.
3. Identify one-hop and two-hop dependent assets through dependency links.
4. Calculate a simple synthetic impact score using asset criticality, health_score, readiness_score, dependency criticality and scenario modifiers.
5. Show the calculation assumptions in plain language and list the source IDs.
6. Compare baseline and scenario state for each capability.

This is not a real operational model. Label all outputs as “Prototype synthetic impact estimate.” Do not invent data that is absent from the supplied records.
```

## Resilience: action comparison prompt

```text
Add an “Action comparison” panel to the scenario view.

For each possible action in the selected scenario, show:
- Action title and action_type
- Target asset IDs and related spare IDs
- Expected benefit
- Trade-off
- Implementation complexity
- Evidence records

Allow the user to select up to two actions and compare their projected synthetic impact side by side. Use clear labels such as “improves near-term continuity,” “creates concentration risk,” “uses limited substitute,” or “requires human review.” Do not state that any action is guaranteed to work.
```

## Resilience: graph and map prompt

```text
Improve the Network view with a toggle between Graph and Map.

Graph view:
- Nodes are assets.
- Edges are dependencies.
- Edge labels or tooltips show dependency_type, criticality and effect_if_lost.
- Highlight scenario-affected nodes and links.
- Allow filtering by asset type, status and dependency type.

Map view:
- Use locations.geojson only as diagrammatic context.
- Include a visible notice: “Fictional diagrammatic positions — not real locations or routes.”
- Clicking a feature opens the corresponding asset detail.

Make both views work without external map APIs. If no map tile service is available, use a simple diagrammatic coordinate canvas or static grid.
```

## Resilience: demo polish prompt

```text
Prepare a 4-minute demo mode for the Regional Communications Relay Disruption scenario.

Create a guided sequence:
1. Baseline: show operational coordination continuity at a synthetic baseline.
2. Inject: show AST-COMMS-002 becoming unavailable and reduced fallback capacity at AST-COMMS-003.
3. Explain: show affected assets, dependency paths and CAP-005 impact with evidence IDs.
4. Decide: compare preferred backup power SPR-006, portable backup SPR-012, rerouting through AST-COMMS-001 and degraded-mode operation.
5. Trade-off: show increased concentration risk at Northhaven and time-bounded fallback limitations.

Add a reset button that returns to the canonical synthetic baseline.
```

# Operational co-pilot track

Use the files in `data/copilot/`:

```text
systems.json
tasks.json
information-objects.json
configuration-rules.json
issue-history.json
report-templates.json
scenarios.json
```

Recommended first scenario: `COP-SCN-001` — APR-220 Revision-D Procedure Mismatch.

## Co-pilot MVP prompt

```text
Build a tablet-friendly web application called “Maintenance Context Co-pilot” for a fictional maritime production and support environment.

Use the supplied synthetic data files: systems, tasks, information objects, configuration rules, issue history, report templates and co-pilot scenarios.

The primary workflow is:
platform → compartment → system → task → applicable information → rule check → next action or report draft.

Create these core screens:
1. Context selector: cascading selections for platform, compartment, system and task.
2. Task workspace: task status, preconditions, required resources, required information objects, follow-on tasks and report template.
3. Applicable information: show procedures, tests, safety notes, checklists and drawing descriptions. Filter them by model, configuration revision, task type, document set and document status.
4. Configuration check: show applicable rules, warnings, blocked states and evidence IDs.
5. Issue history: show related historical issues as risk hints, but distinguish issue history from governing rules.
6. Report draft: pre-fill a selected report template from context and visibly mark missing evidence.

Start with COP-SCN-001. The user selects PLT-001, CPT-002, SYS-002 and TASK-001, then opens INFO-APR-INST-REV-B. The app must block the task because SYS-002 is configuration revision D and the selected procedure is obsolete for that revision. Surface INFO-APR-INST-REV-D and CFG-RULE-001.

Every answer and warning must display record IDs. If the app cannot confirm applicability, show “Insufficient data — request human review.”
```

## Co-pilot: Supabase setup prompt

Use after connecting Lovable to a team-owned Supabase project.

```text
Create a Supabase-backed data model for a fictional maintenance and configuration co-pilot. Do not delete existing seed data.

Create canonical tables or views for:
- platforms
- compartments
- systems
- tasks
- information_objects
- configuration_rules
- issues
- report_templates
- report_template_checklist_items
- copilot_scenarios
- copilot_scenario_injects

Create editable team-specific tables for:
- task_sessions
- session_selected_documents
- report_instances
- report_checklist_results
- report_findings
- technician_notes
- scenario_overlays

Use the supplied text identifiers as primary keys for canonical data. Preserve canonical data as read-only. Team-created reports, notes, selections, temporary scenario injects and generated summaries must be stored separately.

Create indexes for system_id, task_id, platform_id, compartment_id, information_object_id and rule_id.
```

## Co-pilot: applicability and rule-checker prompt

```text
Add a deterministic configuration and document-applicability checker.

For the selected platform, compartment, system and task:
1. Read system model, configuration_revision, software_revision and applicable_document_set.
2. Show task required_document_ids and retrieve matching information objects.
3. Filter information objects by applicable_system_types, applicable_models, applicable_configuration_revisions, applicable_task_types, document_set and status.
4. Evaluate configuration rules whose applies_to context matches the selected system and task.
5. When a rule is violated, show severity, violation_message, required_action and evidence_to_display.
6. Do not use an LLM to override deterministic rule results.

Create a clear result state: Approved for next step, Warning, Blocked, or Insufficient data — request human review.
```

## Co-pilot: RAG/search prompt

```text
Add a search and question-answering feature over the synthetic information object library and issue history.

The user can ask questions such as:
- “What test is required after replacing this module?”
- “Which procedure applies to this system revision?”
- “Why is this task blocked?”
- “Has this issue happened before?”

The answer must:
1. Start from selected platform, compartment, system and task context.
2. Prefer applicable current information objects.
3. Cite information_object_id, task_id and rule_id in the response.
4. Clearly label historical issues as supporting context, not governing procedure.
5. Refuse to invent values or approve a workflow when evidence is missing.

Show a compact Evidence section beneath every answer with links to the source records.
```

## Co-pilot: report drafting prompt

```text
Add report drafting using the supplied report templates.

When a user selects a task:
1. Find its report_template_id.
2. Pre-fill platform, compartment, system, configuration revision, task, required document IDs and known configuration issues.
3. Render the template checklist with pending/complete/not-applicable states.
4. Allow the user to enter findings, notes, deviations and sign-off names.
5. Require evidence references for required checklist items.
6. Prevent a “complete” closure decision when mandatory evidence is absent, a required test has not passed, or a configuration rule is violated.
7. Offer “Draft,” “Blocked,” “Complete with limitations,” and “Engineering review required” states as appropriate.

Use explicit field labels and preserve all record IDs in the generated report.
```

## Co-pilot: guided demo prompt

```text
Create a demo mode for the APR-220 Revision-D Procedure Mismatch scenario.

Guide the presenter through:
1. Select PLT-001 → CPT-002 → SYS-002 → TASK-001.
2. Display system configuration revision D and task context.
3. Show the intentionally selected obsolete INFO-APR-INST-REV-B procedure.
4. Trigger CFG-RULE-001 and display a critical blocked state.
5. Compare obsolete revision-B and applicable revision-D procedure details in a simple table.
6. Show the correct INFO-APR-INST-REV-D and INFO-APR-DWG-REV-D records.
7. Show related issue ISS-001 as a historical risk hint.
8. Offer to create a corrected work package or request configuration-controller review.

Use a reset button to restore the canonical scenario state.
```

## Co-pilot: alternate scenario prompts

### Missing closure test

```text
Implement COP-SCN-002. In the selected context for TASK-003, simulate that TASK-002 has no accepted post-maintenance test result. Block closure, show the replacement → test → closure chain, cite CFG-RULE-002 and CFG-RULE-008, and generate a report draft with the missing evidence visibly marked.
```

### Hardware/software update sequence

```text
Implement COP-SCN-003. For SYS-005 and TASK-009, simulate that TASK-008 hardware installation remains planned or incomplete. Block the SW-4.0 update, show the required sequence TASK-008 → TASK-009 → TASK-010, cite CFG-RULE-004, and offer a readiness checklist plus a draft hardware-installation work package.
```

### Checklist mismatch

```text
Implement COP-SCN-004. For SYS-007 and TASK-011, simulate selection of INFO-SCG-CHECKLIST-REV-C. Reject verification, show that revision-E configuration requires INFO-SCG-CONFIG-REV-E and INFO-SCG-CHECKLIST-01, cite CFG-RULE-005 and CFG-RULE-008, and create a review-required configuration-closure report draft.
```

# Shared UX and quality prompts

## Evidence drawer

```text
Add a reusable “Assumptions and evidence” drawer component to all risk cards, warnings, recommendations and report decisions.

The drawer should display:
- Conclusion status: approved, warning, blocked, degraded, hypothesis or insufficient data
- Source record IDs
- Key input values used
- Applicable rule or scenario ID
- Known limitations and assumptions
- Suggested human-review role when needed

Do not hide evidence behind a generic AI explanation.
```

## Offline and degraded-mode concept

```text
Add an architecture and UX concept for intermittent connectivity.

Show a visible connection indicator with three states: Online, Limited connectivity and Offline local data.

When offline:
- Continue showing locally loaded synthetic data.
- Queue user-created notes and report drafts locally in memory or an app state.
- Clearly label that synchronisation is pending.
- Do not pretend to call external AI services.

Add a small architecture panel explaining that the prototype can use local/static data first and optional cloud AI or Supabase sync when available.
```

## Accessibility and clarity pass

```text
Improve the application for fast industrial use:
- Use high-contrast status labels and icons, not colour alone.
- Keep key actions and current state visible without scrolling.
- Make all tables searchable and sortable.
- Use readable evidence IDs in a monospace or clearly distinct style.
- Add clear empty, loading and error states.
- Make warning and blocked states explain the next required action.
- Ensure keyboard navigation and responsive tablet layout.
```

# Optional final presentation prompt

```text
Create a presentation-ready “Demo summary” view for this hackathon prototype.

Include:
- Challenge selected
- Scenario demonstrated
- User and operational problem
- Data sources used, listed by file and key record IDs
- Architecture overview: UI, data, logic/AI, optional Supabase or LLM components
- Main finding or workflow gate
- Recommended action and trade-off
- Safety and data-boundary note: fully fictional synthetic data; decision-support demonstration only

Make it concise enough to support a 3–5 minute final pitch.
```

## Prompting tips

- Ask Lovable to build one workflow before asking for a full application.
- Use the scenario IDs and record IDs in prompts; they anchor the generated UI to the actual dataset.
- Add persistence only after the main demo works with static data.
- Do not ask Lovable to “make it realistic” by inventing data. Ask it to make the supplied fictional workflow clear, traceable and usable.
- Prefer deterministic rule checks for applicability and workflow gates; use AI/RAG for retrieval, explanation, summarisation and report drafting.
