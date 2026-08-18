# Saab Industrial AI Hackathon — Challenge Kit

Welcome to the Saab synthetic challenge environment for a 10-hour Industrial AI Hackathon sprint. This kit provides a safe, fictional and developer-friendly operational world for building prototypes around lifecycle support, configuration control and resilience decision support.

## Start here

### 1. What are the two challenges?

| Challenge | Build focus |
|---|---|
| **1. Operational Co-pilot for Naval Production & Support** | Build a web or tablet co-pilot that helps a user select a fictional platform, location, system and task; retrieve applicable procedures and safety information; identify simple configuration/revision conflicts; and draft a work or inspection report. |
| **2. Fleet & Coastal-Infrastructure Resilience Engine** | Build a dashboard, graph, map or decision-support experience that explores a fictional network of assets, support dependencies, health events, spares and disruption scenarios; visualises impact; and proposes transparent resilience actions. |

Choose one challenge, or combine them only if the team can still demonstrate a clear, working end-to-end workflow.

### 2. What must teams deliver?

By the end of the sprint, submit:

- A **working web or tablet prototype**.
- A brief **pitch/demo** showing a normal workflow and at least one disruption, conflict or degraded-state case.
- A short **architecture sketch** showing data flow, AI/logic components, user interaction, and a plausible approach to intermittent connectivity and security constraints.
- A concise explanation of the system’s assumptions, evidence sources and limitations.

For the resilience challenge, recommendations must identify the contributing asset IDs, dependency paths, scenario injects or spare records. For the co-pilot challenge, answers and warnings must show the source record IDs, applicable revision/effectivity and rule or document evidence.

### 3. How do teams run the kit?

The target experience is **copy-paste commands only**.

```bash
# Clone or download the challenge repository
git clone <REPOSITORY_URL>
cd saab-industrial-ai-hackathon

# Inspect the available packs
ls data/ docs/

# Optional: launch the supplied starter environment
make demo
```

If using Lovable and Supabase, import the provided schema and seed data, then connect your Lovable project to your own Supabase project. Teams may also use the JSON/CSV files directly in any local, web, graph or AI stack.

No paid model, external API or cloud service is required for a valid prototype. Cloud services are optional enhancements; the core workflow must remain demonstrable with the supplied synthetic data.

### 4. What is intentionally synthetic and simplified?

**Every platform, component, location, dependency, document, event, spare, performance value, capability index and scenario in this kit is notional.** Names, coordinates, relationships, statuses, technical values and operational effects are invented for prototype development.

The kit is deliberately small. It models selected relationships and scenario logic—not a real fleet, production environment, support system, technical publication set, maintenance programme, logistics network or command-and-control architecture. Abstract capability indices are demonstration aids, not operational measures.

Do not infer real information from the data. Do not enrich it with customer, programme, platform, personnel, geographic, readiness, technical-publication or operational information that is not explicitly approved for public hackathon use.

### 5. What are the boundaries?

- **No classified, export-controlled, customer-specific or operationally sensitive data.**
- **No safety-critical control implementation.** Prototypes may provide decision support, visualisation, simulation or workflow assistance only.
- **No real-world operational recommendations.** Treat outputs as fictional, human-reviewable demonstrations.
- **No standards conformance claim.** The data profile may be informed by lifecycle-support and logistics-product-data concepts, but it is not an implementation or conformance demonstration of S3000L, SAE GEIA-STD-0007 or any other standard.
- **No invented certainty.** When the data does not support an answer, show the uncertainty and recommend review rather than fabricating a result.

## Data packs

```text
data/
├── copilot/                 # Operational co-pilot pack
│   ├── systems.json
│   ├── tasks.json
│   ├── information-objects.json
│   ├── configuration-rules.json
│   ├── issue-history.json
│   ├── report-templates.json
│   └── scenarios.json
│
└── resilience/              # Fleet/coastal resilience pack
    ├── assets.json
    ├── dependencies.json
    ├── health-events.json
    ├── spares.json
    ├── capabilities.json
    ├── locations.geojson
    └── scenarios.json
```

The resilience pack is designed for four shared exercises: base closure, sensor-chain degradation, critical-spare shortage and regional relay disruption. Each scenario includes fictional injects, expected impact anchors, possible actions, trade-offs and evidence records to support transparent reasoning.

## Build principles

Prioritise a useful operator workflow over feature count:

1. Start from a clear user question or operational decision.
2. Show the relevant data and evidence, not only an AI-generated conclusion.
3. Make uncertainty, degraded mode and human review visible.
4. Show one complete demo path before adding advanced functionality.
5. Keep all new data and generated content within the challenge boundaries above.

## Help and submission

Use the event support channel for setup questions and report data defects with the relevant file name and record ID. In the final demo, show: **context → evidence → reasoning/logic → recommended action → trade-off or limitation**.
