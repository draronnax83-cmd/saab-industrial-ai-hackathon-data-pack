# Fleet & Coastal Resilience Engine — Quickstart

Build a fictional resilience dashboard, map, graph or decision-support tool for a distributed maritime support system. The goal is not a generic risk dashboard: show how an asset disruption propagates through typed dependencies, affects abstract capabilities, and changes the best available mitigation options.

## Start in 20 minutes

### 1. Use this reasoning chain

```text
Scenario inject → Asset state change → Dependency impact → Capability effect → Mitigation trade-off
```

Every recommendation should identify the asset, dependency, health event, spare record or scenario inject that supports it.

### 2. Open these files first

| File | Why it matters |
|---|---|
| `assets.json` | The fictional platforms, sensors, bases, depots, maintenance sites, communications nodes and logistics nodes |
| `dependencies.json` | Typed relationships: basing, maintenance, supply, logistics, communications, coordination and site services |
| `health-events.json` | Existing degraded conditions, maintenance demand and logistics constraints |
| `capabilities.json` | Five abstract capability indices, contributions, thresholds and baseline reasoning model |
| `scenarios.json` | Four disruption scenarios, injects, expected impacts, possible actions and evaluation anchors |

Use `spares.json` to explain lead time, reserved stock, shortages and substitute trade-offs. Use `locations.geojson` for an optional fictional Baltic-region map view.

## Recommended first scenario

Start with **SCN-004 — Regional Communications Relay Disruption**.

**Scenario**

A fictional site-services fault makes `AST-COMMS-002` / Eastgate Communications Relay unavailable for 72 hours. At the same time, `AST-COMMS-003` / Offshore Mesh Gateway is already degraded.

**Expected reasoning**

- Identify the affected communication and coordination paths, including `DEP-007`, `DEP-015`, `DEP-025`, `DEP-032` and `DEP-033`.
- Explain that `CAP-005` / Operational Coordination Continuity should decline significantly.
- Identify consequences for Eastreach sensor reporting and the surface-platform coordination path.
- Compare mitigation options: restore using `SPR-006`, use limited-duration substitute `SPR-012`, reroute priority traffic through `AST-COMMS-001`, or operate non-priority links in explicitly labelled degraded mode.
- Make the trade-off visible: moving more traffic to Northhaven raises concentration risk because its backup site-service test is overdue (`HE-007`).

## Example user query

> If Eastgate relay is unavailable for 72 hours, which assets lose their primary path, what capability is most affected, and what is the best mitigation?

A good response should cite specific data records and distinguish between **available**, **degraded**, **unavailable** and **low-confidence fallback** conditions. It should not claim that an alternate path is equivalent to full restoration.

## Minimum viable demo

Deliver these five behaviours before adding advanced AI or visual polish:

1. **Asset view** — map, graph or list showing asset status and criticality.
2. **Scenario selector** — choose one scenario and apply its injects.
3. **Dependency trace** — show first-order and, ideally, second-order affected links.
4. **Capability impact** — display affected abstract capability indices with a transparent explanation.
5. **Action comparison** — show at least two mitigation options, their benefit, trade-off and supporting records.

A strong demo flow is:

```text
Select SCN-004 → set Eastgate relay unavailable → highlight affected dependencies → show CAP-005 decline → compare SPR-006 versus SPR-012 → explain why degraded-mode labelling may be preferable for non-priority links.
```

## Additional scenarios

| Scenario | What it tests |
|---|---|
| `SCN-001` | Seven-day primary-base closure and cascading support, maintenance, spares and coordination effects |
| `SCN-002` | Sensor-chain degradation, constrained specialist maintenance and decision to defer planned maintenance |
| `SCN-003` | Critical spare allocation, reserved stock, limited-duration substitute and platform-recovery trade-offs |

## Baseline scoring guidance

`capabilities.json` contains an intentionally simple baseline model:

```text
capability index = sum(contribution weight × asset health × asset readiness × scenario modifier)
```

Clamp the result between 0.00 and 1.00. Teams may replace this model with any transparent alternative, but should retain evidence traceability and clearly state assumptions. The index is fictional and illustrative—not a real operational-performance measure.

## Data and AI guardrails

- All locations, asset relationships, scenarios, capability values and outcomes are fictional and abstract.
- Do not claim real coverage, readiness, military effectiveness or operational feasibility.
- Expose scenario assumptions and uncertainty; do not present a recommendation as certain when input data is incomplete.
- Use human-reviewable language and show the data records driving the recommendation.
- Treat AI-generated narratives as explanations of structured data, not as an authoritative decision source.

## Lovable path

1. Use local JSON/GeoJSON for the fastest UI prototype, or import the data into a team-owned Supabase project.
2. Prompt Lovable to create an asset dashboard with scenario controls, a graph/map, capability cards and an action-comparison panel.
3. Require every risk and action recommendation to show contributing asset IDs, dependency IDs, scenario IDs and spare/event IDs.
4. Complete one scenario end to end before adding chat, agent workflows, advanced graph layouts or predictive features.
