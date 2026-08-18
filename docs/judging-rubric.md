# Judging Rubric

Use this rubric to evaluate prototypes built for the Saab Industrial AI Hackathon synthetic challenge kit.

The aim is to reward **working, evidence-backed and operationally useful prototypes**—not the most elaborate interface, the largest language model, or the most sensitive-looking domain detail.

All teams use fictional, synthetic and non-operational data. A prototype must not be judged more favourably because it claims or implies access to real Saab, customer, operational or restricted information.

## Scoring overview

Score each category from 0 to 5, then multiply by its weighting.

| Category | Weight | What judges assess |
|---|---:|---|
| Operational relevance and user value | 25% | Does the prototype solve a clear decision or workflow problem for a defined fictional user? |
| Evidence, traceability and data use | 25% | Does it use supplied data and show why it reached a conclusion? |
| Resilience, safety and responsible AI | 20% | Does it handle uncertainty, degradation, failure, missing evidence and human review responsibly? |
| Prototype functionality and technical execution | 15% | Does the demonstrated workflow work end to end within the chosen scenario? |
| User experience and communication | 15% | Is the prototype understandable, usable and convincingly demonstrated? |
| **Total** | **100%** |  |

### Score calculation

For each category:

\[
\text{weighted score} = \frac{\text{judge score}}{5} \times \text{category weight}
\]

The maximum total is 100 points.

## Universal scoring scale

| Score | Meaning |
|---:|---|
| 5 | Excellent: clear, complete and convincing evidence of the criterion |
| 4 | Strong: materially meets the criterion with minor gaps |
| 3 | Adequate: demonstrates the core requirement but has meaningful limitations |
| 2 | Limited: partial implementation or weak evidence |
| 1 | Minimal: mostly conceptual or substantially incomplete |
| 0 | Not demonstrated, unsafe, unsupported or outside challenge boundaries |

# Category guidance

## 1. Operational relevance and user value — 25%

**Question:** Does the team solve a specific, credible problem for a defined user in the fictional challenge world?

| Score | Indicators |
|---:|---|
| 5 | A clearly defined user has a focused decision/workflow need; the prototype materially improves speed, clarity, traceability or decision quality; the scenario/task fits naturally into the user journey |
| 4 | Strong user and problem definition; solution is useful and mostly focused, with small gaps in workflow depth or prioritisation |
| 3 | User and problem are plausible, but workflow is broad, generic or only partly connected to the chosen scenario/task |
| 2 | A general dashboard/chatbot/app concept with limited connection to a concrete operational decision |
| 1 | User need is unclear or solution is mostly technology-driven |
| 0 | No relevant problem demonstrated, or prototype relies on prohibited real-world claims/data |

### Co-pilot evidence

Strong co-pilot prototypes typically support a technician, engineer or configuration controller through a concrete workflow such as selecting applicable documents, preventing a revision mismatch, identifying missing closure evidence or drafting a traceable report.

### Resilience evidence

Strong resilience prototypes typically support a planner, operations lead or support/logistics decision-maker through a disruption scenario, showing what is affected, which capability changes, and how mitigation options differ.

## 2. Evidence, traceability and data use — 25%

**Question:** Can the user and judges see the supplied records, logic and assumptions behind the prototype’s conclusion?

| Score | Indicators |
|---:|---|
| 5 | Uses canonical data meaningfully; recommendations/warnings cite relevant IDs; dependency paths, rules, documents or scenario injects are visible; assumptions are explicit; no invented certainty |
| 4 | Strong use of supplied data and evidence, with minor gaps in one workflow or explanation |
| 3 | Uses supplied data but some key conclusions are weakly cited or the provenance UI is inconsistent |
| 2 | Data appears in the UI but conclusions are largely unsupported or manually scripted |
| 1 | Mostly generic/mock content; minimal linkage to supplied records |
| 0 | No meaningful use of supplied data, fabricated evidence, or hidden/non-approved data source |

### Minimum evidence standard

