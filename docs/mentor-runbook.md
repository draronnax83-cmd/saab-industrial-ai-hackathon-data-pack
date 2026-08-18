# Mentor Runbook

This runbook is for Saab domain mentors, technical mentors and organiser-side support staff during the Industrial AI Hackathon.

The goal is to help teams build useful, evidence-backed prototypes from the synthetic challenge data without disclosing sensitive information, prescribing one solution, or turning mentors into a bottleneck.

## Mentor role

Mentors should help teams:

- Understand the fictional operational problem and intended user workflow.
- Navigate the supplied data pack and scenario structure.
- Identify a feasible 10-hour MVP.
- Challenge unsupported assumptions and encourage evidence-backed reasoning.
- Think through intermittent connectivity, human review, security boundaries and degraded modes.
- Prepare a clear, credible final demo.

Mentors should **not**:

- Reveal or discuss classified, export-controlled, customer-specific, proprietary or operationally sensitive information.
- Confirm whether synthetic data resembles real systems, locations, processes, capabilities or dependencies.
- Provide real technical values, maintenance instructions, configuration guidance, readiness insight or operational recommendations.
- Write substantial portions of a team’s solution or choose the winner.
- Require teams to use a particular model, cloud service, database or architecture.

## Core mentor message

Use this baseline framing with all teams:

> The data is fictional and intentionally simplified. Build a useful operator, technician or planner workflow around the supplied evidence. Do not try to make it “more realistic” by adding real information. A strong prototype shows context, evidence, reasoning, action and trade-off—and requests human review when data is incomplete.

## Challenge overview

| Track | Intended user | Core decision | Minimum viable prototype |
|---|---|---|---|
| Operational Co-pilot | Technician, engineer, configuration controller | “What information applies, what is missing, and may this task proceed or close?” | Context selector, applicable documents, rule/warning panel, evidence IDs and a report/workflow output |
| Resilience Engine | Planner, operations lead, logistics/support decision-maker | “What changes under disruption, what capability is affected, and what action has the best transparent trade-off?” | Scenario selector, asset/dependency view, impact explanation, evidence IDs and action comparison |

The co-pilot prototype should start from **platform → compartment → system → task**. The resilience prototype should start from **scenario → affected assets/dependencies → capability impact → action trade-off**.

## Data-pack orientation

### Resilience pack

```text
data/resilience/
├── assets.json              # 18 fictional assets
├── dependencies.json        # 36 typed links
├── health-events.json       # 10 current-condition events
├── spares.json              # 12 logistics/spares records
├── capabilities.json        # 5 abstract capability indices
├── locations.geojson        # diagrammatic map/graph positions
└── scenarios.json           # 4 disruption scenarios
```

Recommended first scenario: **`SCN-004` — Regional Communications Relay Disruption**.

A good first team question:

> “Which fictional assets lose their primary coordination path when the regional relay fails, what fallback remains, and what is the confidence/trade-off of each mitigation?”

### Co-pilot pack

```text
data/copilot/
├── systems.json             # platforms, compartments, systems
├── tasks.json               # 15 work tasks and follow-on links
├── information-objects.json # procedures, tests, safety notes, checklists
├── configuration-rules.json # 8 explicit rules
├── issue-history.json       # 7 historical synthetic issues
├── report-templates.json    # 3 report structures
└── scenarios.json           # 4 task-level scenarios
```

Recommended first scenario: **`COP-SCN-001` — APR-220 Revision-D Procedure Mismatch**.

A good first team question:

> “Can this technician use the open procedure to replace the module on this selected rack, and if not, what evidence explains the block?”

## Event-day cadence

| Time | Mentor activity | Expected team state |
|---:|---|---|
| 09:00–10:00 | Opening, challenge framing, safety/boundary reminder | Teams formed; challenge and scenario selected |
| 10:00–11:00 | First office-hour pass: confirm MVP scope | First screen/data load or workflow sketch exists |
| 11:00–13:00 | Roaming technical/domain support | Teams build core flow and load data |
| 13:00–14:00 | Mid-sprint checkpoint | Teams can show one scenario or task path end-to-end |
| 14:00–16:00 | Challenge assumptions, evidence, trade-off quality | Teams add reasoning, actions, report output or scenario comparison |
| 16:00–17:00 | Demo-readiness pass | Teams have a stable demo path and fallback plan |
| 17:00–18:00 | Pitch coaching, no major scope changes | Teams rehearse evidence-backed narrative |
| 18:00 onward | Demos and judging support | Mentors observe; judges assess independently |

