# Team Submission Template

Complete this template before the final demo. Keep answers concise and link to evidence in the supplied synthetic data pack.

> **Data boundary reminder:** This prototype uses fictional, synthetic and non-operational hackathon data. Do not include classified, export-controlled, customer-specific, proprietary, personal or operationally sensitive information.

## 1. Team details

| Field | Response |
|---|---|
| Team name |  |
| Team members |  |
| Primary contact |  |
| Challenge track | `Operational Co-pilot` or `Fleet & Coastal-Infrastructure Resilience Engine` |
| Scenario demonstrated | Scenario ID and title |
| Prototype name |  |

## 2. One-sentence pitch

Describe your prototype in one sentence.

> Example: “A traceable maintenance co-pilot that blocks inapplicable procedures and drafts evidence-backed work reports for a fictional configuration-controlled environment.”

## 3. User and problem

| Question | Response |
|---|---|
| Who is the primary fictional user? |  |
| What decision, workflow or friction does the prototype address? |  |
| Why does this matter in the selected scenario/task? |  |
| What is the intended user action after using the prototype? |  |

## 4. Scenario and evidence

### Scenario/task context

| Field | Response |
|---|---|
| Scenario ID |  |
| Scenario/task title |  |
| Baseline state |  |
| Injected disruption, mismatch or evidence gap |  |
| Key result shown in the demo |  |

### Evidence records used

List the supplied synthetic records that materially support the prototype’s conclusion.

| Evidence type | Record IDs used | How the prototype uses them |
|---|---|---|
| Assets / platforms / systems |  |  |
| Dependencies / compartments / task links |  |  |
| Health events / issues |  |  |
| Spares / information objects / documents |  |  |
| Capabilities / configuration rules |  |  |
| Report templates / scenario injects |  |  |

## 5. Prototype workflow

Describe the end-to-end path that will be demonstrated.

1. **Context or baseline:**
2. **User input or scenario inject:**
3. **Evidence retrieval / data processing:**
4. **Reasoning, rule check or impact analysis:**
5. **Result shown to the user:**
6. **Recommended action, workflow gate or report state:**
7. **Trade-off, limitation or human-review point:**

## 6. Architecture

### Architecture summary

Describe the main components and data flow in 3–6 bullets.

- 
- 
- 

### Technology choices

| Layer | Technology / approach | Why it was chosen |
|---|---|---|
| User interface |  |  |
| Data source | Static JSON / Supabase / other |  |
| Logic / rules / graph analysis |  |  |
| AI or retrieval, if used |  |  |
| Hosting / runtime |  |  |

### Connectivity and security posture

| Question | Response |
|---|---|
| Can the prototype operate with static/local data? | Yes / No — explain |
| What happens if cloud/LLM/database access is unavailable? |  |
| How is canonical synthetic data kept separate from team edits or scenario overlays? |  |
| How are keys, tokens and credentials protected? |  |
| What data boundary safeguards are implemented? |  |

## 7. Responsible AI and resilience

| Question | Response |
|---|---|
| How does the prototype show evidence and provenance? |  |
| How does it handle missing or conflicting evidence? |  |
| How does it represent degraded state, fallback or uncertainty? |  |
| What human review or approval point is retained? |  |
| What could go wrong with the prototype, and how is that communicated? |  |

## 8. What works today

Check all that are demonstrated in the working prototype.

### Core functionality

- [ ] Uses supplied synthetic data directly
- [ ] Loads a selected scenario or task context
- [ ] Shows a baseline/normal state
- [ ] Shows a disruption, mismatch, missing-evidence case or degraded state
- [ ] Produces a visible result, warning, impact view, workflow gate or report output
- [ ] Shows source record IDs/evidence
- [ ] Shows a recommended action, next step or human-review requirement
- [ ] Shows a trade-off, limitation or uncertainty

### Co-pilot track

- [ ] Selects platform → compartment → system → task context
- [ ] Filters or retrieves applicable information objects
- [ ] Detects document/checklist applicability or configuration mismatch
- [ ] Enforces a workflow gate for missing evidence or prerequisite work
- [ ] Uses issue history as a risk hint
- [ ] Drafts a traceable report or closure record

### Resilience track

- [ ] Visualises assets and/or typed dependencies
- [ ] Applies scenario injects as temporary overlays
- [ ] Identifies direct and cascading effects
- [ ] Shows an abstract capability impact or equivalent transparent metric
- [ ] Uses health events, spares or logistics constraints in the analysis
- [ ] Compares at least two possible actions or mitigations

## 9. Demo plan

| Segment | Duration | What will be shown |
|---|---:|---|
| User/problem and scenario | 30–45 sec |  |
| Live prototype | 2–3 min |  |
| Architecture and safeguards | 30–45 sec |  |
| Backup demonstration, if live service fails |  |  |

### Demo URL and code

| Item | Link or location |
|---|---|
| Live prototype URL |  |
| Source repository URL |  |
| Demo video, if available |  |
| Presentation/slides, if used |  |
| Local/offline fallback instructions |  |

## 10. Final declaration

By submitting, the team confirms:

- [ ] The prototype uses only supplied synthetic data and approved non-sensitive additions.
- [ ] The team has not included classified, export-controlled, customer-specific, proprietary, personal or operationally sensitive information.
- [ ] The prototype does not make real-world operational, engineering, maintenance, safety or security claims.
- [ ] Key warnings, recommendations and generated outputs show evidence IDs or clearly state uncertainty.
- [ ] Credentials, API keys, private URLs and sensitive content are not exposed in the submission or demo.
- [ ] The final demo includes a fictional-data disclaimer.

**Suggested disclaimer:**

> This prototype uses fictional, synthetic and non-operational hackathon data. It demonstrates a possible workflow only and is not a validated Saab product, operational system, technical publication or decision tool.

| Field | Response |
|---|---|
| Submitted by |  |
| Submission time |  |
| Team confirmation |  |