| Track | Minimum evidence expected |
|---|---|
| Co-pilot | `platform_id`, `compartment_id`, `system_id`, `task_id`, applicable `information_object_id`, relevant `rule_id`, and missing evidence where applicable |
| Resilience | `scenario_id`, affected `asset_id` values, relevant `dependency_id` paths, health-event/spare evidence when used, affected `capability_id`, action and trade-off |

A team may use LLMs or agents, but generated prose does not count as evidence on its own.

## 3. Resilience, safety and responsible AI — 20%

**Question:** Does the prototype behave responsibly under uncertainty, failure, degraded conditions or incomplete information?

| Score | Indicators |
|---:|---|
| 5 | Explicitly models or communicates degraded state, uncertainty, missing evidence and human-review gates; gives bounded recommendations with trade-offs; includes safe fallback behaviour |
| 4 | Strong safety/resilience treatment with minor gaps in one edge case or fallback path |
| 3 | Acknowledges uncertainty or degradation but does not make it central to the workflow |
| 2 | Mentions safety/resilience in slides or text but provides little behavioural support in the prototype |
| 1 | Treats all data/recommendations as certain; ignores missing evidence or degraded conditions |
| 0 | Makes unbounded operational/safety claims, bypasses critical workflow gates, or violates challenge boundaries |

### Examples of strong behaviour

- The co-pilot blocks a closure when a required post-maintenance test is missing.
- The co-pilot rejects an obsolete procedure or inapplicable checklist and names the correct evidence path.
- The resilience engine distinguishes unavailable, degraded and fallback states.
- A spare substitute displays its reduced capability/duration limitation.
- A recommendation includes what gets worse, remains unknown or requires approval.
- The app displays **“Insufficient data — request human review”** when evidence is incomplete.

## 4. Prototype functionality and technical execution — 15%

**Question:** Does the core demonstration actually work with the supplied synthetic data?

| Score | Indicators |
|---:|---|
| 5 | End-to-end workflow works reliably; data loads; scenario/task state changes are handled; key result is generated live; sensible technical architecture and fallback are evident |
| 4 | Main workflow works with small manual steps or minor instability |
| 3 | A functional core exists, but important steps are simulated, hard-coded or require significant presenter intervention |
| 2 | Limited working functionality; concept is stronger than implementation |
| 1 | Mostly slides, mockups or disconnected screens |
| 0 | No working prototype or core functionality fails during demonstration |

Judges should not require a particular technology. Static JSON, Lovable, Supabase, Python, TypeScript, graph databases, rules engines, RAG and local tools are all valid.

A team should not be penalised for choosing a simple deterministic implementation if it delivers a clear, reliable and traceable workflow.

## 5. User experience and communication — 15%

**Question:** Can a time-pressured user understand what happened, why it matters and what to do next?

| Score | Indicators |
|---:|---|
| 5 | Clear user journey, concise visual hierarchy, understandable statuses, evidence visible on demand, strong demo narrative and action-oriented interface |
| 4 | Highly usable prototype and clear pitch with minor information-density or polish issues |
| 3 | Understandable but some screens, terms or demo steps are confusing or overly dense |
| 2 | UI/pitch requires substantial explanation; next action is unclear |
| 1 | Difficult to follow or largely presentation-driven |
| 0 | No coherent user workflow or no understandable demonstration |

Reward clarity over visual complexity. A simple, reliable screen that clearly shows context → evidence → decision → trade-off is stronger than a feature-heavy dashboard with no usable flow.

# Challenge-specific checks

## Operational Co-pilot

A strong co-pilot demo should show at least one of the supplied co-pilot scenarios or an equivalent grounded workflow.

| Check | What good looks like |
|---|---|
| Context selection | User selects platform → compartment → system → task, or equivalent traceable context |
| Applicable information | Procedures, tests, notes and checklists are filtered by model, configuration revision, task/document applicability and status |
| Configuration control | Obsolete/inapplicable material is flagged; rules are visible; unsupported approvals are blocked |
| Workflow gating | Missing tests, incomplete tasks or missing evidence prevent false closure/verification |
| Historical context | Issue history is shown as a risk hint, not treated as governing technical instruction |
| Report support | Report draft carries task context and marks missing evidence or limitations visibly |

