# Security and Data Boundaries

This document defines the security, data-governance and prototype boundaries for the Saab Industrial AI Hackathon synthetic challenge kit.

The objective is to enable ambitious prototypes while ensuring that no team needs access to classified, export-controlled, customer-specific or operationally sensitive information.

## Core rule

**Use only the supplied synthetic data and approved public or openly licensed non-sensitive material.**

If a team is unsure whether material is allowed, do not upload, paste, prompt, commit, display or discuss it in the project. Ask the hackathon technical chair or designated Saab challenge owner through the official event channel.

## Data classification

| Data category | Status | Permitted in the hackathon pack? |
|---|---|---|
| Supplied synthetic challenge data | Synthetic, non-classified, non-export-controlled | Yes |
| Team-created fictional extensions | Synthetic/non-sensitive | Yes, if clearly labelled and within this document’s boundaries |
| Public open-source maps or generic data | Public/non-sensitive | Yes, if licence-compatible and not used to infer or reconstruct sensitive context |
| Public marketing material | Public | Usually yes, but do not treat it as technical or operational ground truth |
| Personal data | Sensitive/regulated | No, unless explicitly approved by organisers and handled under a separate process |
| Customer, supplier or programme data | Proprietary/customer-specific | No |
| Real technical publications, drawings or maintenance records | Potentially proprietary/export-controlled/sensitive | No |
| Real asset readiness, deployment, maintenance, logistics or network information | Operationally sensitive | No |
| Classified or export-controlled information | Restricted | Never |

## What is intentionally fictional

All content in the challenge pack is notional, including:

- Platform, asset, system, component, compartment and module names.
- Locations, coordinates, geographic labels, site names, routes and diagram positions.
- Dependencies, network topology, support relationships and communications paths.
- Procedures, tests, safety notes, drawing descriptions, technical values, configuration rules and report templates.
- Maintenance states, health events, stock levels, lead times, substitutes, readiness values and capability indices.
- Scenario injects, impact estimates, actions, trade-offs and outcomes.

Do not attempt to map fictional records to real Saab, customer, government, military, supplier or infrastructure entities.

## Prohibited content

Do not add, use, request, infer, reproduce or disclose:

- Classified, export-controlled or security-protected information.
- Customer-specific, supplier-specific or contract-specific information.
- Non-public product, programme, configuration, interface, performance, test or vulnerability information.
- Real technical drawings, manuals, work instructions, repair records, software/firmware artefacts or configuration baselines.
- Real locations of facilities, sensors, platforms, depots, communications nodes, routes, deployment patterns or operational areas.
- Real readiness, availability, maintenance, spares, lead-time, supply-chain, workforce or mission information.
- Credentials, API keys, tokens, passwords, personal data, internal URLs or non-public system identifiers.
- Screenshots, exports or copied text from internal systems unless explicitly approved in writing through the event process.

## Approved prototype scope

Teams may build prototypes for:

- Evidence-backed information retrieval over the supplied synthetic information objects.
- Configuration applicability checks, document filtering, workflow gates and traceable report drafting.
- Synthetic dependency graphs, risk views, spares allocation comparisons and scenario exploration.
- Abstract capability-index visualisation and transparent action trade-off analysis.
- Human-in-the-loop decision support, simulation, workflow assistance and usability concepts.
- Local-first, offline or intermittent-connectivity architecture concepts.

Teams must present these as fictional demonstrations. They must not be framed as operational control, validated engineering guidance or real-world decision tools.

## AI and external-service boundaries

Third-party AI, database, hosting and development services may be used only if permitted by the hackathon organisers.

Before using an external service:

1. Confirm that inputs are limited to the approved synthetic pack and team-created non-sensitive content.
2. Do not upload internal documents, screenshots, credentials, code from restricted repositories or non-public architecture information.
3. Do not configure the prototype to call internal Saab, customer, supplier or government systems.
4. Keep API keys and secrets in platform secret management or local environment variables; never commit them to source control or expose them in screenshots.
5. Confirm the service terms and workspace-sharing settings are appropriate for hackathon use.

When using an LLM, treat generated text as unverified. The prototype must distinguish source evidence from generated explanation and must request review when required evidence is absent.