Adapt the exact times to the published event schedule. The important checkpoints are: **scope by hour 1, working path by mid-sprint, stable demo by the final two hours**.

## First mentor conversation

Aim for 5–8 minutes. Ask these questions in order:

1. **Who is the user?** Technician, configuration controller, planner, logistics/support lead, or another explicit role?
2. **What one scenario or task will you demo?** Ask for its ID.
3. **What decision or workflow gate will your product support?**
4. **Which three to five data records will you use first?**
5. **What is the smallest working screen or output you can show within the next hour?**
6. **What happens when evidence is missing or data is degraded?**
7. **What is the trade-off or human-review point?**

If a team cannot answer these, advise them to reduce scope before discussing architecture.

## MVP scope guidance

### Resilience: acceptable MVP

A resilient MVP can be as small as:

- Scenario selection for `SCN-004`.
- A list or graph of affected assets and dependencies.
- A clear view of `AST-COMMS-002` outage, `AST-COMMS-003` degraded fallback, and the impact on `CAP-005`.
- Two or three action options drawn from the scenario.
- Evidence IDs and one explicit trade-off.

It does **not** need a sophisticated simulation, a real map, a full graph database, or predictive machine learning.

### Co-pilot: acceptable MVP

A co-pilot MVP can be as small as:

- Context selection for `PLT-001 → CPT-002 → SYS-002 → TASK-001`.
- A document list filtered by configuration revision.
- A visible block when `INFO-APR-INST-REV-B` is selected.
- A comparison to `INFO-APR-INST-REV-D`.
- A next-action button: “Use current procedure” or “Request configuration review.”
- Evidence IDs and `CFG-RULE-001` visible.

It does **not** need a full RAG stack, a sophisticated agent, real drawings, OCR, or a large document corpus.

## Mid-sprint checkpoint

At the mid-sprint check, ask each team to show—not describe—the following:

| Question | Good answer |
|---|---|
| Can you load or display real supplied data? | A visible JSON-driven list, table, graph, report or card |
| Can you run one scenario or task context? | A selected scenario/task with IDs shown |
| Can you show evidence? | Source record IDs, document IDs, dependency IDs or rule IDs |
| Can you demonstrate a decision/gate? | A warning, blocked state, ranked option or report state |
| Can you explain a limitation? | Missing evidence, degraded fallback, substitute constraint or human-review requirement |

If the answer to several rows is “not yet,” recommend a narrower scope immediately.

## Mentor interventions by issue

| Team issue | Recommended intervention |
|---|---|
| Team is building a generic chatbot | Ask them to choose one scenario/task and require cited IDs in every response |
| Team has a beautiful UI but no data logic | Ask them to implement one deterministic rule or one scenario inject before more UI work |
| Team is overbuilding a simulation | Ask for a first end-to-end scenario result using simple assumptions and static data |
| Team wants real data | Reiterate the boundary; redirect to synthetic extensions or approved public generic data |
| Team is stuck on Supabase/Lovable setup | Suggest static JSON first; persistence is optional for a valid prototype |
| Team relies on paid/cloud AI | Ask for a deterministic or local fallback for the primary demo path |
| Team has no trade-off | Ask “What gets worse if you take this action?” |
| Team’s result has no evidence | Require a source/evidence drawer with IDs before final demo |
| Team asks whether synthetic detail is realistic | Say: “Treat it as the governing fictional world for this challenge; do not map it to real systems.” |
| Team wants to bypass a configuration gate | Ask what evidence would make the state valid; do not approve an unsupported shortcut |

## Domain coaching prompts

Use these prompts to guide thinking without giving away sensitive information.

### Co-pilot prompts