Useful reference scenarios:

- `COP-SCN-001`: APR-220 revision-D procedure mismatch
- `COP-SCN-002`: Missing post-maintenance test at closure
- `COP-SCN-003`: Hardware/software update sequence
- `COP-SCN-004`: Revision-E checklist mismatch

## Fleet & Coastal-Infrastructure Resilience Engine

A strong resilience demo should show at least one supplied scenario or an equivalent grounded exploration.

| Check | What good looks like |
|---|---|
| Scenario overlay | Scenario injects are applied as temporary overlays, not silently written into canonical data |
| Dependency reasoning | Direct and cascading impacts are distinguishable; typed dependency links are used |
| Capability explanation | Abstract capability change is explained through visible contributors, events, dependencies or spares |
| Action comparison | Actions include benefits, trade-offs, constraints and relevant evidence |
| Degraded state | Fallbacks show lower confidence, capacity, duration or new concentration risk |
| Decision support | User can understand what to protect, defer, reroute, restore or review next |

Useful reference scenarios:

- `SCN-001`: Base closure
- `SCN-002`: Sensor-chain degradation
- `SCN-003`: Critical spare shortage
- `SCN-004`: Regional communications relay disruption

# Boundary and disqualification guidance

## Automatic zero in affected category

Assign a score of 0 in the relevant category, and escalate to the technical chair, if a team:

- Uses or claims access to non-approved real, customer, classified, export-controlled or operationally sensitive data.
- Presents fictional output as a real Saab/customer operational recommendation.
- Exposes credentials, private URLs, personal data or restricted information.
- Represents a prototype as deployed, certified, standards-compliant or officially endorsed without approval.
- Builds direct control functionality for real equipment, infrastructure or operational systems.

Follow the event process in `SECURITY-AND-BOUNDARIES.md`. Judges should not discuss potentially sensitive material in public.

## Do not penalise

Do not penalise teams for:

- Using static JSON instead of a cloud database.
- Using simple rule logic instead of machine learning.
- Using a local or open model instead of a paid API.
- Choosing one scenario rather than attempting both challenge tracks.
- Explicitly declining to make a conclusion when evidence is insufficient.
- Demonstrating a modest but complete MVP rather than an ambitious incomplete platform.

# Judge scorecard

Use one scorecard per team.

| Category | Weight | Score 0–5 | Weighted score | Notes/evidence |
|---|---:|---:|---:|---|
| Operational relevance and user value | 25 |  |  |  |
| Evidence, traceability and data use | 25 |  |  |  |
| Resilience, safety and responsible AI | 20 |  |  |  |
| Prototype functionality and technical execution | 15 |  |  |  |
| User experience and communication | 15 |  |  |  |
| **Total** | **100** |  | **/100** |  |

## Tie-break order

If two teams have equal or near-equal scores, use this order:

1. Higher score for **Evidence, traceability and data use**.
2. Higher score for **Resilience, safety and responsible AI**.
3. Higher score for **Operational relevance and user value**.
4. Greater demonstrated end-to-end functionality.
5. Clearer and more usable operator/technician experience.

# Suggested demo format

To support consistent judging, use the same timebox for every team:

| Segment | Suggested duration | Expected content |
|---|---:|---|
| Problem and user | 30–45 sec | Challenge selected, user and decision/workflow |
| Live prototype | 2–3 min | Baseline/context, scenario or issue injection, evidence, result and action |
| Architecture and safeguards | 30–45 sec | Data use, logic/AI, offline/cloud posture, uncertainty/human review |
| Questions | 1–2 min | Judge clarification |

## Judge reminder

The winning prototype should make a fictional industrial user **more capable under uncertainty**. It should show its evidence, respect workflow and safety boundaries, and turn a complex dataset into a clear next action—not merely produce persuasive AI text or an attractive dashboard.
