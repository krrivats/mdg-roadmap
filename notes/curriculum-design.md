# Curriculum design — why this order

## The problem with the channel
- 123 videos total; only 54 are SAP MDG.
- The single MDG playlist ("SAP MDG Technical") is ordered **newest first** — i.e. upload order reversed, not teaching order.
- So the playlist starts with "Instant rejection from parallel workitems" (a workflow edge-case) and ends with "MDG Overview for beginners".
- Verdict: the channel is a **topic library / Q&A log**, not a course. Order must be imposed externally.

## The order MDG itself imposes
SAP MDG is configured in dependency layers. You cannot do layer N before N-1:

```
1. Data Model        entity types, attributes, relationships, check tables, search helps
                     -> without this there is no field to put on a screen
2. UI (Floorplan)    OVP/UIBB assignment, layouts, field properties per CR type
                     -> needs entity types + attributes to exist
3. Process Model     CR types, BRF+ process rules, workflow steps, agents
                     -> a CR must have data + UI before it can flow
4. Validation/Deriv   BRF+ rules, BAdI (rule service), DQM
                     -> rules act on a finished CR; context comes from process model
5. Search/Dup Check   duplicate check, search methods, OVS, HANA search
                     -> operates on the completed data model
6. Replication        DRF+, key/value mapping, outbound to systems
                     -> only after governance works
```

Two consequences for study order:
- **Theory first, once.** The 91-min "Concept of Data modeling" is the single video that explains
  staging vs active area, entity types, leading entity, reuse, and why extensions exist. Every later
  video assumes it. It is placed early on purpose, even though the author uploaded it late.
- **No-code before code.** BRF+ (config) before BAdI (ABAP) before "dynamic/advanced" BAdI.
  DQM validations (no code) before any custom rule class. Otherwise you learn ABAP patterns
  without understanding the framework contract.

## Learning-path rules used
1. Concept video -> simplest hands-on on the same concept -> hardest variant.
2. Never two "advanced" videos in a row; each advanced video is followed by a small one.
3. Series keep their internal order and are never split (FPM Part 1-4, DQM Part 1-3, Field property badi 2 parts).
4. Every phase ends with a hands-on checkpoint you must be able to do alone.

## Gaps in the channel (must be covered elsewhere)
The 54 videos are strong on extension + UI + workflow + BRF+/BAdI, but they do **not** cover:
- Key Mapping / Value Mapping configuration and code
- DRF+ replication setup (outbound, replication models, filters) — only one 1:51 "visualization" video
- Data import: file upload framework, mass processing, MDG consolidation
- Data Quality Management full scope (only validations; no cleansing/BRF+ DQ rules for address)
- Analytics / MDG Analytics, change request reporting
- Authorizations (MDG-specific roles, CR-type-based authorizations)
- MDG on S/4HANA specifics (MDG 9.x, Fiori apps, Business Partner as central object)
Recommended supplements: SAP Help "SAP Master Data Governance – Configuration" guide, openSAP MDG course,
and a sandbox/IDES system — MDG cannot be learned by watching alone.