- “What identifies the correct context: system type alone, or model, revision, task and document applicability as well?”
- “What record proves this procedure applies?”
- “What must happen before the task can be marked complete?”
- “What information should a technician see first, and what should be hidden until needed?”
- “How does the user know this is a rule-based block rather than an AI opinion?”
- “What does your prototype do if the correct procedure cannot be found?”
- “Can your report draft preserve platform, system, task, procedure and evidence IDs automatically?”

### Resilience prompts

- “What is directly affected, and what is affected through a dependency path?”
- “Which dependency type explains the impact: supply, maintenance, basing, communications or logistics?”
- “What fallback exists, and why is it not equal to normal operation?”
- “Which capability index changes, and what records explain it?”
- “What does your recommended action improve, and what new exposure does it create?”
- “Can an operator see the difference between an unavailable asset, a degraded asset and a low-confidence assumption?”
- “What would make you request review rather than recommend action?”

## Security and boundary escalation

If a team mentions, shows, uploads or asks for any potentially real sensitive content:

1. Stop the discussion of the content.
2. Do not copy it into notes, prompt text, a public chat, an issue tracker or a slide.
3. Say: “Please do not add or discuss real operational, technical, customer or restricted information here. We need to use the fictional pack only.”
4. Notify the technical chair or designated Saab challenge owner through the private event escalation channel.
5. Follow the process in `SECURITY-AND-BOUNDARIES.md`.

Examples requiring escalation include real technical documents, real readiness information, non-public system details, facility locations, credentials, internal URLs, screenshots from internal tools or customer material.

## Lovable and Supabase support boundaries

Mentors may help teams use Lovable prompts, static JSON or a team-owned Supabase project. Use these principles:

- Static JSON is the fastest valid starting point.
- Supabase is optional; do not let database setup consume the sprint.
- Canonical seed data should remain read-only.
- Store notes, overlays, draft reports and derived values separately.
- Never ask a team to share credentials, service-role keys or access to a private workspace.
- If a shared read-only backend is available, explain that it is an accelerator, not a dependency.
- If cloud access fails, steer teams to a local/static demonstration path.

## Demo coaching checklist

During the final demo-readiness pass, ask teams to confirm:

- [ ] One explicit user and one explicit scenario/task.
- [ ] A working happy path or baseline state.
- [ ] A visible injected error, disruption, mismatch or evidence gap.
- [ ] A response that cites relevant IDs.
- [ ] A clear action, workflow gate or report outcome.
- [ ] At least one trade-off, limitation or human-review requirement.
- [ ] A reset/fallback path if the cloud/LLM/demo service fails.
- [ ] The fictional-data disclaimer in the final pitch or app footer.

Recommended demonstration narrative:

> “This fictional user is trying to make this decision. These supplied records establish the baseline. This scenario inject changes the context. Our prototype identifies the impact using these IDs. It recommends or blocks this action because of these constraints. Here is the trade-off and where human review is required.”

## Mentor notes for judging

Mentors may be asked clarifying questions during judging but should not advocate for a particular team or disclose non-public context.

When discussing a prototype, focus on observable qualities:

- Does it use the supplied data rather than purely invented mock content?
- Does it show a coherent user workflow?
- Are warnings, recommendations and reports traceable to evidence?
- Does it handle degraded conditions, missing evidence or uncertainty responsibly?
- Is the proposed action understandable and bounded by visible trade-offs?
- Is the prototype functional within the demonstrated scenario?

Do not reward apparent domain realism achieved through invented sensitive-looking detail. Reward clarity, traceability, useful workflow design and responsible reasoning.

## Mentor quick reference

| Need | File |
|---|---|
| Pack purpose, setup and boundaries | `README.md` |
| Field definitions and relationships | `docs/data-dictionary.md` |
| Scenario cards and expected demos | `docs/scenario-guide.md` |
| Lovable prompt patterns | `docs/lovable-prompts.md` |
| Synthetic-data licence/use notice | `LICENSE-DATA.md` |
| Security and escalation process | `SECURITY-AND-BOUNDARIES.md` |
| Pack contents and validation targets | `manifest.json` |

## Final reminder

The mentor’s highest-value contribution is not an answer to a technical question. It is helping a team turn a broad idea into a **small, demonstrable, evidence-backed workflow** that respects the synthetic-data boundaries and can be shown reliably at the end of the day.