## Lovable and Supabase boundaries

For Lovable/Supabase projects:

- Use a **team-owned Supabase project** or an organiser-provided read-only synthetic-data project.
- Keep canonical synthetic seed data read-only in the application.
- Store team notes, scenario overlays, draft reports and derived scores in separate tables.
- Do not share a write-enabled canonical database between teams.
- Apply Row Level Security or equivalent access controls when exposing a shared backend.
- Use anonymous access only for approved public synthetic data; never embed sensitive credentials or service-role keys in frontend code.
- Maintain a static JSON/GeoJSON fallback so a cloud outage does not block the prototype.

## Required safety behaviours in prototypes

Every prototype should implement or visibly demonstrate these behaviours:

| Situation | Required prototype behaviour |
|---|---|
| Evidence is complete and applicable | Show evidence IDs and a bounded recommendation or next workflow action |
| Evidence is missing | Show **“Insufficient data — request human review”** |
| A document/checklist is obsolete or inapplicable | Show a warning/block and identify the applicable record or review step |
| A required test or task is incomplete | Block closure or return-to-service state; identify the missing prerequisite |
| A scenario uses degraded fallback | Show reduced confidence, capacity, duration or other limitation |
| An LLM produces a summary | Show source records separately; do not treat generated prose as evidence |
| A user asks for a real-world recommendation | Explain that the prototype uses fictional data and cannot provide real operational advice |

## No control implementation

Do not build or demonstrate:

- Direct control of physical equipment, sensors, vehicles, platforms, infrastructure or industrial systems.
- Automated safety-critical, mission-critical or security-critical decisions.
- Commands that could be connected to a real actuator, C2 system, industrial controller, operational network or facility system.
- Interfaces that appear to issue real orders, deployments, configuration changes or maintenance releases.

A prototype may simulate a decision, proposed action, workflow state or scenario overlay. It must make clear that human review and external approval are required.

## Public demonstration rules

In every final demo, slide deck, video, repository and public post:

- State that the prototype uses fictional, synthetic and non-operational data.
- Avoid real platform, location, customer, configuration, capability or readiness claims.
- Do not show API keys, credentials, private repository URLs or non-public conversations.
- Do not claim endorsement, deployment, product status, validated performance or standards compliance without written approval.
- Use this disclaimer or equivalent:

> This prototype uses fictional, synthetic and non-operational hackathon data. It demonstrates a possible workflow only and is not a validated Saab product, operational system, technical publication or decision tool.

## Incident and escalation process

Stop work and contact the designated event contact immediately if:

- A team member believes that sensitive, non-synthetic or restricted information has been introduced.
- A prompt, repository, database, attachment or screen includes internal, customer or operational content.
- A team discovers a data item that appears to resemble a real asset, location, procedure or operational pattern.
- A credential, secret or token is exposed.
- A prototype is accidentally connected to a real system or service.

### Immediate steps

1. Stop sharing the material.
2. Do not copy it into another tool, prompt, repository, chat or presentation.
3. Restrict access or take the affected prototype/repository offline if possible.
4. Notify the technical chair or Saab challenge owner through the approved private escalation channel.
5. Follow organiser instructions for removal, rotation, deletion or documentation.

Do not report potential sensitive content in a public Slack/Teams channel, public GitHub issue or public social-media post.

## Final pre-submission check

Before submitting, each team should confirm:

- [ ] The prototype uses only supplied synthetic data and approved non-sensitive additions.
- [ ] No credential, personal data, internal URL, customer name or restricted content is committed or displayed.
- [ ] All key recommendations, warnings and generated reports show evidence IDs or explicitly state uncertainty.
- [ ] The prototype does not make real-world operational, engineering, safety or security claims.
- [ ] The final demo includes the fictional-data disclaimer.
- [ ] Team-owned cloud resources are configured so other teams cannot modify their data.
- [ ] The prototype can fall back to static/local data if a cloud service is unavailable.

## Contact

For a boundary question or incident, use the official event support channel and request a private escalation to the hackathon technical chair or designated Saab challenge owner. Do not include potentially sensitive information in the initial public message.
