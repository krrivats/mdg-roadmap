# SAP MDG - Study Roadmap

**Channel:** Koushik Konda ([@koushikkonda1994](https://www.youtube.com/@koushikkonda1994))
**Scope:** 54 SAP MDG videos · **25h14m** of video · notes built from the transcripts of all 54
**Goal:** MDG consultant, configuration hands-on
**Generated:** from the channel's live video list; every note below comes from the spoken content, not from the titles.

---

## Why you could not figure out the order

The channel has **123 videos, and only 54 are SAP MDG** - the rest is C programming, HTML, NX CAD and Rubik's cube tutorials, all mixed into the same upload feed. The single MDG playlist ("SAP MDG Technical") is sorted **newest first**, so it opens with *"Instant rejection from parallel workitems"* - a workflow edge case - and ends with *"MDG Overview for beginners"*.

It is a topic library, not a course. Nothing is numbered, series are uploaded out of order (Part 4 before Part 1), and two titles are actively misleading (see caveats at the end). So the order below is **designed from MDG's own dependency chain**, not copied from the channel.

## How to use this roadmap

1. **Follow the phase order.** Within a phase, follow the numbering. Skipping ahead is what makes MDG feel random.
2. **Watch at 1.25x, but pause and do it in the system.** MDG cannot be learned by watching - every video is a screen recording of configuration.
3. **After each video, write 3 lines in your own words.** If you cannot, rewatch that part.
4. **After each phase, do the checkpoint without the video.** That is the real test.
5. Any video over 40 minutes: split into 2-3 sittings. They are sequential, not modular.

## Start here - tonight (41 minutes)

Do not plan. Just watch these three in this order, they are short and they set up everything else:

1. [MDG Overview for beginners](https://youtu.be/-WjWaGdmuCY) - 6m
2. [MDG High Level visualization in integration](https://youtu.be/_z3U_uaZ9W4) - 2m
3. [Adding MDG Apps to NWBC](https://youtu.be/L9nSSBmOhgA) - 12m
4. [SAP MDG BP Number ranges and CVI config basics](https://youtu.be/c4IXaHVKfuY) - 21m

Then stop. Tomorrow you start Phase 1 with the 91-minute data modeling video - and it is the one video in this list you should watch twice.

## At a glance

| Phase | Videos | Time | After this phase you can |
|---|---|---|---|
| Phase 0 - Orientation | 4 | 0h41m | Know what MDG is, log in to a CR screen, explain BP vs customer/vendor |
| Phase 1 - Data Modeling | 8 | 5h54m | Extend BP / customer / material, add a custom entity, drive field properties by table |
| Phase 2 - UI / Floorplan | 14 | 4h40m | Change any MDG screen, hide/adapt by role and CR type, build a form UIBB |
| Phase 3 - Process Modeling / Workflow | 11 | 6h39m | Build a CR type end-to-end, design a multi-level workflow, handle requester/approver edge cases |
| Phase 4 - Validations / Derivations | 13 | 5h54m | Write validations/derivations in BRF+, BAdI and DQM, and know when to use which |
| Phase 5 - Search / Duplicate Check | 4 | 1h24m | Configure duplicate check and search (OVS, HANA search, defaulting methods) |
| **Total** | **54** | **25h14m** | |

**Three schedules - pick one**

| Plan | Pace | How it maps |
|---|---|---|
| **Sprint** | ~2h/day, 13 days | P0 day 1 · P1 days 2-4 · P2 days 5-7 · P3 days 8-10 · P4 days 11-12 · P5 day 13. Only works if you have a sandbox system. |
| **Standard** (recommended) | ~1h/day, 5 weeks | One phase per week; P1 and P4 take a full week each. Leaves time to actually configure. |
| **Weekend** | 2 weekends, ~6h/day | Weekend 1: P0+P1+P2 · Weekend 2: P3+P4+P5. Do the checkpoints on weekday evenings. |

---

## Phase 0 - Orientation and environment

**4 videos · 0h41m**

Goal: know what MDG is, where you actually work, and how BP relates to customer/vendor. Nothing here is hard - do not skip it, because every later video assumes these four facts.


### 1. MDG Overview for beginners
**ID:** [-WjWaGdmuCY](https://youtu.be/-WjWaGdmuCY) | **Length:** 6m | **Level:** beginner

**In one line:** Why duplicate master data breaks a business and what SAP MDG plus the Reference Solution Architecture actually are — concepts only, no system demo.
- Problem framing: same customer entered as "J. Smith" (sales) and "John Smith, Suite X" (finance) = two different records to the system → billing errors, wrong shipments, wrong reports, bad decisions; ownership of "the customer list" is contested between sales and finance.
- MDG defined as the referee over customers, suppliers, products: one golden record, single point of control, tools to clean existing records, rules to keep new ones accurate.
- **Reference Solution Architecture** — a framework (explicitly *not* software to buy) of best practices, diagrams and guides covering planning → testing → go-live; resources are published on the **SAP Business Accelerator Hub**.
- Two deployment/strategy models: **centrally managed** (one MDG system is king of all master data) vs **federated** (central system governs the core, e.g. customer name; local units own their specifics, e.g. regional shipping details).
- Four artifact types used to document the design: **value flow** (business view, the "what/why"), **component diagram** (systems and how they connect, the "how"), **data flow** (where data is born/travels), **process flow** (one task step by step, who approves, what is automatic).
**Key insight:** The video's whole thesis is that installing MDG is not the deliverable — the reference architecture is, because it puts business and IT on one visible roadmap and makes the build extensible. Nothing here is configurable in the system; it is the "why" you use to justify the project.
**Prereq:** none (entry point of the whole playlist)

---

### 2. MDG High Level visualization in integration
**ID:** [_z3U_uaZ9W4](https://youtu.be/_z3U_uaZ9W4) | **Length:** 1m51s | **Level:** beginner

**In one line:** NO TRANSCRIPT - title-based only.
- Short (1m51s) clip, no captions available on the channel: by title it is a high-level visual overview of MDG integration with the target/ERP system (data flow MDG -> CVI -> customer/vendor), not a step-by-step config video.
**Key insight:** Nothing extractable beyond the title; do not treat as configuration guidance.
**Prereq:** none

### 3. Adding MDG Apps to NWBC
**ID:** [L9nSSBmOhgA](https://youtu.be/L9nSSBmOhgA) | **Length:** 12m | **Level:** beginner

**In one line:** How to expose any transaction, report, WebDynpro/FPM application (or BSP/Fiori app) as a tab in NWBC through the role menu, for users who only have the NWBC URL and no SAP GUI.
- Business driver: client has access only to the NWBC link, not SAP GUI, so custom reports/Z transactions must surface inside NWBC. The combined **NWBC** node at the top of the NWBC launchpad merges all roles below it (Material Governance, Analysis of Change Request Process, Business Partner Governance, …).
- Find your roles: **SU01** → enter/display user ID (get the ID from **System → Status**), display mode → list of roles; work only on `Z*` custom roles because SAP standard roles must not be touched (example role `Z_MDG_...` had users assigned but an **empty Menu**).
- Transaction as a tab: role → **Menu** → change mode → **Create folder** (the folder name *becomes* the NWBC tab title) → inside the folder add node type **Transaction** → T-code `BP` → Save → refresh NWBC; the new tab appears at the **end** (custom roles render last).
- Report as a tab: new folder ("Report for IDoc") → node type **Report** → program `RBDMIDOC` (message-type IDoc report) → variant optional → Save; note the "Execute" button sits bottom-right in the portal vs top-left in SAP GUI, but behaves the same.
- MDG-specific case — WebDynpro application as a tab: new folder "My customer application" → in the WebDynpro configuration browser search **Adaptable OVP** under *Web Dynpro applications* → application **BS_OVP_BP** (application configuration for customer = **BS_OVP_CU**) → node type **WebDynpro application**, application `BS_OVP_BP`, configuration `BS_OVP_CU` → Save → tab opens the SE customer search and lets you create an organization customer.
- Other node types that also work: **BSP application** (Business Server Pages — old CRM-on-ECC technology), **SAP Fiori catalog / Fiori group**, and other launchpad-style application types.
**Key insight:** One application, many behaviours: the tab is built from WebDynpro application `BS_OVP_BP` for *all* objects, and it only becomes "customer" because application configuration `BS_OVP_CU` is supplied. Remember the pairing **BS_OVP_BP + BS_OVP_CU = customer**; the identical mechanism gives you BP/supplier/MM tabs. Also remember folder name = visible tab name.
**Prereq:** none technically, but pairs with *MDG UI OVP Component Overview* (that video explains what `BS_OVP_BP` / `BS_OVP_CU` really are inside).

---

### 4. SAP MDG BP Number ranges and CVI config basics
**ID:** [c4IXaHVKfuY](https://youtu.be/c4IXaHVKfuY) | **Length:** 21m | **Level:** beginner

**In one line:** End-to-end minimum setup to get a BP grouping to also create an ERP customer: groupings, number ranges, account groups and the CVI BP-to-customer number assignment.
- Architecture: XD01/XK01 are obsolete in S/4 and route to BP; `BUT000` is master data, `CVI_CUST_LINK` links BP<->customer, `CVI_VEND_LINK` links BP<->vendor (mapping via `PARTNER_GUID`).
- Groupings: `BUT000-BU_GROUP` (field BU_GROUP in BP tcode) decides which number range the BP gets. SPRO -> Cross-Application Components -> SAP Business Partner -> Business Partner and Basic Settings -> Number Ranges and Groupings -> **Define Groupings and Assign Number Ranges**. Demo: grouping B001 = external, assigned to number range B1 with interval ~541000–600000; entering a number outside gives "number not in interval".
- Customer side: SPRO -> Logistics – General -> Business Partner -> Customers -> Control -> **Define account groups and field selection for customers** — account groups 000001 / ZB; ZB is internally numbered so the customer number is generated automatically.
- The missing link: SPRO -> Cross-Application Components -> Master Data Synchronization -> Customer/Vendor Integration -> Business Partner Settings -> Settings for Customer Integration -> **Define Number Assignment for Direction BP to Customer**; add BP grouping B001 -> customer account group ZB. Before this, the ERP Customer "New" button is disabled with "CVI customizing does not allow creation of customer for business partner grouping B001".
- After activation: check BP in BUPA (BP 545...) and customer in FD03/KNA1-style display; verify the link in table `CVI_CUST_LINK` by pasting `PARTNER_GUID` from BUT000 — that GUID lookup is exactly how MDG resolves the customer number for display.
**Key insight:** The ERP customer is created only at final activation, never at first-level approval — an empty ERP Customer field after approval is normal, not a bug. And both number-range layers must be consistent: BP external range for the grouping, customer internal range for the account group.
**Prereq:** none (this is the foundational CVI/BP-numbering video).

**Checkpoint:** create one BP grouping (external, number range) and one customer account group (internal), wire CVI number assignment, create a BP and find its customer in `CVI_CUST_LINK`. If you can explain BUT000 vs KNA1 vs CVI_CUST_LINK out loud, Phase 0 is done.

---


## Phase 1 - Data Modeling (the backbone)

**8 videos · 5h54m**

This is the phase that decides whether the rest makes sense. Order inside the phase is strict: theory -> simplest custom attribute -> the Field Property BAdI -> the same pattern on other objects -> custom entity (type 4) -> the 95-minute reuse-mode build last.

Two warnings from the transcripts: the 91-minute theory video ends at "visualize the data model" - it does **not** cover UI or process modeling. And the two Field Property videos are mislabelled: `N0ddqPBlIwg` ("Implementation") is the prerequisite, `HX1CXqzRODI` ("Using custom table") builds on it.


### 1. Concept of Data modeling (Theory + Practice)
**ID:** [0_Zh5l8cRko](https://youtu.be/0_Zh5l8cRko) | **Length:** 91m | **Level:** intermediate

**In one line:** The end-to-end theory of MDG data modeling (entity types, relationships, hierarchies, editions, key assignment, text, attachments, sets, active area) followed by a hands-on Bank → Account → Address data model built from scratch.
- Data modeling = creating the model that represents how data is stored/processed/accessed, and it **creates the staging area** (temporary tables holding change-request data). Navigation: `MDGIMG` > General Settings > Data Modeling (create/edit data model); the generated tables are inspected with the **MDG data model** transaction (open the model, e.g. `Z4`, and drill into "generated database tables" / "check table").
- Entity type = a field or group of fields with common storage/use-type/time-dependency; its fields live under the **Attributes** tab. Storage & Use Type (SU type) dropdown is identical for every data model, standard or custom.
- **Type 1** ("changeable via change request, generated database tables"): data element optional (if omitted you must maintain attributes inline); only type 1 can be attached to a change request type in Process Modeling; on activation (`check generating database tables`) it produces a real check table.
- **Type 2** ("changeable without change request, generated check/text tables"): data element mandatory; generates tables at MDG level; **attributes are not allowed** — error "attribute should not be assigned to type two entity" (same for type 3; long text says attributes can only be assigned to SU types 1 and 4).
- **Type 3** ("not changeable via MDG, no generated database tables"): data element mandatory, no attributes, nothing generated even after activation; used purely as a key/qualifier entity; you can create but not change its data in MDG.
- **Type 4** ("changeable via other entity type, generated database tables"): data element **must be blank** (error "data elements cannot be specified for this storage and use type"); needs at least one attribute; cannot exist standalone — must hang off a type 1 (or type 4) via a **leading relationship**, and only then does the model activate and generate its table (demo: Z4 ends with 3 tables — type 1, type 2, type 4; type 3 produces none).
- **Relationships**: leading (bank → bank account; no account without a bank), qualifying (adds a **key** field, from type 3 or type 2 to type 4, cardinality must be 1:n — with 1:1 the system does not even prompt for the qualifying relationship), referencing (adds a **non-key** field, reusable across type 3/type 2 to type 4), foreign key (like referencing but field-by-field, type 1→type 4 or type 4→type 4).
- **Hierarchies**: parent-child node structures (cost center groups, BP/customer hierarchies); type = **synchronized** (all sibling nodes must carry the identical sub-structure, system validates) or **version dependent** (same structure visible in different versions/perspectives, e.g. employee vs manager vs client view); options for hierarchy validation and hierarchy time dependency sit separately from entity time dependency.
- **Time dependency / editions** ("addition" = validity): used for finance objects (cost center, GL account, profit center) with financial-year validity; user must fill valid-from. Activation check: if a parent entity has edition, every dependent type 4 entity must **also** have edition on — MDG verifies this at activation.
- **Key assignment**, 4 options: (1) no internal key assignment, key cannot be changed (greyed after first entry); (2) internal key assignment only (field empty/greyed, MDG allocates dynamically); (3) key changeable, no internal assignment; (4) key changeable **and** internal assignment possible (leave blank → system numbers it).
- **Text generation**: only type 1 and type 2; checkbox "key / language dependent text" plus Short/Medium/Long text lengths → on activation an extra text table appears (fields `TXTSH`, `TXTM`, `TXTMI`/`TXTLG` style) and the `LANGUAGE` key is added when language-dependent, so each record can hold descriptions in several languages; **Visualize** shows the resulting structure without activating.
- **Attachments** (type 1 only): one checkbox adds two extra tables (file type, file size) so files can be attached at entity level, not at change-request level. **Sets** (type 1 only): an entity that groups other entities; SAP's own example is "breakdown category set" in Financial Consolidation in NWBC (create set, define from/to ranges); a set also overrides the check table like a search help.
- **Source field short text**: for fields whose check table has no text table (e.g. `BUKRS`, company code, description field `BUTXT`), enter the description field in the short/medium/long text columns so F4 shows text. **Temporary keys**: choosing internal key assignment demands a **number range object** (else "missing number range object").
- **Active area**: on final check/approval staging data is written to the active area; only relevant in **reuse** data models, not flex. **Deletion** flag controls whether a record may be deleted at all. **Description** is configuration-only (shows at CR step / entity / attribute level when configuring). **Structure / table / field / X-field** are used by SMT mapping; the `X` structure flags "field changed" in change scenarios. Attribute level offers currency and unit-of-measure reference fields.
- Hands-on build (second half): SE11 tables `ZT_BANK` / `ZT_BANK_ACCOUNTS` as the target picture; entity **Bank** (type 1, data element for BANK_ID, attributes country `BANKS`, bank name, branch), entity **B_ACCOUNT** (type 4, first/last name, account type `CHAR30`, government ID `NUMC15`), leading relationship Bank→B_ACCOUNT 1:n; type 3 entity **ACC_N** (account number `NUMC15`) with a qualifying 1:n relationship into B_ACCOUNT so the account number becomes a key; entity **ADR_DATA** (type 4: street, postal code, country, region, house number, street2, landmark, building) and type 2 **ADR_TYP** with text table; qualifying ADR_TYP→ADR_DATA 1:n and leading B_ACC→ADR_DATA 1:n.
- Practical traps seen live: giving every address attribute a **different data element** (identical data elements cause mismatches at data-transfer level) and the activation error "attribute country is assigned more than once" after reusing country in ADR_DATA — remove the duplicate, then activate and inspect the generated tables / visualized model.

**Chapter-ish flow:** 1) why data modeling matters + slides → 2) MDGIMG navigation, existing models, entity types & attributes → 3) Storage & Use Type 1 demo (new model Z4, prefix `ZMDG`, package, activate, generated table) → 4) type 2 restrictions → 5) type 3, no tables → 6) type 4 + leading relationship → 7) relationship kinds (leading/qualifying/referencing/foreign key) → 8) hierarchies (synchronized vs version dependent, validation) → 9) time dependency / editions → 10) key assignment (4 options) → 11) text generation (short/medium/long, language dependent) → 12) attachments → 13) sets (FIN consolidation example) → 14) source field short text, temporary keys/number ranges → 15) active area, deletion, description, structure/table/field/X-field → 16) currency & unit of measure attributes → 17) full build: Bank / Account / Address data model.

**Key insight:** The SU type dictates everything downstream — only type 1 can go into a change request, types 2 and 3 reject attributes, type 3 never generates a table, and type 4 is dead weight until a leading relationship from a type 1 entity exists. Get the relationship right (and give each attribute its own data element) before activating, because activation is where MDG enforces all of it.
**Prereq:** none — this is the backbone; do it before any extension, field-property BAdI or UI modeling video.

### 2. Data model extension in SAP MDG Business partner
**ID:** [45nxZNTE4HY](https://youtu.be/45nxZNTE4HY) | **Length:** 28m | **Level:** intermediate

**NO TRANSCRIPT - title-based only**
**In one line:** Overview-level video on adding a custom element to the MDG-BP data model (the generic "data model extension" concept; no captions captured, so no verified steps).
- No transcript available for this ID (auto-captions missing), so no object names, transactions or paths are claimed here.
- For the concrete mechanics of this topic, use the two verified blocks above: `-jKrMych1yc` (staging-level type-4 entity, form UIBB, GenIL + wiring) and `AOShQLm_f6I` (entity + custom table + handler class persistence).
**Key insight:** unverified — treat this video as a concept overview only; do not cite specifics from it.
**Prereq:** none verified.

### 3. Field property badi - Implementation
**ID:** [N0ddqPBlIwg](https://youtu.be/N0ddqPBlIwg) | **Length:** 22m | **Level:** advanced

**In one line:** First, code-only walkthrough of the field-property BAdI: makes salutation read-only/hidden/mandatory per change-request type using the standard BAdI and explains why the naive version must be filtered in code.
- Two pre-checks that decide whether the BAdI works at all: `MDGIMG` > Process Modeling > **Define Governance Scope** — the entity (BP Central) and every attribute must be *Governed*, otherwise field properties are ignored; and `MDGIMG` > Change Request > **Configure Properties of Change Request** > change-request tab — field properties at initiation must be **Standard** ("Not relevant / No required field check" variants break it).
- BAdI location: MDGIMG > Change Request > Business Add-Ins > BAdI for **customer-dependent field property settings** → enhancement implementation `ZMDG_FLD_PROP_BP`, class `ZMDG_FLD_PROP_BP`; filter values created as a combination on **model = BP** only (comparator EQ), i.e. it must at least fire for the BP data model.
- Method `MODIFY_FIELD_PROPERTY_ATTRIBUTE` already receives model, change request, CR type, status and the field-property table — no need to import the static MDG classes; the parameter table is `CT_FLD_PROP`, each line a structure with nested `USMD_FP`.
- Find the attribute: MDGIMG > Edit Data Model > BP > **Visualize** (BP Central, salutation = `TITLE_LET`); in the debugger the line shows the nested structure components (`USMD_FP`, then the attribute name) — he screenshots the debugger to get exact names.
- Code: `LOOP AT ct_fld_prop ASSIGNING <ls_fld_prop>`, `ASSIGN COMPONENT 'USMD_FP' OF STRUCTURE <ls_fld_prop> TO <ls_usmd_fp>`, `IF <ls_usmd_fp> IS ASSIGNED`, `ASSIGN COMPONENT 'TITLE_LET' OF STRUCTURE <ls_usmd_fp> TO <lv_title_let_fp>`, then set the property: `'M'` = mandatory (star appears), `'R'` = read only, `'H'` = hidden (field vanishes), `'C'` = changeable.
- Drawback demonstrated: without a CR-type condition the code fires for **every** CR type (another CR type also showed salutation read-only). Fix = `IF iv_crequest_type = 'ZCUST1P3'` **inside** the method — filtering in the BAdI filter instead would stop the whole BAdI from firing for other CR types.
- He closes by saying the `ASSIGN COMPONENT` chain grows unmanageable on real projects ("sophisticated", too lengthy) and points to the custom-table approach in the next video.

**Key insight:** Field-property BAdI only changes the *appearance/behaviour* of the field — a mandatory setting gives the asterisk but **no validation is triggered** by the BAdI, so real checks still need validation/BRFplus. And never restrict CR types via the BAdI filter; restrict them in code.
**Prereq:** Data modeling (entities/attributes, Visualize), governance scope & CR property configuration basics.

### 4. Field property badi - Using custom table
**ID:** [HX1CXqzRODI](https://youtu.be/HX1CXqzRODI) | **Length:** 37m | **Level:** advanced

**In one line:** Turns dynamic field properties into table-driven configuration: a custom Z table holds CR type / step / entity / attribute / field-property rows, and one small BAdI method loops that table instead of hard-coding `ASSIGN COMPONENT` chains.
- SE11: create table `ZMDG_FLD_PROP`, delivery class C (customizing), data class master data, size category 0; **every field is a key** so several rows can exist per CR type/step — fields CR type (`USMD_CREQUEST_TYPE`), step (`USMD_*` change-request step, "change request step used in rule-based workflow"), entity (`USMD_ENTITY`), attribute, and field property (`USMD_FLD_PROP` domain). Cross-client would need MANDT; he deliberately leaves the table client-dependent.
- Watch the data element: he first picked `USMD_FLD_PROP` for the property column and got "inconsistency in length of ddic data type" / could not enter values; checking the domain's fixed values showed the four usable entries (required, hidden, read-only, changeable) and he corrected the field to the proper data element.
- Table maintenance: Utilities > Table Maintenance Generator, one-step, function group + authorization group `&CR`, so entries can be maintained in `SM30` (`ZMDG_FLD_PROP`) without a transport each time.
- BAdI: MDGIMG > Change Request > Business Add-Ins > the last one, **field-property settings for customer-dependent field properties** → implementation `ZMDG_FLD_PROP` / enhancement `ZMDG_FLD_PROP_BP`, class `ZMDG_FLD_PROP`, method `MODIFY_FIELD_PROPERTY_ATTRIBUTE`.
- Method body: `SELECT * FROM zmdg_fld_prop INTO TABLE lt_fld_prop WHERE cr_type = iv_crequest_type AND step = iv_fld_workflow_step AND entity = iv_entity` (he starts with only CR type + step because those never change during a step, then adds entity; attribute filtering is not needed since it is read per line). Then `LOOP AT lt_fld_prop`, inner `LOOP AT ct_fld_prop ASSIGNING <ls_fld_prop>`, `ASSIGN COMPONENT 'USMD_FP' OF STRUCTURE <ls_fld_prop> TO <ls_usmd_fp>`, then `ASSIGN COMPONENT 'ATTRIBUTE' OF STRUCTURE <ls_usmd_fp> TO <ls_attribute_fp>`, and if assigned `<ls_attribute_fp> = ls_fld-fld_prop`.
- Live test on CR type `ZCUST1P3`: entity `BP_..._CNTRL`, attribute for salutation → hidden, then changed to required in SM30 (salutation shows the asterisk), then read-only (field greyed); then entity for address postal data, attribute region (`REFPOSTA_*`) required → country becomes mandatory; then `LANGU_*` hidden → the language field disappears from the UI entirely. Opening the same customer under a different CR type shows everything back to standard, proving the CR-type filter works.
- Performance refactor: move the `SELECT` into the class **CONSTRUCTOR** and store it in a public instance attribute `GT_FLD_PROP TYPE TABLE OF zmdg_fld_prop`, so the DB read happens once per class instance lifetime; the modify method then only loops the cached table with the three WHERE conditions.

**Key insight:** Field-property settings are per CR type + step + entity + attribute, so the table must be fully keyed and the BAdI must filter on all three dimensions — and because `MODIFY_FIELD_PROPERTY_ATTRIBUTE` fires for every field on every screen build, always cache the table in the constructor or the UI slows to a crawl once the table grows.
**Prereq:** "Field property badi - Implementation" (BAdI creation, method, filter) and the data-modeling video for entity/attribute technical names.

### 5. Data model extension with custom attribute at Customer General Data
**ID:** [iC84jBUj3fc](https://youtu.be/iC84jBUj3fc) | **Length:** 27m | **Level:** advanced

**In one line:** Same extension pattern as material but for customer General Data in the BP model — checks for a CI_ include, appends to the SAP-provided include in KNA1 plus its `_X` twin, then wires the attribute through the BP data model, SMT/STG mappings and the customer UI.
- SE11 `KNA1`: first check whether SAP shipped a CI_ custom include (none here), then use the **SAP-provided extensible include** inside KNA1 and create append structure `ZZ_AP_APPEND_CUSTOM_FIELD`-style with data element `ZSTRATEGY` (ROUTING_STRATEGY, `CHAR20`, with field labels); set the **enhancement category** ("can be enhanced – character-like or numeric") on the append to match the underlying include before activating.
- Second append structure with the `_X` suffix on the **same include** (component type = flag/update type) — this is what tells the system, in change/change-finder scenarios at database level, that the field changed; its description says "custom fields in KNA1 for change finder scenarios".
- MDGIMG > Edit Data Model > **BP** > customer entity (the entity behind Customer General Data) > add attribute `ROUTING_STRATEGY` with the same data element, and tick **Change Document** relevance on the attribute's characteristics; save and activate the data model.
- Activation produced the warning to **adjust the change request / staging area** → confirm, staging area is regenerated; then Data Model Specific Structures > Business Partner > select all related entities > **Generate** so the structures are rebuilt.
- UI: NWBC Organization > New customer > right-click > Technical Help > Component Configuration > Other Functions > **Create Customizing** (new customizing for the customer screen), then drag the new field under "Additional Data / Attribute 10", save.
- SMT mappings: read the mapping name from the generated BP data-model-specific structures, open the same SMT mapping > Details > Transformations > Add field mapping `ROUTING_STRATEGY` ↔ `ROUTING_STRATEGY` with package `ZMDG`; repeat for the **`_X` mapping** and for the staging→staging ("STA") mapping even though stage-to-stage already works (common practice).
- Save trap: the mapping must go into a **local workbench request created in SE10** with the default **target system removed** in the mapping's properties — with a target system filled it refuses to save.
- Test: create customer with routing strategy, submit, approve; check the field in the change request, in `KNA1` via SE16 in both active and staging area.

**Key insight:** For KNA1 there is no CI_ include, so the only hook is the SAP-delivered extensible include — and you must append **both** the data structure and its `_X` counterpart, then add the attribute to the BP data model with Change Document ticked, or the value never reaches the active area.
**Prereq:** Data modeling (BP entity/attribute, activate + generate structures), the material extension video (same 6-structure/mapping logic), UI customizing basics.

### 6. Material data model extension with custom attribute
**ID:** [_aPCLXVHhAs](https://youtu.be/_aPCLXVHhAs) | **Length:** 22m | **Level:** advanced

**In one line:** Full stack for adding one custom field (`ZZ_EXT_NUM`) to the material UI in the reuse MM model so it survives into MARA — dictionary, transfer/UI structures, field selection, data model, SMT + PP mappings, UI, and proof in MM03/SE16.
- SE11: append to **IMARA** (not MARA directly) — `ZCUSTOM_EMARA`, component `ZZ_EXT_NUM` type `NUMC5`; because IMARA is included in MARA, the field lands in MARA and in everything else that includes IMARA.
- The CMD transfer structures for material: extend the three `CMD_*MARA` structures (normal transfer structure, plus UI and X variants) and the `MDG_*MARA_X`-style structures; the normal one fills automatically through the IMARA include, but the **X** (change-flag, `XFELD`) and **UI** (component type `MDG_BS_FIELD_STATE`) structures must be appended manually, otherwise existing-material changes break or the field is not flagged as changed.
- Field selection: SPRO > Logistics – General > Material Master > Field Selection > **Assign Fields to Field Selection Groups** (the OMSR path, `/nSPRO`) — copy an existing field such as weight unit to register `ZZ_EXT_NUM`, save.
- MDGIMG > General Settings > Data Modeling > Edit Data Model **MM** > entity type MATERIAL > new attribute `ZZ_EXT_NUM` with the same data element → save, activate data model (warnings can be ignored), generate data model structures.
- SMT mapping: Data Model Specific Structures > Material > SMT mapping > Transformations > Add > field mapping `ZZ_EXT_NUM` ↔ `ZZ_EXT_NUM`; he also fills the switch name (`MDG_APPLICATION_FRAMEWORK_7` in his system) — without it the mapping does not take effect; same again in the **PP mapping** (`MDG_*_PP_MAPPING`) for the material root entity, add transformation with package `ZMDG`.
- Post-processing: "post processing of data model activation not completed" appeared when opening the material CR → run the edit-data-model staging/generation step for MM *after* the mappings are done.
- UI: NWBC create material > Technical Help > Component Configuration/Customizing (create a customizing from component configuration if none exists) > drag `ZZ_EXT_NUM` from the repository onto the screen next to Authorization Group, relabel it, save.
- Verification: create material (external number e.g. 999, type/industry/description/UoM), submit, approve to final check; the external number persists; MM03 shows the field and SE16 `MARA` shows `ZZ_EXT_NUM` populated — he notes MM is a reuse-mode model.

**Key insight:** The DDIC append on IMARA is only step one — the field is invisible in the MDG UI until the data model attribute, the SMT **and** PP mappings and the UI customizing all exist, and it will not persist to MARA unless the `_X` (and `_UI`) CMD structures were appended by hand.
**Prereq:** Data modeling (type 1 vs type 4, entity attributes, activate/generate), basic SE11 append structures, UI customizing.

### 7. Data model extension with custom entity at staging level in BP
**ID:** [-jKrMych1yc](https://youtu.be/-jKrMych1yc) | **Length:** 28m | **Level:** intermediate

**In one line:** Minimum recipe for a type-4 custom entity + custom form UIBB in MDG-BP that lives only in the staging area (no table, no handler class).
- Entity type `ZCUSTOM`, entity type 4, storage/use 4, saved + data model activated. Attribute `ZCUSTOM` with data element CHAR 40, description "Router". Relationship BP header (type 1) → ZCUSTOM (e.g. `BP2Z...`), **1:1** because it is a form UIBB on the main page (list UIBBs are used for 1:n). Ignore the "not assigned to …" warning and save.
- **Generate Data Model Specific Structures** → new entries for ZCUSTOM covering PDF-based forms, search/appl of entity type, entity attributes, … → select all → *Generate selected structures*.
- GENIL_MODEL_BROWSER → enhancement over `BUPA_CASP` → dependent object `ZCUSTOM` with key structure of **BP_ROOT** (same key, because 1:1), attribute structure = generated source structure, root object BP_ROOT; then on BP_ROOT create relation `ZCUSTOM_REL` (source BP_ROOT → target ZCUSTOM, 0..1).
- SM34 `VC_MDG_BS_GENERAL_C` (customizing cluster): component BUPA / BP_ROOT / object type **BUS1006**; second entry component BUPA, entity type `ZCUSTOM`, entity object `ZCUSTOM`.
- SE80 `FPM_FORM_UIBB_GL2` → component configuration `ZMDG_ZCUSTOM_FORM` with the SAP standard BP feeder class, object ZCUSTOM, editable, rename the field to "custom router"; then overview-page config → **create Customizing** (SAP recommends never changing the delivered component configuration) → add the UIBB below Customer Details. Wire schema: source component FPM_FORM_UIBB_GL2 / config BS_BP_ROOT, target = custom config, connector class = BOL relation connector for BP, port `L_SELECTION` / `STANDARD`, relation `ZCUSTOM_REL` auto-filled (`Z*REL` must match the GenIL relation name exactly).
- **capture action = none** to hide Create/Edit buttons in the UIBB ("if I click create it will create dump"). Test with an organization CR: enter router, submit to next level, verify via workflow log (transaction **SWIA**) that the value survives; it disappears after final approval.
**Key insight:** this is a staging-only entity — the field vanishes at final check by design; adding a table + handler class is the separate step (see AOShQLm_f6I). Wiring in the UI is called a **wire**, in the data model/GenIL it is a **relationship** — the names must match.
**Prereq:** understanding of entity types 1/4 and a working FPM overview-page customizing.

### 8. DM extension custom entity and custom table, Reuse mode in BP
**ID:** [AOShQLm_f6I](https://youtu.be/AOShQLm_f6I) | **Length:** 1h35m | **Level:** advanced

**In one line:** End-to-end custom entity in MDG-BP ("Legal advisor" on a custom form UIBB) that persists to its own custom table through a custom handler class, and reads back from the active area.
- **DDIC first:** data element `ZZ_LEGADV` (domain = built-in CHAR 30, field label "Legal advisor"). In SE11 → Further Characteristics you MUST tick **Change Document**, otherwise the field is never captured in change documents. Custom table `ZT_MDG_BP2LEGALADVISOR` = MANDT, `BP_PARTNER` (BU_PARTNER, key), `ZZ_LEGADV`; delivery class C, data class APPL0, buffering not allowed, log changes, **enhancement category = can be enhanced (deep)**.
- **Data model:** MDGIMG → General Settings → Data Modeling → Edit Data Model → BP → Entity Types: new entity `ZLEGAL`, entity type 4 (custom entities must start with Z), no data element; attribute `ZZLEGADV` with data element; relationship BP header (type 1) → `ZLEGAL`, name `BP2ZLEG`, type **leading relationship**, cardinality **1:1** (type 1→4 is always leading). Activate → "adjust staging area of linked change request" gets scheduled. Then **Generate Data Model Specific Structures** with entries for ZLEGAL: SM/MM mapping, reuse active area, field control for attributes, field properties for attributes + key fields; verify the generated `*ZXX*ZLEGAL*` structure in SE11 and copy the name.
- **GenIL:** GENIL_MODEL_BROWSER → enhancement over super enhancement `BUPA_CASP` → dependent object `ZLEGAL`, key structure `BSS_BPIL_ROOT_KEY` (contains the BP GUID), attribute structure = the generated ZXX structure, root object `BP_ROOT`; on `BP_ROOT` create relation `ZLEGAL_REL` (card of assigned object 0..1). Register in SM34 view cluster **`VC_MDG_BS_GENERAL_C`**: entry 1 = component BUPA / object name BP_ROOT / object type **BUS1006**; entry 2 = component BUPA / external object name = entity type `ZLEGAL` / entity object `ZLEGAL`.
- **UI:** SE80 → Web Dynpro component **`FPM_FORM_UIBB_GL2`** → component configuration `ZMDG_ZLEGAL_FORM` with the SAP BP form feeder class, component BUPA, object ZLEGAL, "editable"; delete the BP-header fields. Then overview-page application configuration → create a **Customizing** (never edit SAP's own config) → add UIBB with that config ID, title "Legal data", drag under Customer Details. Wire schema: wire BS_BP_ROOT → FPM_FORM_UIBB_GL2/ZMDG_ZLEGAL_FORM, connector class = the **BOL REL connector for BP** (F4 list, name ends `..._BOL_REL`), port `L_SELECTION` / identifier `STANDARD`; relation `ZLEGAL_REL` is auto-filled. Set **capture action = none** on the tab to remove the Create/Delete buttons (Create dumps).
- **Handler class:** `ZCL_CUSTOM_HANDLER` extends `CL_MDG_BS_ECC_HANDLER`; six mandatory redefinitions: `SORT_ENTITIES`, `READ_OBJECT_DATA`, `GET_OBJECT_DATA_BY_ENTITY`, `MAP_DATA_TO_STAGING`, `MAP_DATA_TO_API`, `SAVE_ADDITIONAL_OBJECT_DATA`. Register under MDGIMG → Central Governance for BP → **Specify Handler Processor by Access Class** (BP → ZCL_CUSTOM_HANDLER). Add append structure to API structure **`MDG_BS_BP_S_ECC_EXTERN`** with ZZLEGADV.
- **Mechanics:** `SORT_ENTITIES` filters IT_ENTITIES and appends only `ZLEGAL` into **CT_ENTITIES** (skip this and the handler fires for every standard entity). Activation runs as background user WF-BATCH and fires `MAP_DATA_TO_API` → `SAVE_ADDITIONAL_OBJECT_DATA`; reopening the CR fires `GET_OBJECT_DATA_BY_ENTITY` (SELECT from ZT_MDG_BP2LEGALADVISOR, then must hand back **REF TO DATA**: `CREATE DATA LR_DATA TYPE ZT_...`, `ASSIGN LR_DATA TO <fs>`, fill, `ER_DATA = LR_DATA`) → `MAP_DATA_TO_STAGING`. Both use `ASSIGN COMPONENT` on dynamically typed structures.
**Key insight:** after activation the value sits in the custom table but the UI comes back empty — that is not a bug in MAP_DATA_TO_API, it is the missing `GET_OBJECT_DATA_BY_ENTITY` + `MAP_DATA_TO_STAGING` pair; and the entity only "exists" for the handler if `SORT_ENTITIES` puts it into CT_ENTITIES.
**Prereq:** DDIC element with change-document flag, an activated data model + generated structures, and the custom table (the API append structure cannot be built before the table fields are known).

**Checkpoint:** extend BP with your own attribute, see it in staging and active tables, put it on a CR screen, activate one CR. Then repeat the same on material without re-watching the video.

---


## Phase 2 - UI and Floorplan

**14 videos · 4h40m**

Watch the architecture video first even though it is 70% theory - it is the only place that explains WebDynpro -> FPM -> OVP -> GenIL and why `Z` data models behave differently from BP/MM. After that the phase runs easy-to-hard: 4-10 minute no-code wins, then CR-screen changes, then the 88-minute FPM form build.

The FPM series is one continuous build: Part 1 creates the app, Part 2 is a display-type catalogue, Part 3 adds an action, Part 4 adds a right-click context menu. Never split them across weeks.


### 1. UI Modelling in SAP MDG - Intro
**ID:** [bFJtYhM8wxU](https://youtu.be/bFJtYhM8wxU) | **Length:** 32m | **Level:** intermediate

**In one line:** The architectural "why" of MDG UI modelling — SAP GUI → WebDynpro → FPM → OVP/GUIBB, where GenIL sits between data modelling and UI modelling, and how to identify each UIBB type in a live BP screen.
- **GenIL** (Generic Interaction Layer) is the layer between data modelling and UI modelling that buffers what the UI sends. Activating a data model creates the staging tables, and for a **`Z`-namespace** model SAP auto-generates a **GenIL component/gen object**; for SAP-owned namespaces (BP, MM) no GenIL is generated, so you must build/maintain your own GenIL model + classes yourself — slower and harder.
- Web stack behind every MDG screen: HTML (now HTML5), CSS for styling, JavaScript for dynamic pages. SAP's frameworks mean you write **ABAP, not HTML/CSS/JS**: **WebDynpro** (hook methods such as `INIT`, `WDDOBEFOREACTION`/before-exit, MVC but code scattered across many places, no drag-and-drop, and **no direct GenIL access**) → **FPM = Floor Plan Manager**, built on top of WebDynpro, which adds reusable components, far less code to maintain, drag-and-drop layout, and feeder classes that **do** reach GenIL.
- FPM templates/components used in MDG: **FPM OVP** (overview page — the majority of MDG screens), **FPM Adaptable OVP** (OVP + context-based adaptation), **FPM GAF** (guided activity floor plan — wizard; steps 1..n shown across the top with Next; uses **FPM IDR** = identification region for the title/header), **FPM OIF** (object instance floor plan — behaves like an ABAP selection screen: enter parameters → Execute → next screen).
- GUIBB catalogue with feeder-class rules: **FPM_LIST_UIBB** (multiple entries/table), **FPM_FORM_UIBB_GL2** (single record; `GL2` = guideline 2, added ~2018 with the Fiori look; previously plain `FPM_FORM_UIBB`), **FPM_TREE_UIBB** (hierarchies, folder-like nodes — BP/customer hierarchy), **FPM_TABBED_UIBB** (tabs; **no feeder class of its own**, it nests list/form UIBBs), **FPM_COMPOSITE_UIBB** (several UIBBs shown simultaneously, not on separate tabs; also **no feeder class**). List and form are the two used in nearly every OVP.
- Feeder class mechanics: `CL_MDG_BS_BP_LIST` (SAP-delivered generic list feeder) is the pattern — you either use the standard feeder or **subclass it as the superclass** of your `ZCL_...` feeder. When declaring the feeder class you pass the **GenIL model/gen object** created by activating the data model, and the data-model fields then appear in the FPM repository. Inside GenIL there are root objects and dependent objects, plus an implementation class.
- Live verification in the BP/customer screen (NWBC → Customer Governance → Customer Maintenance → SE customer): F12 → DOM Explorer to prove the page is HTML SAP rendered into (editing the header text live). Right-click **Technical Help** on "Customer details" → component config `BSBP_DETAILS` → component **FPM_FORM_UIBB_GL2** is itself a WebDynpro component; right-click → *application configuration → insert application configuration* → *overview page* assigned. `Roles` = list UIBB, `New` adds rows with 1:n cardinality (restrictable in the feeder). Composite UIBB = the three UIBBs `BS_BP_DETAILS`, `BS_BP_ADDRESS_STD`, `BS_BP_ADDRESS_COMM_STD`. The tabs *General notes / Attachments* at the top of the change request = **FPM_TABBED_UIBB** wrapping form + list UIBBs. The "C Center" hierarchy view = **FPM_TREE_UIBB**.
**Key insight:** The data-model → UI bridge is the auto-generated GenIL object: because it is generated only for `Z` models, a custom data model gives you UI fields almost for free, while enhancing BP/MM screens means adopting SAP's GenIL and feeder classes (subclass `CL_MDG_BS_BP_LIST` etc.). Second must-remember: tabbed and composite UIBBs have no feeder of their own — always chase the nested form/list UIBB that actually holds the data.
**Prereq:** *MDG UI OVP Component Overview* (this video assumes the OVP → UIBB → feeder nesting and the customer screen it drills into); ideally the data-modelling video from the same channel, since GenIL is explained as its output.

---

### 2. MDG UI OVP Component Overview
**ID:** [HXY0LNcFDn8](https://youtu.be/HXY0LNcFDn8) | **Length:** 15m | **Level:** intermediate

**In one line:** The full runtime object hierarchy behind any MDG screen — WebDynpro application → application configuration → OVP component → pages → UIBBs → feeder classes → wiring — traced live through the customer OVP.
- Nesting rule stated up front: **FPM OVP component** contains multiple **pages**; every page contains multiple **UIBBs** (user interface building blocks); a **global toolbar** at the top/bottom carries the action buttons (approve/reject/save). Creation order: WebDynpro application → application configuration (runtime properties) → OVP component → FPM UIBBs with feeder classes, buttons, feeder fields → finally **wiring** between UIBBs.
- **FPM Adaptable OVP** = the commonly used variant because it supports **CBA (context-based adaptation)**; it holds two component usages: the CBA component (with a **CBA schema**, i.e. conditions) and the plain FPM OVP component.
- Two navigation routes to the same screen: right-click → **Technical Help** → *component configuration* (jumps straight into the UIBB config, skips the application layer — which is why most people never learn how the app is built), versus the long route **SCAT / WebDynpro configuration** → `BS_OVP_BP` → application configuration `BS_OVP_CU` → *Display configuration* → *Execute* (lands on the identical page from the WebDynpro layer).
- Application-configuration-level parameters are **what makes the object type different**: customer carries `USMD_OTC` = `159`, business partner `147`, supplier yet another number. Component usages of `BS_OVP_BP` are `BS_OVP_BP` (CBA, with CBA schema) and `BS_OVP_CU` → drilling into the FPM OVP component shows its used components; the OVP component configuration for customer is **BS_CU_OVP** (customer overview page).
- Inside the OVP config: pages are identified by **page IDs** (navigation from page 1 → page 2 is configured at UIBB level); UIBB types are interchanged freely — form UIBB, list UIBB, tree UIBB, composite UIBB, tabbed UIBB. Composite UIBB (`BS_OVP_BP` composite) is shown to contain three form UIBBs stacked as "Customer details"; composite and component configs each carry their own **wire schema / wire plug**, and wiring is what moves data (e.g. form UIBB → list UIBB) so one UIBB can read another's data.
- Feeder classes are the **field repository / field catalog** for a UIBB — fields are dragged from the feeder's field catalog into the form layout.
**Key insight:** The OVP is only a template. The *same* WebDynpro application `BS_OVP_BP` serves BP, customer and supplier, and the only thing that makes it "customer" is the application configuration with `USMD_OTC` = 159 — so a wrong or missing app configuration is the first place to look when a screen opens the wrong object or comes up empty. Cement the chain in this order: app → app config → component usage → FPM OVP component config → UIBBs → feeder class → toolbar schema → wire schema.
**Prereq:** *Adding MDG Apps to NWBC* (that video is where `BS_OVP_BP` / `BS_OVP_CU` are first introduced and is referenced as "the previous video" here); *UI Modelling in SAP MDG - Intro* for what FPM/feeder/GenIL mean.

---

### 3. Context based adaptations in MDG
**ID:** [ITHM22lgAwE](https://youtu.be/ITHM22lgAwE) | **Length:** 9m | **Level:** intermediate

**In one line:** Hides/moves fields per change-request type with zero code using Context-Based Adaptation inside the FPM component configuration.
- Requirement shape: hide a field (Salutation) for one CR type (`ZCUST1P2`) while keeping it for all other CR types, per business activity.
- Critical navigation: CBAs can only be maintained when you reach the screen through **Application Configuration** (Technical Help > Application Configuration > OVP overview page > BP Details UIBBs > open > Edit Customizing). Reached through Component Customizing you get the **Compare** tool and the Adaptations section is not editable ("in customizing mode we cannot add adaptations").
- Inside the opened component configuration the **Adaptations** area is already enabled by SAP — do not touch the SAP-delivered adaptations; press **+ (Add)** and create a new adaptation **based on CR type** = `ZCUST1P2`, partner category = **Organization**, give a namespace, OK, save as local object.
- In the new adaptation edit the layout directly: select the Salutation line and delete it, drag Search Term up to fill the gap, save.
- Test: same customer screen with CR type `ZCUST1P2` → salutation gone (so the user cannot even enter it); with another CR type → salutation still there.

**Key insight:** The adaptation is keyed on CR type + partner category and lives in configuration, not in the customizing transport — and the entry point matters: through Component Customizing you get comparison mode and cannot create adaptations at all.
**Prereq:** basic FPM/UI component concepts and CR type navigation in NWBC.

### 4. How to make key appear for BP Grouping or any dropdown in MDG UI
**ID:** [BbnjHrh-vtE](https://youtu.be/BbnjHrh-vtE) | **Length:** 4m | **Level:** beginner

**In one line:** One checkbox in UI component customizing makes a dropdown show the technical key next to the description (e.g. BP grouping code) without any code.
- Problem: in the change request, the **Grouping** field shows only descriptions ("only descriptions will show by default in MDG"), so you cannot see which grouping code is actually assigned.
- Right-click the field > **Technical Help** > **Component Configuration**; the existing grouping customizing already starts with `ZMDG` (a Z customizing already exists), so he creates another via **Create Customizing** — "customizing for customer overview page main data".
- In customizing mode select **Insert Grouping** (the Grouping UI element) so its attributes appear, then under **display type dependent properties** tick **Display Key**; save.
- Reopen a change request (New organization > Create customer > OK) — the dropdown now lists key + description; same trick applies to any dropdown UIBB.

**Key insight:** "Display Key" is a UI-layer checkbox only — it changes nothing in the data, and it doubles as a debugging aid because developers can read the real key straight off the screen instead of debugging the code.
**Prereq:** none (basic NWBC + technical help navigation).

### 5. Changing Highlight Colors in SAP MDG
**ID:** [juIpPuAwOlM](https://youtu.be/juIpPuAwOlM) | **Length:** 7m | **Level:** beginner

**In one line:** Overrides SAP's default "changed field" highlight colour by filling the MDG_HC_* application-configuration parameters with a numeric colour code taken from SAP's own `MDG_DISPLAY_COLORS` Web Dynpro application.
- Context: after a field is changed and Enter is pressed (validations + derivations run), MDG highlights it because highlighting is enabled in MDGIMG; the colour is SAP-delivered.
- Target parameters in **Application Configuration** (Technical Help > Application Configuration): the three SAP variables **MDG_HC_COLOR_UNSAVED**, **MDG_HC_DISABLED**, **MDG_HC_COLOR_SAVED** — they have **no F4 help**, so you must know the value format.
- Get valid values: SE80 > Edit Object > Web Dynpro > Application/Component **`MDG_DISPLAY_COLORS`** > Display > its application configuration > **Test/Execute** → a table of colour value + colour constant name (e.g. `05` for red); copy the code.
- Paste the code into `MDG_HC_COLOR_UNSAVED`, save (the value "lasts one year", i.e. it is a dated config entry), then test by changing any field and pressing Enter — highlight turns red; repeat with another code for black.
- Note: red is normally reserved for error messages, but nothing prevents using it for highlighting.

**Key insight:** There is no value help for MDG_HC_COLOR_*, so the only reliable source of legal colour codes is SAP's delivered `MDG_DISPLAY_COLORS` Web Dynpro application — run it and copy the numeric code, never guess.
**Prereq:** none.

### 6. Multi selection F4 help
**ID:** [4oNhI695gjM](https://youtu.be/4oNhI695gjM) | **Length:** 15m | **Level:** intermediate

**In one line:** Turning an existing single-value F4 exit class into a multi-select one, and rewriting the returned data as a comma list.
- Starting point: existing custom F4 class (`ZCL_CUST_SET_F4`-style) bound to the `SET_STEMS`-like attribute; Go returns 3 values, clicking one immediately navigates back with one value. This is a follow-up to his earlier "Object F4 helps in MDG" video.
- Phase 0 (configuration): set the field's multi-select property to `ABAP_TRUE` (`'X'`) — after this the dialog stays open, allows multi-selection, and only navigates on OK.
- Phase 3 (handle selection): the selection now arrives as a **table**, not a structure, so the old `ASSIGN COMPONENT ... OF STRUCTURE <ls_selection>` leaves the short-form empty and the attribute ends up blank (OK does nothing). Fix: declare the field symbol `TYPE ANY TABLE`, `LOOP AT <lt_selection> ASSIGNING <ls_selection>`, then `ASSIGN COMPONENT 'SHORT_FORM' OF STRUCTURE <ls_selection> TO <lv_short_form>`.
- Build the display string: `IF sy-tabix = 1. lv_result = lv_short_form. ELSE. CONCATENATE lv_result ',' lv_short_form INTO lv_result. ENDIF.` -> selecting C then A yields "C,A" in the field.
- Guard with `IF lv_short_form IS ASSIGNED` before use; bind the result with `set_attribute` at the end of the loop so the UI shows "C, A" after Continue.
**Key insight:** Multi-select silently breaks single-select code with no dump at all — the field just comes back empty, because a table cannot be assigned to a structure-based field symbol. The only symptom is an empty attribute after OK.
**Prereq:** an already-working single-value F4 help exit class (Phase 0 + Phase 3) for that attribute.

### 7. CR UI extension with attribute
**ID:** [pvMsc_cCXQs](https://youtu.be/pvMsc_cCXQs) | **Length:** 37m | **Level:** advanced

**In one line:** Add a brand-new custom field (CR category, CHAR1) into CR General Data, make it editable, and persist it two-way through a Z table because USMD120C cannot be appended.
- Discover the anchor: CR UI right-click -> Technical Help -> Component Config -> General Settings -> **Feeder Class Parameters**; the CR block is the General component, whose root object is `CR_ROOT` (model browser -> CR display -> root objects) with attribute structure `BSS_CR_ROOT_ATTRIBUTES` (BS_* root attributes structure).
- Extend: append structure `ZCR_CAT`-style ("custom CR UI extension") to that attribute structure with field `ZZ_CR_CAT` (char1; text alternative also possible), enhancement category "Can Be Enhanced (Deep)" to clear the warning. Refresh: `ZZ_CR_CAT` appears in Component Config and can be drag-dropped under Description, label "CR Category", saved. Field is greyed out/read-only at this stage.
- Make it editable (recommended = runs once): handler class of the CR root, method that handles **attribute properties** (`GET_ATTRIBUTES` / `CHANGE_OBJECT` / attribute-properties area), implicit enhancement -> `iv_property_object->set_property_by_name( name = 'ZZ_CR_CAT' value = 'CHANGEABLE' )`. Do not use the other, multiple-times-per-process option.
- Persistence blocker: `USMD120C` is the CR header table (CR type, status, created by...) but its structure is flagged "cannot be enhanced" — appending `ZZ_CR_CAT` fails with "structure USMD120C cannot be enhanced".
- Custom table in SE11: `ZT_CR_CAT` — MANDT + `CR_ID` (`USMD_CREQUEST`) as primary key, `ZZ_CR_CAT` CHAR1, data class Master data, size category 0/minimum, enhancement category "Can Be Enhanced (Deep)". Note the field-name rule: an underscore is not permitted in 2nd/3rd position, hence `ZT_CR_CAT` not `Z_USMD_CR_...`.
- Feeder class `CL_USMD_CR_UIBB_GENERALDATA` (CR General Data), `GET_DATA`: at the TOP of the method add an enhancement that extracts `ZZ_CR_CAT` and `CR_ID` from `CS_DATA` via `ASSIGN COMPONENT` and does `MODIFY zt_cr_cat` (set MANDT = `sy-mandt`). This is written before the superclass runs, so it is still valid — but the value is then overwritten in `CS_DATA` by the standard call, hence a second enhancement at the END of `GET_DATA`: `SELECT SINGLE * FROM zt_cr_cat WHERE cr_id = lv_cr_id`, then assign back into `CS_DATA` field symbol.
**Key insight:** One-way binding looks "broken" — the value is in ZT_CR_CAT after Submit but blank in the UI. The fix is two enhancements in the same implementation: write at the top of `GET_DATA`, read back at the end. And because USMD120C is locked, any CR-header extension must go to a side table.
**Prereq:** FPM/component-config access in the CR UI, SE11 table creation, implicit enhancement basics.

### 8. SAP MDG CR section default collapsing based on CR type
**ID:** [XflP-k9u0tc](https://youtu.be/XflP-k9u0tc) | **Length:** 22m | **Level:** advanced

**In one line:** Force the CR overview tabbed UIBB to open collapsed for one specific CR type by enhancing CL_USMD_COMMUNICATOR->ON_START.
- Debug path: SE24 -> `CL_USMD_COMMUNICATOR` (assistance class of MDG Communicator, links the CR to the rest of the UIBBs), break point in `ON_START`. In locals: `action = create`, `io_obp`; inside io_obp the UIBB list lines 39/40 — line 39 = form UIBB inside CR master, line 40 = the CR overview tabbed window UIBB.
- Proof of concept: manually flip the `COLLAPSED` flag of the CR-overview UIBB instance to `X` in debugger -> every CR opens collapsed; therefore the instance is controllable per CR type.
- Implementation: SE24 `CL_USMD_COMMUNICATOR`, Edit -> Enhancement -> Show Implicit Enhancement Options -> create enhancement `ZE_...` ("collapse CR uibb for CR types Z_CUST_1_P1"), local object, inside `ON_START`.
- Code shape: `io_obp->get_uibbs( EXPORTING content_area = 'BS_BP_OVP' IMPORTING et_uibb = DATA(lt_uibb) )` into `TY_T_UIBB`; then `READ TABLE lt_uibb WITH KEY component = 'FPM_TABBED_UIB' interface_view = 'TABBED_WINDOW' config_id = 'USMD_CR_OVERVIEW' INTO DATA(ls_uibb)`; set `ls_uibb-collapsed = 'X'`; types involved `TY_S_UIBB`, `IF_FPM_OVP` structure.
- CR-type filter: `DATA(lo_context) = cl_usmd_app_context=>get_context( )`, guard `IF lo_context IS NOT INITIAL`, then `lo_context->get_attributes( IMPORTING ... = lv_cr_type )`; wrap everything in `IF lv_cr_type = 'Z_CUST_1_P1'`.
**Key insight:** `get_uibbs` must be given the EXPORTING parameter `content_area = 'BS_BP_OVP'`; without it the enhancement compiles and activates but never fires (silent no-effect). Also ON_START is called only once when the UIBB starts, not on every open/close of the CR.
**Prereq:** CR type already existing (here Z_CUST_1_P1) and CR description already being defaulted — this video only handles the collapse.

### 9. Hiding UIBBs according to role
**ID:** [E_ouMzBTLEo](https://youtu.be/E_ouMzBTLEo) | **Length:** 21m | **Level:** advanced

**In one line:** Hides a whole UIBB (bank accounts on the SE customer OVP) at runtime through the OVP exit class, driven by a PFCG role check — instead of statically deleting it from the OVP configuration.
- Requirement shape: the BP/customer overview page in NWBC (Change Request → Customer Maintenance → SE customer → New → Organization) shows a UIBB sequence (change request section, customer details, roles collapsed, addresses …). Sensitive data such as **bank accounts** must disappear for users without the right role; removing it in the component configuration is static and cannot cover that.
- Hook: class **`CL_MDG_BS_BP_OVP_*`** exit class (heard as "CL_BS_BP_OVP_H") method **`IF_FPM_OVP_CONF_EXIT~OVERHEAD_EVENT_OVP`**. Implementation via **implicit enhancement**: SE24/SE80 → *Edit → Enhancement Operations → Show Implicit Enhancement Options* → Enhance → create enhancement implementation **`Z_RESTRICT_BANK_ACCOUNT`** (short text "to restrict bank account"), local object → insert code as a post-exit.
- The method's importing parameter only references the interface, so inspect it: usable methods are `ADD`, `CANCEL`, `CHANGE…`, and the pair needed here — **`GET_UIBBS`** (returns `ET_UIBBS`) and **`CHANGE_UIBB`**. Retrieve with an inline declaration inside `TRY … CATCH` so a missing assignment cannot dump.
- The UIBB row carries field **`HIDDEN`** of type **`FPM_HIDDEN`**: **space/empty = visible**, **`X` = hidden and excluded from the event loop** (feeder not processed), **`T` = hidden but still processed in the event loop** (backend keeps running). `READ TABLE lt_uibb WITH KEY … ASSIGNING <ls_uibb>` on the UIBB's **config ID** — taken from right-click → Technical Help on bank accounts (e.g. `BSBP_BANK_ACCOUNTS…`) — guard with **`IF <ls_uibb> IS ASSIGNED`**, set `hidden = 'T'`, then **`io_ovp->change_uibb( <ls_uibb> )`**.
- Role gate: function module that returns the roles of the current user drawn from **`PAGR_USERS`** (declared as `DATA lt_agr_users TYPE TABLE OF agr_users`, filled via the FM), then `READ TABLE lt_agr_users WITH KEY agr_name = 'Z_BANK_DETAIL' TRANSPORTING NO FIELDS`; `sy-subrc <> 0` → role absent → set `hidden = 'T'`. Verified both ways by assigning/removing the user in PFCG: with the role the UIBB appears, without it the UIBB is gone **and** absent from the personalization / *Change Layout* list. `X`/`T` vs empty is shown to be the difference between hidden and visible.
- Why this class: SCAT → FPM Adaptable OVP → application **`BS_OVP_BP`** → application configuration (customer) → FPM OVP component (`PROCESS CUSTOMER` page) → **General Settings → Application Controller Settings** → configuration `BS_OVP_BP` + configuration name `SETTINGS BS_OVP_BP` → that WebDynpro component's **assistance class** is the class holding the OVP overhead/exit logic.
**Key insight:** Use `HIDDEN = 'T'` (hidden but still processed in the event loop) rather than `'X'` (hidden and excluded from the event loop) when the backend must keep working with the UIBB; and hiding in the overhead exit is stronger than static removal because the UIBB also disappears from personalization, so users cannot re-add it. Remember the entry point: **`IF_FPM_OVP_CONF_EXIT~OVERHEAD_EVENT_OVP`** on the OVP exit class, reached via the application controller settings' assistance class.
**Prereq:** *MDG UI OVP Component Overview* (you must be able to navigate app → app config → FPM OVP component → application controller settings, which is the last third of this video) and *UI Modelling in SAP MDG - Intro* (UIBB concepts and Technical Help). Part 3/4 help for feeder/event fluency but are not required.

### 10. Inserting Images in MDG UI
**ID:** [gZkhnUdljT0](https://youtu.be/gZkhnUdljT0) | **Length:** 23m | **Level:** advanced

**In one line:** Puts a static logo/image on an MDG (FPM) screen end-to-end: append an image field to the GenIL/BP attribute structure, import the image into the MIME repository, drag it into the UI as display type Image, and fill its URL in the feeder class `GET_DATA`.
- Sequence he insists on: (1) enhance the GenIL/BP structure, (2) have the image file ready, (3) import it into the **MIME repository**, (4) UI customizing, (5) feeder-class enhancement — the field must exist in the structure before the UI repository can show it.
- Step 1: right-click screen > Technical Help > Component Customizing > General Settings > **Feeder Class Parameters** to read the FPM component and object (BP), open them in the **GenIL model browser** > BP root > **attribute structure** (not key structure) > create append structure `ZAPP_BP_IMAGE` with component `IMAGE_FIELD`, component type = the predefined FPM image/string type; set the enhancement category, activate (ignore warnings).
- Step 2/3: import the file in **MIME Repository** (in SE80; if the node is missing, enable it via Utilities > Settings); navigate **SAP > Public > BC > UR (Unified Rendering)** — only nodes shown "activated"/dark can be reached through the ICF, inactive services will not resolve; right-click > **Import MIME Object** > choose the GIF (e.g. reliance logo) > description > save as local object.
- Step 4: reopen/refresh the component customizing so `IMAGE_FIELD` appears in the repository, drag it below Organization data, stretch the layout to about four rows, change **Display Type** from input field to **Image**, set label text "Logo", save (no transport in the demo system).
- Step 5: display the feeder class in SE24 and create an **implicit enhancement** `Z_IMAGE_BP` in **`GET_DATA`** (called on every initiate/on-enter roundtrip): `ASSIGN COMPONENT 'IMAGE_FIELD' OF STRUCTURE cs_data TO <lv_image_field>` — note `CT_FIELD_USAGE` does not help here — then set `<lv_image_field> = '//SAP/PUBLIC/BC/UR/…/reliance_logo.gif'`, activate and retest; the logo renders.

**Key insight:** An image field on an MDG screen is just a normal string attribute whose value is a MIME-repository URL — so the whole job hinges on the exact path `//SAP/PUBLIC/BC/UR/...` pointing at an **activated** ICF/MIME node, plus a `GET_DATA` assignment on every roundtrip since FPM rebuilds the screen.
**Prereq:** FPM/feeder-class basics, UI component customizing, ability to create append structures and SE24 implicit enhancements.

### 11. Simple FPM Form Application - Part 1
**ID:** [pxfn1s6Yg_0](https://youtu.be/pxfn1s6Yg_0) | **Length:** 28m | **Level:** intermediate

**In one line:** Builds a working standalone FPM overview-page application ("simple bank form") from zero — WebDynpro app, application configuration, OVP component configuration, form UIBB, custom feeder class, field catalog, drag-and-drop layout and a PFCG role to launch it in NWBC.
- In **SCAT** → FPM OVP component → create WebDynpro application **`Z_FPM_BANK_APP`**; interface view = `FPM_WINDOW`-style default (single interface view, default view, plug maintained), save as local object. The app then appears under *Web Dynpro applications* with a collapsed arrow; the arrow stays dotted/▲ = **no application configuration assigned**.
- Right-click the app → *create/change configuration* → application configuration ID **`BANK_APP`** (1 application : n application configurations = reusability). Then in **Component Configurations** create the OVP component configuration **`Z_FPM_BANK_APP_CONFIG`** (this *is* the overview page), go back to the app config and assign that config ID → the component usage is filled automatically. Division of labour stated by the trainer: application = just the FPM component to launch it; application configuration = properties for that instance; component configuration = UIBB sequence; UIBB = field layout.
- Open the configuration → OVP page editor → **+ UIBB** → **`FPM_FORM_UIBB_GL2`** → config ID **`Z_BANK_SIMPLE_FORM_UIBB`** → confirm save → *Configure UIBB* → create the UIBB-level component config.
- Feeder class from scratch in **SE24**: **`ZCL_BANK_FORM_UIBB_FEEDER`**, add interfaces **`IF_FPM_GUIBB_FORM`** + the generic GUIBB interface (both get inherited), then implement/activate the generated methods one at a time (`GET_DEFINITION`, `GET_DATA`, `PROCESS_EVENT`, flush/check-config…) because activating all at once causes runtime dumps. Assign this class as the UIBB's feeder class in the UIBB config.
- Field catalog in **`GET_DEFINITION`**: export `ET_FIELD_DESCRIPTION` via `CL_ABAP_STRUCTDESCR`/`describe_by_data`, and declare the structure as a **global public type `GTY_BANK_DATA`** (`TYPES BEGIN OF gty_bank_data … bank name TYPE char255 … END OF`) — deliberately global, not local, because **`GET_DATA` needs the same type again**. Refresh the UI → fields appear in the repository → drag into the form, relabel (e.g. `CAR20` → "Bank name", add "registration code", IFSC, phone, website, country with F4 from the existing country data element / BP or MM value help).
- Launch it: **PFCG** role **`Z_SHOW_BANK_DETAIL`** (empty menu) → assign user → **Menu** → *assign WebDynpro application* (FPM sits on WebDynpro so this node type is used) → application `Z_FPM_BANK_APP` + configuration `BANK_APP` → create a folder "Simple bank app" and drag the node into it → refresh NWBC → new tab renders the form.
**Key insight:** The dependency order is the whole lesson — a component (OVP) configuration must exist **before** it can be assigned in the application configuration, the UIBB's component config must exist **before** the feeder class can be attached, and a WebDynpro app without an application configuration silently refuses to open (dotted arrow). And declare the field structure as a class-level public type, or you will duplicate it in `GET_DATA` and fight type mismatches.
**Prereq:** *UI Modelling in SAP MDG - Intro* (FPM/GUIBB/feeder concepts) and *MDG UI OVP Component Overview* (the app → app config → component config chain this video builds by hand).

---

### 12. Simple FPM Form Application - Part 2
**ID:** [nemZlP1b11k](https://youtu.be/nemZlP1b11k) | **Length:** 33m | **Level:** intermediate

**In one line:** A complete tour of every field **display type** available on a form UIBB field, and the data-element/domain prerequisites each one imposes.
- Default behaviour: every field exported through `GTY_BANK_DATA` arrives in the UIBB config as **input field** unless `GET_DEFINITION` says otherwise. Display type is changed per field in the UIBB config.
- **Checkbox group**: switching a field from input field to checkbox group throws *"expected configuration is inconsistent, preview is not possible"* because a plain `CHAR2`/`CAR2` has no fixed values. Fix = new **data element `Z_COUNTRY`** (field label "Country") over a **domain with a value range** (India, Iraq, China, Israel, Canada), reassign the structure field to `Z_COUNTRY`, then set **column count = 5**. Allows multi-select, reduces clicks vs F4.
- **Dropdown list box** and **radio button group**: same domain-driven behaviour, **single** selection only (radio buttons show all options at once — only for a small list; dropdown hides them behind one click). All three pull their entries from the **domain fixed values**.
- **Explanation**: no value shown; text entered in the display-type "text" property (e.g. "country code is mandatory as geographical identity") appears only after right-click → **Display quick help** (and *Hide quick help* removes it). For long text, leave the field empty and point to an **SC61** document in *display-type dependent properties* — document class must be **General text (`TX`)**; the document content then renders in quick help.
- **Formatted text edit** (WYSIWYG in the UI: bold/italic/underline/bullets, Ctrl+B / Ctrl+I like Word) vs **formatted text view** (same formatting but constant/read-only, text maintained in the property). Gotcha: formatted text edit is **always truncated to the domain length** of the field (a `CHAR2` country field only keeps 2 characters).
- Remaining types: **image** (MIME object stored via the config browser, path handed over in `GET_DATA`), **input field** (default), **input tokenizer** (chip/tag with one-click delete; modes *text only / text ID / ID text*, plus suggest values, suggest history, row count — ID modes show the key such as `IN` next to the description), **link to action** (needs an action, handled in `GET_DATA`/`PROCESS_EVENT` via IF/CASE), **link to popover** (assign a dialog page, data supplied from `GET_DATA`), **link to URL** (URL must be set in `GET_DATA` in the field-usage `-LINK` entry **and** the field marked changed = `X`, otherwise the link is not propagated at runtime), **text edit** (multi-line, Enter = new line, height = rows) and **text view** (read-only plain text, no input/display toggle needed).
**Key insight:** Display types are **not** a cosmetic toggle — checkbox group, dropdown and radio button all read the **domain's fixed values**, so any "preview is not possible / configuration inconsistent" error means "your data element has no value range". Build the `Z` data element + domain first (and remember it changes the structure type in the feeder), then the display type just works.
**Prereq:** *Simple FPM Form Application - Part 1* (the same `Z_FPM_BANK_APP` / `ZCL_BANK_FORM_UIBB_FEEDER` / `GTY_BANK_DATA` is being extended; the video explicitly recaps Part 1).

---

### 13. Simple FPM Form Application - Part 3
**ID:** [yK72NQNf-98](https://youtu.be/yK72NQNf-98) | **Length:** 18m | **Level:** intermediate

**In one line:** Adds a custom button to a form UIBB by exporting an action definition from the feeder, then makes it actually persist data — event handling in `GET_DATA` plus `INSERT` into a Z table with error messaging.
- The blocker first: in the OVP editor, adding a **button** asks you to pick an **action**, and the list is empty — "actions are a prerequisite for buttons", so nothing can be added until the feeder exports one.
- Button definition in **`GET_DEFINITION`** → exporting parameter **`ET_ACTION_DEFINITION`** (table type `FPMGB_T_ACTIONDEF`, not a structure) using inline ABAP 7.4 `VALUE #( ( id = 'SAVE' enabled = abap_true text = 'Save UI data' ) )`. **ID and ENABLED are mandatory**; `text` shows up while configuring. Reactivate → the button shows in the repository (its label/name visible) → drag it under the last field (preferred over the *element* dialog) → the configured text can be overridden in the UIBB config.
- Why the button does nothing yet: point the debugger at **`GET_DATA`** — on first render `io_event->mv_event_id` = **`FPM_START`** (this is where you set default values); clicking the button arrives with `mv_event_id` = **`SAVE`**. Handle with `CASE io_event->mv_event_id WHEN 'SAVE'`.
- The UI contents arrive in **`CS_DATA`** (dynamic structure — cannot be used directly in ABAP SQL), so **`MOVE-CORRESPONDING cs_data TO ls_db`** into a work area typed on the transparent table **`Z_BANK_TABLE`** (`MANDT` first → client-dependent, then bank name, registration code, IFSC, phone, country, website), then **`INSERT z_bank_table FROM ls_db`** and check `sy-subrc`.
- Error path: on failure raise a message in **`ET_MESSAGES`** (type `FPMGB_T_MESSAGES`) with **`PLAINTEXT`** = "unable to insert data into database, please contact administrator" and **severity `E`**. Demo: re-entering the same key → INSERT fails → the message appears in the UI.
**Key insight:** An action, not the layout editor, creates a button — no row in `ET_ACTION_DEFINITION` means no selectable action in the OVP config. And the event id you invent there is the exact string you must `CASE` on in `GET_DATA`; remember `FPM_START` is the initial-render event used for defaults. `cs_data` is dynamic and must be moved into a typed structure before any DB statement.
**Prereq:** *Simple FPM Form Application - Parts 1 and 2* (same app, feeder and form; part 1 built `GET_DEFINITION`/field catalog, part 2 changed the field display types).

---

### 14. Simple FPM Form Application - Part 4
**ID:** [mjoSb4Rrtdo](https://youtu.be/mjoSb4Rrtdo) | **Length:** 9m | **Level:** intermediate

**In one line:** Builds a right-click **context menu** (not used in standard MDG but available) whose item fires a feeder action that clears the form — menu schema, menu item, event id, attaching the menu, and the data-changed flag.
- Locate it via **Technical Help** on the form → component configuration → this belongs to the form UIBB → below the **FPM UIBB schema** there is **`MENU_SCHEMA`** (the context menu schema).
- Edit mode → **Add Menu** → context menu ID e.g. **`IDCORE_MENU_ONE`** / name `MENU_ONE` → **Add Menu Item** → item type **`single action`** (alternatives: separator) → set **FPM event ID = `REFRESH`** (the text auto-fills). Without a feeder action this ID does not exist yet, so…
- In **SE24** feeder class `GET_DEFINITION`, add a **second row** to `ET_ACTION_DEFINITION`: `id = 'REFRESH'`, `enabled = abap_true`, `text = 'refresh'` → activate → two actions now exist, the new one appears in the menu item's selection.
- A menu schema is only **logical** — it does nothing until attached: either per **field** (field properties → *context menu ID*) or UIBB-wide via **General Settings → Context Menu ID** (may need *show more* to reveal the field) → Save → refresh the app → right-click now lists **refresh**.
- Handler in **`GET_DATA`**: `WHEN 'REFRESH'` → **`CLEAR cs_data`** then **`ev_data_changed = abap_true`** (`'X'` also accepted) so FPM knows the buffer changed; without that flag the cleared data is not redrawn.
**Key insight:** Two separate things must both be true for a context menu to appear — the **menu schema with its items** *and* the **context menu ID assignment in general settings** (or on a specific field). And any feeder-side data change must set `ev_data_changed`, otherwise the screen keeps showing stale values.
**Prereq:** *Simple FPM Form Application - Part 3* (the `SAVE` action, `GET_DATA` event handling and `cs_data` all come from there; this part only adds a second action and a `WHEN` branch).

---

**Checkpoint:** hide one UIBB by role, add a multi-select F4 to a field, add a custom field to the CR header with your own label. You should be able to say which layer you touched each time (UIBB config vs CR UI vs FPM app).

---


## Phase 3 - Process Modeling: CR types and workflow

**11 videos · 6h39m**

Custom CR type is the pivot of the whole implementation - everything in Phase 3 and 4 filters on a CR type. Do it first and keep that CR type (`ZCUST1_P1`/`ZCUST1_P2` in the videos) for every later exercise.

Workflow videos are ordered by the problem they solve, not by upload date: build a parallel workflow -> the three requestor/approver edge cases -> instant rejection -> notification and follow-up CR.


### 1. Creation of Custom CR type in SAP MDG
**ID:** [2FvrNfH--4c](https://youtu.be/2FvrNfH--4c) | **Length:** 52m | **Level:** intermediate

**In one line:** Build CR type ZCUST1_P2 from scratch and wire a complete BRFplus rule-based workflow (submit -> approve -> background activation -> final check approved, plus reject -> rollback).
- CR type: MDGIMG -> General Settings -> Process Modeling -> Change Request -> **Create Change Request Type**: data model `BP`, description "Create Customer Plan", main entity type `BP_HEADER` (type 1), plus `ADDRESS`, `BP_RELATIONSHIP` etc. Entry type must contain the main entity type first or the entry is not saved; omitting ADDRESS gives "address cannot be changed via change request". Workflow template `WS...` (always used with BRFplus), business activity e.g. CREATECUSTOMER — that activity is what makes the CR appear in the NWBC New popup.
- Workflow config: Rule-based workflow -> "Configure your rule based workflow" for `ZCUST1_P2` (local object). Three decision tables: **Single Validation** (the controller), **User Resolution**, **Non-User Resolution**. Hide the unused columns via table settings so only ~5 remain: Workflow Step, CR Status, Condition Area, Next Step, Previous Action.
- Single Validation rows: (step 00, condition 1) -> next step 30, CR status "Final Approval"/custom "To be approved by manager"; (30 + previous action 03 approve) -> 50; (30 + 04 reject) -> 60; (50 + action "Activation Successful") -> 99 with status Final Check Approved; (50 + activation failed) -> back to 30; (60 rollback) -> 99 with Final Check Rejected. Action codes: approve = 03, reject = 04. Condition Area is just an alphanumeric key that must exist in whichever table handles that step.
- User Resolution: condition area 1, agent group `01` (always), **step type `02`** (= approve 03 + reject 04 buttons, in that order), agent type `US`, agent = SAP user `TEST_MDG1`. Step types themselves live in MDGIMG -> Change Request -> **Change Request Types and Actions** (step type 02 exposes actions 03/04).
- Non-User Resolution (background): condition area 2, agent group 01, **process pattern 06** (05 is the near-identical alternative) = activate; process pattern **99** = complete workflow; process pattern for rollback on reject. Verify all three tables are in active state before testing.
- Test: submit -> status Final Approval, workflow log shows pending with TEST_MDG1; log in as TEST_MDG1 -> approve and reject buttons appear (from step type 02) -> approve -> background step activates and completes -> Final Check Approved, BP number generated, CR closed and re-usable. Reject path: reason note recorded -> Final Check Rejected -> data rolled back and disappears from the system.
**Key insight:** Never map "approve" straight to CR status Final Check Approved. Approval must go to a **background/non-user step** that runs activation and then a completion step — otherwise the CR stays locked and no further CRs of that type can be processed. Main entity type missing from Entry Types silently blocks saving too.
**Prereq:** a BP data model with business activities; BRFplus access; NWBC with the two test users.

### 2. Hiding CR types in popup, making CR attributes mandatory or default values
**ID:** [_Ab39RJ_1uM](https://youtu.be/_Ab39RJ_1uM) | **Length:** 19m | **Level:** intermediate

**In one line:** One BAdI (MDG_UNCORE_CR_DEFAULTS) does all three CR-header tricks: hide a CR type from the New popup, default the description, and force Priority to mandatory.
- Locate CR type IDs: MDGIMG -> General Settings -> Process Modeling -> Change Request -> **Create Change Request Type** (key + description), e.g. "Create customer parallel" = `ZCUST1_P1`, "Create customer Planet" = `ZCUST1_P2`.
- BAdI: Process Modeling -> Change Request -> CR UI defaults (`MDG_UNCORE_CR_DEFAULTS`); enhancement `ZEI_MDG_UNCORE_CR_DEFAULTS`, implementation `ZBIOR...`, class `ZCL_MDG_CR_UI_PROPS`; filter value = data model `BP`; activate all four methods empty first.
- Method `FILTER_CR_TYPE` (changing table `CT_CR_TYPE`): the table has no structure — its line type is directly the data element `USMD_CREQUEST_TYPE`, so `DELETE ct_cr_type WHERE table_line = 'ZCUST1_P1'`. Debugger proof: deleting one row in the changing table drops 6 CR types to 5 in the popup.
- Method `GET_CR_ATTRIBUTES`: `IF iv_cr_type = 'ZCUST1_P2'` -> `cs_cr_data-cv_description = 'Create Customer ...'`; this is the only hook for CR-header defaulting.
- Method `SET_CR_FIELD_PROPERTIES`: `cs_cr_data-cv_priority_field_prop = 'M'`. Field-property codes (from the domain behind the field-property data element): `C` = optional, `R` = read only, `M` = required, `H` = hidden.
**Key insight:** Do not "hide" a CR type by removing its business activity — that also kills it for the background program. Hiding belongs in FILTER_CR_TYPE. The field-property codes are C/R/M/H; anything else silently does nothing.
**Prereq:** CR types exist and you can read them in MDGIMG; BAdI enhancement basics (SE19/SE18).

### 3. Restriction of account group based on CR types in MDG BP
**ID:** [RGICx0gfuC4](https://youtu.be/RGICx0gfuC4) | **Length:** 32m | **Level:** advanced

**In one line:** A custom CR-type-to-grouping table plus an implicit enhancement in the grouping dropdown feeder method, trimming the value set at runtime.
- Customizing table in SE11: `ZMDG_CR_ACCOUNT_GROUPS` — MANDT as key (client-dependent), `USMD_CREQUEST_TYPE`, `BP_GROUPING` as second key, foreign key BP_GROUPING -> `TB001`, delivery class C, table maintenance generator created (Utilities -> Table Maintenance Generator, function group, one-step, no auth group) so it can be maintained in SM30.
- Find the feeder class: in the CR UI right-click -> Technical Help -> Component Config -> General Settings -> **Feeder Class** (here the BP root feeder class). The dropdown values are not built on page load — they are supplied by `GET_ATTRIBUTE_VALUE_SET`; debugging shows 159 grouping values arriving in `ET_VALUE_SET` with `IV_ATTRIBUTE_NAME = 'GROUPING'`.
- Enhancement: SE24 on that root feeder class, `GET_ATTRIBUTE_VALUE_SET`, Edit -> Enhancement -> Show Implicit Enhancement Options -> create `ZEI_MDG_RESTRICT_GROUPING`.
- Logic: skip unless `iv_attribute_name = 'GROUPING'`; get CR type via `CL_USMD_APP_CONTEXT=>GET_CONTEXT( )` then `get_attributes` — store the context in a variable and test `IS NOT INITIAL` first, otherwise an empty context dumps. Then `SELECT bp_grouping FROM zmdg_cr_account_groups WHERE crequest_type = lv_cr_type` into a table.
- Build a selection table of type RSDSSELOPT-style `SIGN/OPTION/LOW/HIGH` (`SIGN = 'E'`, no HIGH needed), loop the selected groupings, `APPEND` each, then `DELETE et_value_set WHERE value IN lt_selopt`. Keeping the SELECT-OPTIONS build outside the loop avoids re-appending stale rows.
- Result: only the maintained groupings (e.g. two, then three after adding one row in SM30) appear in the dropdown for CR type `ZCUST1_P2`; the same pattern works for any CR-type-dependent dropdown.
**Key insight:** `ET_VALUE_SET` must be *deleted from*, not rebuilt, and the sign has to be `E` on the select-option, otherwise you show exactly the groupings you meant to hide. Also the same enhancement must be created in the class actually used at runtime — after moving it, delete the leftover duplicate implementation or it fires twice.
**Prereq:** the custom CR type (ZCUST1_P2) and working SE11/SM30 customizing-table skills; implicit enhancement experience.

### 4. MDG BP CVI field configurations for address, sales area and company code data
**ID:** [6P3zaxPPYv8](https://youtu.be/6P3zaxPPYv8) | **Length:** 12m | **Level:** intermediate

**In one line:** Why fields like Street and Reconciliation account suddenly become mandatory in the ERP-customer block, and how account-group field status in S/4 (not CVI) drives it.
- Table contrast: address lives in `BUT000` separately, whereas `KNA1` holds address fields inline (LAND1, NAME1, NAME2, PSTLZ, SORTL, REGIO) — that mismatch is exactly why a CVI mapping is required; address is only maintained at BP level in MDG.
- Repro: BP grouping that is externally numbered (e.g. 500408 on the "Birla"/external grouping) + customer role `FLCU00`/`FLCU01` added -> the ERP Customer block shows "Standard address" but no address fields, yet Done triggers "Enter a value for Street".
- Cause: SPRO -> Logistics – General -> Business Partner -> Customers -> Control -> **Define account groups and field selection for customers**, account group (000001 in the demo) mapped from the BP grouping, Field status -> General data -> Address -> Street = Required entry.
- Fix demo 1: set Street to Optional entry -> after re-creating the customer, the CR no longer demands Street (country remains mandatory from standard).
- Fix demo 2: Field status -> Company code data -> Account management -> Reconciliation account = Required entry -> after adding a company code in the CR, reconciliation account becomes mandatory.
- Page layout: Settings -> Change page layout -> add UIBBs "ERP Customer Data", "ERP Customer Company Code Data" (or both) to actually see sales area/company code blocks.
**Key insight:** Missing/mandatory fields in the MDG BP UI are frequently S/4 account-group field-status configuration leaking in through CVI, not missing CVI mapping — check S/4 first before touching MDG. This config is S/4 config: in real projects it goes through the functional consultant's transport.
**Prereq:** BP grouping + customer account group + CVI number assignment already working (i.e. the c4IXaHVKfuY basics).

### 5. Making attachment as mandatory in a CR in SAP MDG
**ID:** [PqHVKwlLiDs](https://youtu.be/PqHVKwlLiDs) | **Length:** 19m | **Level:** advanced

**In one line:** A USMD_RULE_SERVICE validation BAdI that reads CR attachments and blocks check/submit until at least one attachment exists.
- IMG: MDG -> General Settings -> Data Quality and Search -> Business Add-Ins -> **Validations and Derivations** -> create enhancement implementation `ZEI_...`, BAdI implementation `ZBA_BADI_..._MDG_BP_VALIDATIONS`, class `ZCL_MDGBP_VALIDATIONS`; an enhancement needs at least one BAdI implementation before it can be activated.
- Filter values: `MODEL = BP` and `ENTITY_TYPE = BP_HEADER` (BP_HEADER is the type-1 entity) — filter must be maintained on both.
- Filter conflict: filter values must be unique per BAdI implementation inside an enhancement; identify the clashing SAP implementation via SE18 (`USMD_RULE_SERVICE`), e.g. the standard BP description check on the same filter. Do not deactivate SAP's in SE18 — go to MDGIMG -> Process Modeling and Data Quality -> Data Quality -> Business Add-Ins -> **Activate/Deactivate BAdI implementations** (the "active" flag there is display-only, the deactivate flag is editable).
- Activate every method individually (all four); skipping one causes runtime errors, not just warnings.
- Code: guard `IF io_model IS NOT INITIAL`; get CR type with `CL_USMD_CR_UTIL=>GET_CR_TYPE_BY_CR( i_cr_id )` (alternative `USMD_120C`) and compare to `Z_CUST_1_P1`; then `io_model->read_cr_value( EXPORTING fieldname = 'USMD_CREQUEST' ... )` into `USMD_TS_ATTACHMENT` — the attachment/notes read flag is OFF by default and must be enabled, and the field name must be `USMD_CREQUEST` because CR data (not entity data) is being read.
- If `lt_data IS INITIAL`: build the error at runtime with `CL_D_MESSAGE=>CONVERT_TEXT_TO_MESSAGE` (avoids SE91 message class for a demo) and APPEND it to `et_message`; message surfaces as MSMD5-style error and blocks Submit. With one attachment present, the table has one row (file type, file size, title, content in encrypted form) and no error.
**Key insight:** `read_cr_value` returns nothing unless you explicitly switch on the read-attachments/notes option — otherwise the validation always fails even when an attachment exists.
**Prereq:** a custom CR type (Z_CUST_1_P1) to filter on; SE18/SE24/SE11 basics.

### 6. SAP MDG Simple parallel workflow
**ID:** [aHzAdGHS3g8](https://youtu.be/aHzAdGHS3g8) | **Length:** 45m | **Level:** advanced

**In one line:** Designs and builds a 3-approver parallel workflow from a copied CR type: BRF+ step matrix, agent table with 3 agent groups, merge BAdI, plus approve-all and reject-one test runs.
- Design first: step **00** requester → **20** parallel split to approvers → **30** merge → **90** Act → **31** activation successful → **99** Final check approved; reject path → **RLB** (rollback) → **95** → **99** Final check rejected.
- Copy CR type `Z_CUST_P1` → new "create customer parallel" type, then `USMD_SSW_RULE` → single evaluation table rows: previous 00 / condition alias **AP1** / CR step **20** / status "to be approved by data steward" / process pattern **2** + parameter = service name for matching; keep the **parallel step / parent step = 20** and branches for agent groups 1, 2, 3; action **03** (approve) from step 20 → **30**; **CMP** (completion) → 99; step 30 + action **31** → 99 final check approved; step 30 + action `<>31` (activation failed) → agent **REQ** with status **07** and CR step 00/01; step 30 + action **04** (reject) → **RLB**, parent AP1, CR step **95**; step 95 → CMP → 99 final check rejected.
- Agent assignment table: `AP1` entered **three times** with agent groups 1/2/3, user type **US**, users TEST_MDG1/2/3, step type **2** (approve + reject); `REQ` with agent group 1, user type **SU**, value **INIT** (initiator), step type **7** "finalist processing" = the only single-button step; **CMP** = process pattern *completion*, **RLB** = *rollback*, **ACT** = *activation bypass snapshot*.
- Merge BAdI: MDGIMG → Rule-Based Workflow → Business Add-Ins → **Handling of Parallel Results in Rule-Based Workflow**: enhancement `ZEI_MDG_MATCH...`, class `ZCL_MDG_MATCH`-style; filter value = the service name (must be maintained first, activation fails without it).
- Merge code signature `IT_STEP_ACTION` / `EV_MERGE_ACTION`: loop actions → any **04 (reject)** sets merge action 04 and `RETURN` immediately; otherwise **03 (approve)**; the returned action drives step 30 onward (approve → Act → 99 approved; reject → rollback → 95 → 99 rejected, staging data deleted).
**Key insight:** approval is only reached after **all three** work items are decided — that is why the merge BAdI must return reject as soon as it sees one reject; also the whole thing cannot be tested until the merge BAdI exists, the BRF+ table validates but the workflow stops at merge time.
**Prereq:** CR type copy + BRF+ USMD_SSW_RULE basics; three test users; activation/rollback step types understood.
**Workflow concept covered:** parallel workitems with 3 agent groups, merge (match) BAdI decision, rollback and activation-failure branches.

### 7. Skipping approver step if approver is requestor in SAP MDG
**ID:** [pGaG2Ky5_OQ](https://youtu.be/pGaG2Ky5_OQ) | **Length:** 40m | **Level:** advanced

**In one line:** When the requester is also in the level-1 role, the whole level is skipped via the **dynamic agent selection** BAdI so the CR jumps straight to level 2.
- Setup: role `ZC_MDG_TEST` = level 1 (users S4_MDG7 + ZS4_MDG71), `ZC_MDG_TEST1` = level 2 (ZS4_MDG71 only, has Activate/Reject; level 2 status showed as "Final check to be performed").
- MDGIMG → Define Service Names for Rule-Based Workflow → `Z_SKIP_GLOBAL_SPECIALIST`, description "to skip global specialist if requester is also global specialist"; then put that service into the BRF+ decision table's **dynamic agent selection** column (first restore the hidden dynamic columns), save + activate.
- BAdI: Rule-Based Workflow → Business Add-Ins → **Dynamic Agent Selection in Rule-Based Workflow**: enhancement `ZEI_SKIP_GLOBAL_SPECIALIST`, class `ZCL_SKIP_GLOBAL_SPECIALIST`, filter *service = Z_SKIP_GLOBAL_SPECIALIST*; must first generate/implement the empty interface method in SE24 and activate the class, otherwise the BAdI shows "not implemented".
- Code on changing parameter `CT_USER_AGENT_GROUP`: loop groups → inner loop `USER_AGENT`; where `USER_TYPE = 'AG'` (role), call FM **RSRA_USERS_OF_AGR_GET** (role → users, time-dependent) into table type **AGR_USERS**; compare UNAME with the CR creator read via `SELECT SINGLE USMD_CREQUEST_CREATED_BY ... FROM ... ESMD120C WHERE usmd_crequest = lv_cr_number`.
- On match: FREE ct_user_agent_group, rebuild the row with step type 8 / agent group 000 and user agent type **AG**, user value `ZC_MDG_TEST1` (append to `LT_USER_AGENT_GROUP`, then assign back), and also set `CV_NEW_CR_STATUS = '00'` and `CV_NEW_CR_STEP = '10'` — forgetting these two leaves the CR on the old step.
**Key insight:** pass only the **first 30 characters** of the role name (USER_VALUE is 100 chars long) to RSRA_USERS_OF_AGR_GET or the call dumps; and you cannot FREE/MODIFY the table you are looping over — copy to a local table first.
**Prereq:** two-level rule-based workflow with role-based agents; PFCG role/user knowledge.
**Workflow concept covered:** dynamic agent selection BAdI used to skip an approval level when the requester is in the approver role.

### 8. Eliminating requestor from approver levels in SAP MDG
**ID:** [Kxbryjx6opo](https://youtu.be/Kxbryjx6opo) | **Length:** 41m | **Level:** advanced

**In one line:** Instead of skipping a level, it strips the requester out of the level-1 role and re-writes the agent as explicit users, so only the remaining users see the work item.
- Requirement demo: user S4_MDG7 is both requester and member of role `ZC_MDG_TEST`; rule = "anyone who requests a CR must not process any further step", so the CR must route only to ZS4_MDG71.
- BAdI choice: Rule-Based Workflow → Business Add-Ins → the **general BAdI that executes at every step** ("MDG user determination"), enhancement `ZEI_MDG_USER_DETERMINATION`, impl `ZBI_REQUESTER_EXCLUDE`, class `ZCL_REQUESTER_EXCLUDE`.
- Filter values must pin both dimensions: **CR type = Z_CUSTOM_P1** and **model = BP** (comparator `=`), so the code needs no CASE/IF on CR type.
- Inside the loop over `CT_USER_AGENT_GROUP`: where `USER_TYPE = 'AG'`, call FM **RSRA_USERS_OF_AGR_GET** (time-dependent) into `AGR_USERS`; `continue` when `UNAME = LV_CREATED_BY` (requester read with `SELECT SINGLE ... USMD_CREQUEST_CREATED_BY ... esmd120c WHERE usmd_crequest = iv_cr_number`).
- Then **convert the role agent into single users**: build `LS_USER_AGENT` rows with user type **US** and user value = each remaining user ID into a `USMD_TS_USER_AGENT`-style table, append into the group's USER_AGENT, and append the group back — instead of leaving one AG/role entry.
**Key insight:** the role must be exploded into US entries, otherwise deleting one UNAME does nothing (BRF+ still resolves the whole role). Also never FREE/MODIFY the internal table you are inside — doing so dumped; move the assignment outside the loop, verified by debugging the class from **SM50**.
**Prereq:** the parallel/level workflow with role-based agents; PFCG + AGR_USERS knowledge.
**Workflow concept covered:** requestor exclusion from role-based agent determination (role → user conversion).

### 9. Instant rejection from parallel workitems in workflow
**ID:** [F_d7f-gcgAA](https://youtu.be/F_d7f-gcgAA) | **Length:** 43m | **Level:** advanced

**In one line:** Fixes the "reject one, wait for the others" flaw of parallel approval by closing every sibling work item and sub-workflow programmatically the moment one approver rejects.
- Workflow hierarchy first: SWIA shows the requester's **top/main work item** (type W = workflow), each parallel branch is a **sub-workflow work item (W)**, and inside it **dialog items (F)** for each approver; background steps show as type **B**.
- Top work item lookup in SE24: class **CL_USMD_WORKFLOW_CREQUEST_MAPPER**, method *get work item by CR (single)* → returns the parent work item ID for a CR number (427333 for CR 877) — no table digging needed.
- FMs: **SAP_WAPI_GET_DEPENDENT_WORK_ITEMS** (input work item ID; result rows type **SWR_WIHDR** with WI_ID, WI_TYPE, status text) and **SAP_WAPI_WORKITEM_COMPLETE** (only WI_ID mandatory) to finish each item.
- BRF+ changes: new service `Z_MDG_CUSTOMER_PARALLEL_REJECT` in Define Service Names; split reject from approve into its own row (duplicate row, remove approve/reject from each), new condition alias **REJ**, previous step 60 → new CR step 60, then a **99** row, plus parent step 20; agent REJ = agent group 1, process pattern 2, service `Z_MDG_CUSTOMER_PARALLEL_REJECT`.
- BAdI "calling of system method for rule-based workflow": enhancement `ZEI_MDG_...`, class `ZCL_MDG_SYNC_SYSTEM_METHOD`-style, filter = the reject service; code: get top work item → get dependent items → loop → if `WI_TYPE = 'W'` (or `'F'`) and status text = READY (also "in process") → `SAP_WAPI_WORKITEM_COMPLETE( wi_id = ls_items-wi_id )`; closing the sub-workflows fires the **merge (match) BAdI**, which carries the reject decision and closes the CR.
**Key insight:** you must close the sub-workflow items, not just the dialog items — otherwise the merge BAdI never runs and the CR hangs; and status text is compared as text ("READY"), so both dialog and workflow types need the check.
**Prereq:** a working 3-approver parallel workflow with merge BAdI and BRF+ step table.
**Workflow concept covered:** parallel work items + instant rejection (programmatic closing of sibling work items).

### 10. Email notifications in workflows in MDG using SO10 template
**ID:** [QeKQaB19vpo](https://youtu.be/QeKQaB19vpo) | **Length:** 50m | **Level:** advanced

**In one line:** Builds a "mail requester after activation" step from scratch — service name, synchronous-system-method BAdI, SO10 HTML template, CL_BCS_MESSAGE send — and verifies it in SOST.
- `USMD_SSW_RULE` (or MDGIMG → Process Modeling → Change Requests → Rule-Based Workflow → Configure Rule-Based Workflow) for CR type `Z_CUSTOM_P1`: duplicate the post-activation row, insert a new CR step before **CMP** (completion), agent `EAA`, description "email after activation".
- MDGIMG → **Define Service Names for Rule-Based Workflow** → `Z_EMAIL_TO_REQUESTER`; agent group 0, process pattern **2 = synchronous system method**.
- BAdI: Rule-Based Workflow → Business Add-Ins → the 5 workflow BAdIs → **synchronous system method** one: enhancement `ZEI_...`, impl `ZBI_SEND_EMAIL_TO_REQUESTER`, class `ZCL_SEND_EMAIL_TO_REQUESTER` (local object), filter *service name = Z_EMAIL_TO_REQUESTER, comparator =*.
- **SO10** standard texts `Z_EMAIL_TO_REQUESTER` (body) and a subject text, object `TEXT`, text ID `ST`, language EN — body written with **`<BR>`** breaks because the mail is sent as document type **HTM**; the Word/SAPscript editor line breaks are lost (proved by running FM **READ_TEXT** and seeing the text collapse).
- ABAP: `CL_USMD_MODEL_EXT=>GET_INSTANCE( 'BP' )` → read char values of the CR into a `USMD_TS_SEL` selection (sign I, option EQ, low = CR number) → BP number from the entity row; `READ_TEXT` + `DESCRIBE TABLE ... LINES` loop + `CONCATENATE` into one string; `CL_BCS_MESSAGE` object → `SET_SUBJECT`, `SET_MAIN_DOCUMENT` (type HTM), `ADD_RECIPIENT`, `SET_SEND_IMMEDIATELY( ABAP_TRUE )`, `SEND` in TRY/CATCH; `REPLACE ALL OCCURRENCES OF` for `&customer number` / `&req`.
**Key insight:** recipient is derived from the CR header creator (`USMD_CREQUEST_CREATED_BY` / created-by in the CR table) and then **BAPI_USER_GET_DETAIL** with its RETURN structure — you must pass the RETURN type or the call dumps; debug with an **external breakpoint under user WF-BATCH**.
**Prereq:** rule-based workflow with an activation step and a completion (CMP) row; SOST access to verify.
**Workflow concept covered:** post-activation background step via synchronous system method BAdI (mail on activation).

### 11. Creation of follow-up CR for BP
**ID:** [pD6rWraKtlE](https://youtu.be/pD6rWraKtlE) | **Length:** 41m | **Level:** advanced

**In one line:** Creates a follow-up change request automatically just before the main CR completes, using CL_USMD_CREQUEST_API create-by-reference plus convenience API object-list copying.
- Baseline flow: requester S4_MDG7 → role `ZC_MDG_TEST1` (PFCG check) → level 1 check → "Final check to be performed" → **95** activation → **99**.
- `USMD_SSW_RULE` / MDGIMG rule-based workflow: add service `Z_FOLLOWUPS` in **Define Service Names**, insert new step **98** (status 02) right after activation-success row, set the `$` (completion) symbol on it, keep 99/05 rows, agent `Z_FOLLOWUPS` = process pattern 2 (synchronous system method).
- BAdI "calling of system method for rule-based workflow": enhancement `ZEI_CREATE_FOLLOWUPS`, impl `ZBI_CREATE_FOLLOWUP`, class `ZCL_CREATE_FOLLOWUP_CR`, filter service `Z_FOLLOWUP_CR`.
- ABAP: `CL_USMD_CREQUEST_API=>GET_INSTANCE` (do **not** pass a CR ID, model = BP / GP_BP_MODEL) → `CREATE_CREQUEST_BY_REFERENCE` with `IV_CREQUEST_TYPE` = follow-up type, `IV_ATTRIBUTES` empty (`USMD_TS_FIELD_NAME`), attachments/notes ABAP_FALSE → `EV_CREQUEST` = new CR ID; read source objects with `CL_USMD_CONV_SOM_GOV_API=>GET_INSTANCE( 'BP' )→GET_OBJECT_LIST`, loop, `ENTITY = BP_HEADER`, `ASSIGN COMPONENT ... STRUCTURE` → `LV_BP_HEADER` type `BU_PARTNER`.
- Attach to the new CR: `crequest_api->ADD_OBJECT_LIST` with table type `USMD_TS_CREQUEST_ENTITY` (USMD_CREQUEST, USMD_ENTITY (must be a USMD_ENTITY value, not a field name), sequence 1, USMD_VALUE = BP number), then `ENQUEUE`/`DEQUEUE`, `WRITE_VALUE` (field name `GP_BP_HEADER`-style constant) with the generated **/MDG/BP_PP_CORE...** mapping structure, and save.
**Key insight:** `ADD_OBJECT_LIST` rejects a field-name string — passing `GC_FIELD...` gives a type error; you must pass the model entity constant. Second gotcha: `SM12` lock leftovers block the workflow edit ("just delete the lock"), and the new CR appears in the original CR only as an out-of-the-box **follow-up hyperlink** (276 → 277) once the API save succeeds.
**Prereq:** rule-based workflow with activation-success/CMP rows + ABAP knowledge of the MDG CR APIs.
**Workflow concept covered:** follow-up CR creation from a workflow background step (create-by-reference).

**Checkpoint:** build your own CR type with 3-step approval (level 1 parallel, level 2 single), force the requester out of an approver level, and make one field block submission until filled. That combination is exactly the interview-level scenario.

---


## Phase 4 - Validations and Derivations

**13 videos · 5h54m**

Deliberate order: BRF+ (config, no ABAP) -> calling BRF+ from ABAP -> rule context BAdI -> simple BAdI -> dynamic BAdI -> cross-entity -> DQM three-parter -> DQM formulas.

Do not start with BAdI. The BAdI videos assume you already know how a rule is triggered, what the rule context provides, and what MDG does when a validation returns an error. The DQM series likewise assumes BRF+ fluency - its conditions are BRF+ conditions.


### 1. Validation and derivations in BRF+ in SAP MDG
**ID:** [3yeb0Xadj9Y](https://youtu.be/3yeb0Xadj9Y) | **Length:** 31m | **Level:** intermediate

**In one line:** Build a BRF+ validation (make organization name mandatory) and a BRF+ derivation (copy name1 into search term 1) that fire only for one change request type.
- Reached via MDGIMG → General Settings → **Data Quality and Search → Validations and Enrichments** (or the direct tcode he prefers instead of MDGIMG); choose data model **BP** → continue → **Open Trigger Function**; the catalog has a `Check Entity` branch (validations) and a `Derivation` branch.
- **Naming convention is law:** function must be `CHECK_<entity name>` for validations and `DERIVE_<entity name>` for derivations, entity name exact (org name1 lives in entity `BP_CENTRAL`, attribute `MC_NAME1`/name1). "If you don't give the entity name here it doesn't get triggered and doesn't work at all."
- Add data objects via *Add Existing Data Object*: the entity's central-data structure (BP central data) **plus** the change-request data objects (change request index / step / process) — the CR objects are what put the change request type into the context.
- Rule set `RS_CHECK_NAME1`, rule "make name of our organization mandatory": condition (AND) `BP_CENTRAL–FIRST_ORG_NAME is initial` + `change request type = ZCUSTOM_P2` → action `LOG_NAME1_MANDATORY`, action type **log message**, message type **Error** (SAP's default message is an information message, which users can bypass), text "Name of organization should be filled".
- Derivation: function `DERIVE_BP_CENTRAL`, rule set `RS_DERIVE_SEARCHTERM`, condition `CR type = ZCUSTOM_P2` AND name1 not initial → then `SEARCHTERM1 = name1`. The derive function must also be **assigned under the Derivation folder** of the trigger function.
**Key insight:** if you hit Cancel while assigning a new function node the first time, the object stays created but unassigned — you must go back and *Select existing object*; same symptom appears when a lock ("currently locked by me") blocks the assignment. Delete your own locks and re-assign, then refresh (green = active).
**Prereq:** the entity/attribute must already exist in the BP data model, and you must know the CR type to restrict to.

### 2. DB lookup validations in MDG BRF
**ID:** [8eP3QOnXh6Q](https://youtu.be/8eP3QOnXh6Q) | **Length:** 16m | **Level:** intermediate

**In one line:** OVS accepts any hand-typed value, so add a BRF+ database-lookup existence check that rejects values not present in the custom table.
- Problem shown first: field `ZZROUTER` has an OVS search help backed by custom table `ZT_MDG_ROUTERS`, but typing "Arabia" and pressing Check passes — OVS only constrains the picker.
- BRF+ app BP → Open Trigger Function → `Check Entity` → object node → new function (validation), add the custom entity's data object (entity `ZCUSTOM`) via *Add Existing Data Object*; no CR-type component needed (must work for every CR type).
- Rule set `RS_CHECK_ZZROUTER`; rule 1 = **exit condition** using the value range from context: if `ZCUSTOM-ZZROUTER` is initial, exit the rule set (so an empty field is never validated).
- Rule 2 = expression type **Database Lookup**, name `DL_ZZROUTER`: mode **"Existence check – at least one entry exists"** (not *data retriever*), table = the custom table, WHERE `ROUTER = context ZZROUTER`, returns a Boolean.
- Rule 2 THEN/ELSE: if the lookup is true do nothing (else branch), if false perform action `LOG_ZZROUTER` — log type **error**, text "router field you entered is invalid". Activate function + rule set, then test in NWBC: valid drop-down picks pass, "Arabia" errors on Check.
**Key insight:** rule order inside the rule set matters — drag the exit-condition rule to the top, otherwise the exit fires after the lookup has already been processed. A search help never validates; BRF+ DB lookup gives you the check without ABAP.
**Prereq:** custom table + populated OVS (see the OVS video).

### 3. How to create and execute BRF+ decision tables via ABAP
**ID:** [1_foYbVuKco](https://youtu.be/1_foYbVuKco) | **Length:** 28m | **Level:** intermediate

**In one line:** Build a BRF+ decision table (CR type + BP grouping → role) and call it from an ABAP report through a wrapper function and the generated code template.
- Why: business users have **Fiori-only** access (no GUI, no SM30), BRF+ is web-based, and every change is versioned (who/when, transport button, last-changed).
- Transactions **BRF+ / BRFPLUS** → create application `ZAPPLICATION` (storage type Customizing) in a transport → activate (green).
- Decision table `DT_SAMPLE_TABLE`: result data object `ROLE`, created as a BRF+ element with binding type **"bind to DDIC element" → `AGR_NAME`** (not "no binding"). Then *Table Settings* → insert columns from **context data objects**: `CR_TYPE` bound to DDIC element **`USMD_CREQUEST_TYPE`**, `BP_GROUP` bound to **`BU_GROUP`**. Columns cannot be created from inside the insert-column dialog — save, right-click, create the element first.
- Rows: ZCUST1P1 + BP01 → Z_TEST, BP02 → Z_BASIS_TEST, BP03 → Z_TEST_DEBUG, BP04 → Z_TEST_MODE (different results so you can prove it works).
- **A decision table cannot be called directly from ABAP** — wrap it: function `Z_FN_SAMPLE`, signature gets only the context objects (CR type, BP grouping — NOT role), then *Assign Rule Set* `RS_GET_ROLE`, insert rule with **no condition** (so it always executes) → *Process Expression* → select the decision table → *Add Variables to Rule Set* so `ROLE` becomes the result. In the function, move ROLE into **Result/Actions**, not context.
- Personalize → switch user mode **Simple → Expert** (required to expose *Create Code Template*), then Code Template → Apply → copy the whole generated snippet into a SE38 report; fill the context values (`LV_CR_TYPE`, `LV_BP_GROUP` — element text is a string type), `EXPORTING lt_name_value`, `IMPORTING`. Unknown/invalid combination returns an empty result, no error.
**Key insight:** the wrapper function is mandatory (BRF+ objects are not ABAP-callable), and Expert mode is the gate for the code template — without it the effort is all hand-written BRF+ API code.
**Prereq:** DDIC data elements for the columns (AGR_NAME, USMD_CREQUEST_TYPE, BU_GROUP) and a transport for the BRF+ application.

### 4. Rule context badi in MDG, debugging and issue resolving
**ID:** [FsYJYx7x7r0](https://youtu.be/FsYJYx7x7r0) | **Length:** 52m | **Level:** advanced

**In one line:** Makes a BRF+ decision table branch on a brand-new field (account group) by implementing the **rule context preparation** BAdI, then debug/fix the assertion dump it causes after activation.
- BRF+ (`USMD_SSW_RULE`) → create data object → **create element** `ACC_GRP`, binding type *bind to DDIC element* = **BU_GROUP** (gives F4 help), activate, then add it to the trigger/context structure via *Add existing data object*.
- Decision table (single evaluation table) → edit mode → Table Settings → **insert column → from context data objects** → ACC_GRP as condition column; rows `B001` → role `ZC_MDG_TEST1`, `<> B001` → other role; expression view: destination-table "min columns for horizontal scrollbar" changed from 55 to 6 so all six columns are visible.
- New conditional alias (`&`) in the user-agent part of the table: agent group 000, step type 8, user agent type **AG**, user agent value `ZC_MDG_TEST`.
- BAdI: MDGIMG → Process Modeling → Workflow → Rule-Based Workflow → **Business Add-Ins → Rule Context Preparation** (1st of the 5 workflow BAdIs): enhancement `ZEI_...`, impl `ZBI_ACC_GROUP_ROUTER`, class `ZCL_ACC_GROUP_ROUTER`, created from **copy sample class** (sample is material-based: delete unused methods, swap data model "MM" → "BP").
- Class work: `GET_ELEMENT_ID` takes the context element name (ACC_GRP) and returns the runtime unique ID (verified in BRF+ as 5-hour-36-dB style ID); new `READ_ACCOUNT_GROUP` reads the CR's **BP_HEADER** field **BU_GROUP** (type BU_GROUP, not material) and fills `ET_RULE_CONTEXT-VALUE`; filter value must equal the service name `MDG CUSTOM P1 SERVICE`, comparator `=`.
- Debug: SM50 → *active workflows only* → Administration → Program → Debugging with a `DO ... ENDDO` breakpoint; work item 397275 processed in SWIA "without check".
**Key insight:** the rule-context BAdI also runs once more **after activation** with an empty context — the sample code's `ASSERT` and unguarded read then dump in **ST22** ("assert size" in read method) and the workflow log shows *Error in agent root finder*. Fix: delete the ASSERT, wrap the read in `IF lv_acc_group IS NOT INITIAL` / `IF lt_data IS NOT INITIAL`; a wrong rule-context field name produces the same *agent root finder* error at submit time.
**Prereq:** working rule-based workflow decision table + BRF+ access; ABAP debugging of background/`sm50` jobs.
**Workflow concept covered:** rule context BAdI feeding a new field into BRF+ context for account-group based routing.

### 5. Validations and derivations using Badi - Simple
**ID:** [Ll6eQ76z8s0](https://youtu.be/Ll6eQ76z8s0) | **Length:** 33m | **Level:** intermediate

**In one line:** The minimal BAdI round trip: create an enhancement + implementation on the rule-service BAdI, set filter values, activate all methods, then use `check_entity` for "BP grouping is mandatory" and `derive_entity` to default country `US`.
- Entry point: MDGIMG → General Settings → **Data Quality** — inside it, the "Validations and Enrichments" node is the **BRF+** one and must not be used; the BAdI path is the **Business Add-Ins** node. Before creating anything, check that no existing implementation already has the same filter criteria (only one implementation per filter combination wins).
- Objects created: enhancement `ZEI_MDG_VALIDATION_DERIVATION` ("enhancement for validations and derivations for customer"), implementation `ZBI_MDG_…`, implementing class; BAdI name/class had to be typed manually the first time (not in the F4 dropdown). Reuse the BAdI for a custom CR type `Z_CUST…P2`.
- Filter values: `USMD_MODEL = BP` (always, it is the BP data model) and `USMD_ENTITY = BP_HEADER` — the entity is derived from MDGIMG → Data Modeling → **Visualize data model**, where `BU_GROUP` visibly sits in BP header. Comparator "equal to". Then open the class and **activate every interface method once (empty)** or nothing fires.
- Only two methods matter: `CHECK_ENTITY` (validations) and `DERIVE_ENTITY` (derivations). Debug tip from the video: put a breakpoint, press Check — nothing happens; you must leave the app and re-enter the CR (Create Organization), then check again after entering the description. In the debugger you see `ID_DATA` with the temporary BP number, BP type 2 (organization) and an empty `BU_GROUP`.
- `check_entity` body: `IF id_entity_type = BP_HEADER` → `LOOP AT id_data ASSIGNING FIELD-SYMBOL(<fs_ls_data>)` → `ASSIGN COMPONENT 'bu_group' OF STRUCTURE <fs_ls_data> TO <fs_bu_group>` → `IF IS ASSIGNED AND IS INITIAL` → append a message to `ET_MESSAGE`. Message is built without `SE91` by filling the `USMD_S_MESSAGE`/`USMDT_MESSAGE` line (message class/text, message type `E`) — the author notes that when the parameter is `RECEIVING` you can append the returned structure directly instead of passing it back.
- `derive_entity` body: CR type from `CL_USMD_CREQUEST_UTIL=>GET_TYPE_BY_CREQUEST( id_crequest = … io_model = … )` (avoids reading `USMD_…` tables and needing architect approval), or `CL_USMD_CREQUEST_APP_CONTEXT=>GET_INSTANCE( ) → GET_ATTRIBUTES( )`; `IF lv_crequest_type = 'Z_CUST…P2'` → `LOOP AT ct_data ASSIGNING <fs>` → `ASSIGN COMPONENT 'REF_POSTL'` (country key, entity `AD_POSTAL`) → if initial set `'US'`. A **combination filter** (`BP_HEADER` + `AD_POSTAL`) must be added in the BAdI filter for this to trigger.
- Verified behaviour: "BP grouping is mandatory" clears as soon as a grouping is typed; `US` appears in the postal country as soon as any field of that entity is touched.
**Key insight:** `DERIVE_ENTITY` runs **before** validation, and it only re-fires when a field of a filtered entity changes — so "derive a default on CR open" is not achievable in this simple BAdI; that limitation is exactly what drives the next video (cross-entity derivation, highest priority). Also: the BRF+ node and the BAdI node in the same IMG folder are two different mechanisms — picking the wrong one is the most common beginner mistake.
**Prereq:** Knowing the data model well enough to say which entity owns the field (visualise data model), plus ABAP basics (`ASSIGN COMPONENT`, field symbols) and the CR type you want to filter.

### 6. Dynamic Validations and derivations using badi
**ID:** [StXYbdnRzQk](https://youtu.be/StXYbdnRzQk) | **Length:** 52m | **Level:** advanced

**In one line:** Four dynamic rules in one BAdI implementation — BP grouping mandatory, then properties that depend on the grouping value (name1 mandatory, title mandatory) plus upper-casing name1 — done in `check_entity` and `derive_entity`.
- Requirements set up front: (1) `BU_GROUP` mandatory on BP header; (2) if grouping = internal number assignment (`3000`) → `NAME1` in BP central mandatory; (3) if grouping `3000` → `TITLE` mandatory; (4) `NAME1` always converted to capitals on Enter — the author's point is that uppercasing is **not possible in BRF+**, only in the BAdI. Note the built-in cross-entity flavour: `BU_GROUP` is BP header, `NAME1`/`TITLE` are BP central.
- Entity names are never hard-coded: `ID_ENTITY_TYPE = IF_MDG_BP_CONSTANTS=>GC_BP_MODEL_ENTITY-BP_HEADER` (and `-BP_CENTRAL`), checked by browsing the constants interface in SE24/SE11. Data is structure-agnostic, so `LOOP AT ID_DATA ASSIGNING FIELD-SYMBOL(<ls_data>)` + `ASSIGN COMPONENT 'BU_GROUP' OF STRUCTURE <ls_data>` (and `NAME_ORG1`, `TITLE_BP` for BP central); always `IS ASSIGNED` before reading, then `IS INITIAL`.
- Grouping values are found in customizing, not guessed: SPRO → SAP Reference IMG → Cross-Application Components → SAP Business Partner → Business Partner Basic Settings → Number Ranges → **Define Groupings and Number Ranges** → "internal number assignment" = `3000`; a second grouping used in the code is `2019`. Also useful: MDGIMG → Data Modeling → Edit Data Model → **Visualize data model** to confirm which entity owns `BU_GROUP`.
- BP central values are read with `IO_MODEL->READ_ENTITY_DATA_ALL( IV_ENTITY = type-1 entity BP_HEADER, IT_SEL = USMD_TS_SEL, IF_ACTIVE = '' , IO_CREQUEST = ... )`; the result `ET_DATA_ENTITY` (`USMD_SX_DATA_ENTITY`, entity + `USMD_CONT`) is reduced with `READ TABLE ... WITH KEY USMD_ENTITY = BP_HEADER` and `STRUCTURE = KATTR` (key-attribute structure), then `ASSIGN <ls_data_entity>->*DATA TO <lt_rt_data>` (dereference `TYPE REF TO DATA`, guard with `IS ASSIGNED` / `SY-SUBRC`) before looping.
- Messages: `CL_USMD_MESSAGE` → `CONVERT_TEXT_TO_MESSAGE` with text symbols `001` "business partner grouping is mandatory", `002` name of organization mandatory, `003` title mandatory; `CONV #( TEXT-001 )` needed where the text is a string but the field is `USMD_S_MESSAGE`-typed; append to `ET_MESSAGE` (type `USMD_T_MESSAGE`, message type `E`) — no `SE91` message class needed.
- Derivation: in `derive_entity`, `LOOP AT CT_DATA ASSIGNING FIELD-SYMBOL(<ls>)` and `TRANSLATE <lv_name_org1> TO UPPERCASE`. Because the field symbol points into `CT_DATA`, writing through it pushes the value back to the UI — but only if you loop `ASSIGNING` (changing), never `INTO`.
**Key insight:** All four rules are "dynamic" only because they read the *current* CR data at runtime; the technical split is fixed — `check_entity` for messages, `derive_entity` for changing data, and the assignment must go through field symbols into the `CT_DATA`/`ID_DATA` references or the change is lost. Expect several runtime errors the first time: unassigned field symbols and `READ ENTITY DATA ALL` with the wrong entity filter (the author fixes a filter left on `AD_POSTAL` to `BP_CENTRAL` mid-video).
**Prereq:** Basic BAdI implementation setup (video "Validations and derivations using Badi - Simple"), knowledge of MDG data model visualisation, and ABAP field symbols / `ASSIGN COMPONENT`.

### 7. Cross entity derivations in SAP MDG
**ID:** [jXCGbu5jSxE](https://youtu.be/jXCGbu5jSxE) | **Length:** 37m | **Level:** advanced

**In one line:** Implements the cross-entity BAdI (`USMD_RULE_SERVICE`) to default roles `FLCU01` and `FLCU02` on CR open, by reading BP header with `read_data` and writing BP role rows with `write_data`.
- Where: navigate from MDGIMG → Data Quality, or go straight to BAdI **`USMD_RULE_SERVICE`** (SE19). "Create new implementation" → enhancement "cross entity derivations for BP", implementation `ZBI_MDG_CROSS_DERIVATION`, new class `ZCL_MDG_CROSS_DERIVATION`; filter value `USMD_MODEL = BP`.
- Interface parameters are all `TYPE REF TO`: `IO_MODEL`, `IO_CHANGE_DATA` (read), `IO_WRITE_DATA` (write), `IO_READ_DATA`. The important one is `WRITE_DATA`; read the CR staging area with `IO_CHANGE_DATA->READ_DATA( … )` or `IO_MODEL->READ_ENTITY_DATA_ALL`.
- **Errors cannot be raised here** — the author states that messages sent from a cross-entity derivation are downgraded to warnings, so this BAdI is for derivation only, never validation.
- Code shape: CR type via `CL_USMD_APP_CONTEXT=>GET_INSTANCE( ) → GET_ATTRIBUTES( )` → `IF lv_crequest_type = 'Z_CUST…P2'`; `io_change_data->read_data( entity = 'BP_HEADER', data_mode = … )` returns a `REF TO DATA`, so the target must be `DATA lr_data TYPE REF TO data` (a field symbol on the left of the dereference dumps) then `<lt_data_mod>` after dereferencing; `ASSIGN COMPONENT 'BP_HEADER' OF STRUCTURE <lt_data_mod> TO <lv_bp_header>`; move to a real `BU_PARTNER` variable.
- Write: fill a work area typed with the **generated BP role structure** (copied from MDGIMG generated structures / PP mapping via SE11, name ending `…BPOR`), set `BP_HEADER = lv_bp_header` and `BP_RO_ID = 'FLCU01'`, append, repeat for `FLCU02` (reusing the same work area), then `io_write_data->write_data( entity = 'BP_RO', it_data = lt_bp_ro )` inside `TRY … CATCH … ENDTRY` — the try/catch is called "extremely mandatory".
- Guard for contact persons: instead of blindly using BP header, `ASSIGN COMPONENT 'BU_GROUP'` and only continue when `BU_GROUP = 2` (organization). Otherwise every contact person created under the organization also gets the customer roles.
- Debugging narrative: the author hits an unassigned field symbol first, then realises that `READ_ENTITY_DATA_ALL` cannot see the BP header because it is still only in the buffer, and switches to `io_change_data->read_data` — "exactly the same code doesn't work every time".
**Key insight:** In a cross-entity derivation the BP header is only in the **write buffer** at CR-open time, so `IO_MODEL->READ_ENTITY_DATA_ALL` returns nothing and `IO_CHANGE_DATA->READ_DATA` must be used. And because errors become warnings, cross-entity derivation can never replace a validation — pair it with a `check_entity`/DQM rule if the value is mandatory.
**Prereq:** Simple BAdI video (enhancement + filter values + `ASSIGN COMPONENT` habits), plus understanding that BP role is a separate entity whose key is BP header + role ID.

### 8. Adding attributes for copy scenarios in BP
**ID:** [4LzcirabqXo](https://youtu.be/4LzcirabqXo) | **Length:** 7m | **Level:** intermediate

**In one line:** Fixes "my custom ERP customer attributes are not copied" by adding them to the entity cloner's confine-attributes list through an implicit enhancement.
- Symptom: copying an existing BP (with ERP customer data) into a new CR copies everything except **`KATR1`** and `KATR2` (customer attribute 1/2) under ERP customer → Additional Data, even though nothing custom was implemented.
- Cause: SAP's copy scenario is driven by **entity cloner** classes (three of them exist for BP-type objects: one for business partner data, one for customer/supplier data — the caption garbles the exact class names, e.g. "BSBP…" and "CUST…entity cloner"). Attributes in ERP customer must be handled by the customer/supplier cloner, so that is the class opened in SE24.
- Inside the cloner, the method that decides what is copied maintains two lists: **confine attributes (include)** and **exclude/ignore attributes**. SAP has already hard-coded entries there (e.g. the general data entity included, company codes excluded); custom attributes are simply absent from the confine list, which is why they are dropped.
- Fix without modifying SAP code: open the method → `Edit → Enhancement → Show Implicit Enhancement Options` → `Enhance` → `Create`, name `Z…` enhancement with short text "customer attribute 1", then in the enhancement block append `KATR1` to the confine list for the ERP customer entity (copy the pattern of the existing lines) → activate.
- Verify: re-run copy into a new CR type; ERP customer now shows customer attribute 1 populated, while attribute 2 remains uncopied until the same enhancement is extended for it.
**Key insight:** Copy behaviour is not in the CR type or the data model — it lives in a generated-ish cloner method, and the only supported change point is an implicit enhancement inside it. There are separate cloners per object family, so the attribute's **entity** (here ERP customer, i.e. customer general/additional data) decides which cloner you must enhance.
**Prereq:** Know where the attribute lives (entity + "Additional Data" group) and be comfortable with implicit enhancements in SE24 methods.

### 9. Simple validations in DQM (DQM Series - Part 1)
**ID:** [-27cR_d459o](https://youtu.be/-27cR_d459o) | **Length:** 20m | **Level:** beginner

**In one line:** Builds one DQM data-quality rule (salutation mandatory) end-to-end: rule header, usage, scope expression, condition expression, approval workflow, and the MDGIMG switch that makes DQM messages appear on the floorplan.
- Why DQM exists: today a validation can sit in BRF+ for same-entity, in the `check entity` BAdI, or in a cross-entity BAdI — three different places, and BAdI ones need code. DQM centralises all rules in one catalog, introduced with S/4HANA 2020; 2021 split "business rules" into separate validation and derivation sections (the demo system is pre-2021, so only business rules show).
- Scope: DQM tiles exist only for **business partner and material** — not finance, not custom data models. Tiles: Data Quality Rules Management, Rule Mining Process, Rules from Rule Mining, Data Quality Evaluation, Evaluation Results (`/n/ui2/flp` Fiori launchpad, "Data Quality Management for Business Partners").
- Create rule: any naming convention (no `USMD_RULE` style enforced); **Rule name = the message the user sees when the rule fails**; **base table = `B0` (BP general data)**, salutation field = `TITLE`; **"checked field" = the field that gets the red border** (an advantage over plain BRF+, which shows the message but no red field). Business description / business reason / contact person are all optional free text.
- Usages: `ADD` → "Check in Change Request" (the consolidation variant is the other option) → **Prepare** → base table → the framework then generates `SCOPE_EXPRESSION` and `CONDITION_EXPRESSION`. Scope = broad applicability (e.g. `true = true` so it fires for every record, non-archived only); condition = the actual check, built by replacing the SAP-delivered operand with `EDIT` → Direct Value → context field `TITLE`.
- Condition logic is inverted: the expression must evaluate **false** to raise the error. For "salutation must be filled" the condition is `TITLE is not initial`, so an empty field returns false → message fires.
- Release path: `New` → `Send for implementation` (to be implemented) → `Send for testing` (to be tested) → `Approve` → `Enable`. Rule cannot be enabled before it is approved; the usage row must be enabled separately.
- MDGIMG one-time switch: in the change request **step** (requester step, e.g. `00`) → **Enhancements → checkbox "Relevant for [Data Quality Management]"** must be ticked and saved, otherwise the framework messages never reach the frontend. Then `Check` on Create Customer shows the new line "salutation is mandatory for customer or supplier"; **Display help** reveals the source as "MDQ data quality rule …".
**Key insight:** The rule, the expression, the approval state and the CR-step "relevant" flag are four separate switches — missing the IMG checkbox is the classic silent failure where the rule works in DQM but nothing appears in the UI.
**Prereq:** none (but you must know BP entity types / the CR type you are testing on).

**Series order note:** Part 1 gives the complete DQM skeleton — rule header (rule ID, rule name = UI message, base table, checked field), usage in a change request, scope vs condition expression, the approve/enable workflow, and the IMG "relevant for DQM" flag. Part 2 and Part 3 never repeat any of that: they only swap what goes into the condition expression (two attributes of one entity in Part 2, a BRF+ procedure call into ABAP in Part 3). So Part 1 is the prerequisite for both, and Part 3 is Part 1 + Part 2 + a static ABAP method.

### 10. Single entity validations in DQM (DQM Series - Part 2)
**ID:** [-H4fi9dZxAc](https://youtu.be/-H4fi9dZxAc) | **Length:** 10m | **Level:** beginner

**In one line:** Second DQM rule that compares two attributes of the same entity (salutation vs. name1) by making the condition return false when they are equal.
- Requirement: if `SALUTATION` contains the same text as `NAME1`, the check must fail ("Salutation should not be same as name one"). Same skeleton as Part 1: rule ID `CHECK_EQUAL_NAME1_SALUTATION`, rule name = message, base table `B0`, checked field = `NAME1` (so the red border lands on name1).
- Hard limit met while typing the rule ID: **rule ID accepts max 26 characters including spaces** — the field rejects anything longer, so plan short IDs.
- Usage → "Check in Change Request" → Prepare → scope expression set to `true = true` (all records), then condition built with `EDIT OPERAND` → Direct Value → context `SALUTATION`, operator **`is not equal to`**, second operand from "change context" → `NAME1`.
- Resulting behaviour in the UI: equal values → expression false → message; different values → true → silent. Verified by entering the same text in salutation and name1 and pressing Enter; both the DQM message and the standard MDG BRF+ validations fire in the same check.
**Key insight:** Everything in DQM is "false = error", so an equality check must be written as "is **not** equal to" — writing the natural `= ` flips the rule and it never fires. Also note the author's remark that same-entity comparisons are actually easier in plain BRF+ because both attributes sit in the same context; DQM's value here is the red field border and central catalog.
**Prereq:** Part 1 (rule creation, usage, scope/condition, approve+enable).

**Series order note:** (see Part 1) — Part 2 adds only the notion of a two-operand condition inside a single entity; it reuses Part 1's rule object, scope expression trick and release path unchanged.

### 11. Cross entity validations in DQM (DQM Series - Part 3)
**ID:** [cK_wysGWOT8](https://youtu.be/cK_wysGWOT8) | **Length:** 37m | **Level:** advanced

**In one line:** DQM rule whose condition calls a BRF+ "procedure call" into a static ABAP method that reads the BP header and BP roles of the change request, so a cross-entity check (role FLVN00 required for BP grouping S012) can be enforced with the DQM UI.
- Requirement: if BP grouping = "supplier hierarchy node", role `FLVN00` must exist on the BP. First step is finding the technical grouping ID behind the UI description — the description carries a digit; here it resolves to **`S012`**, found in the BP grouping customizing (`TBD00001`-style entry the author inspects in the backend).
- Rule: `CHECK_ROLE_FOR_BP_GROUP`, message "role FLVN00 is mandatory for this BP group", base table `BU20`/BP header level. This time the **scope expression is real**: `BUSINESS_PARTNER_GROUPING = S012`, so the rule does not even trigger for other groupings; the condition then does the role check.
- In the condition, instead of Direct Value: `CREATE EXPRESSION` → **Procedure Call** (`ZPS_CORE` / call name `READ_ROLES_FLVN00`), created via "Create and navigate to object". A **function call** would also work but needs a function group, so procedure call + static method is preferred. The method lives in a utility class `ZCL_BP_READ_UTILITY` (SE24, public static, "read utilities for validations in BP") so several checks can share one class.
- ABAP inside the method: `CL_USMD_APP_CONTEXT=>GET_INSTANCE( )` → `GET_ATTRIBUTES( )` → `IO_MODEL` + `C_REQUEST` id; `IO_MODEL->READ_CHAR_VALUE( )` twice — first with entity/type-1 BP header to obtain the **temporary BP number** (`USMD_VALUE`, moved to a 12-char `BU_PARTNER`), then with entity `BP_RO`; selection criteria as `USMD_TS_SEL` (`FIELDNAME = USMD_CREQUEST`, `SIGN = I`, `OPTION = EQ`), object list typed `USMD_S_CREQUEST_ENTITY`; `READ TABLE ... WITH KEY USMD_ENTITY = BP_HEADER`; role rows typed with the **generated MDG structure for BP role** (copied out of the generated structures / PP mapping in SE11, `...BPOR` suffix) because MDG generates these structures — a shortcut vs. dynamic `GET_DATA_REFERENCE`.
- BRF+ wiring gotcha: the method needs `RETURNING VALUE(RV_IS_ROLE_EXISTS) TYPE abap_bool`, that returning parameter must appear in the procedure call's **Mapped Parameters** and be assigned to the Boolean **result data object** — otherwise activation fails with "no result data object set". Loop roles, set `abap_true` if `BP_RO_ID = 'FLVN00'`, else final `abap_false`.
- Then approve → enable → test in Create Customer: pick grouping "supplier hierarchy node", the procedure call fires, no role rows → false → message; add FLVN00 → `READ_CHAR_VALUE` returns the row → true → message disappears while the other standard required fields still show.
**Key insight:** Cross-entity validation in DQM is **not possible without code** — the only no-code option is same-entity. The reusable contract is: BRF+ procedure call → static method → read the CR staging area through `IO_MODEL->READ_CHAR_VALUE` → return `abap_bool` → map it to the Boolean result object. True means "no error", so the return value is the positive condition, not the error.
**Prereq:** Part 1 and Part 2 (rule object, scope/condition, approve/enable) **plus** basic MDG ABAP: CL_USMD_APP_CONTEXT, IO_MODEL read methods, field symbols. Without the ABAP part this video cannot be reproduced.

**Series order note:** (see Part 1) — Part 3 builds directly on Part 1's rule lifecycle and Part 2's two-operand condition; what it adds is that the right-hand operand is no longer a context field but a program.

### 12. String functions in DQM Validations (No code)
**ID:** [WAVZTzNf2bI](https://youtu.be/WAVZTzNf2bI) | **Length:** 15m | **Level:** intermediate

**In one line:** Enforces a length limit on `SORT1` by building a BRF+ *formula* that calls the string-length function on a context attribute and feeding it into the DQM condition.
- Requirement: `SORT1` must not exceed 10 characters; the author stresses this class of requirement is done **entirely in BRF+ — no coding**.
- Rule: base table `BU20`, checked field `BU_SORT1` (optional but used), rule name "SORT1 should not exceed 10 characters"; create → usage "Check in Change Request" → `Prepare` → scope `true = true`.
- The core trick: in the condition, `CREATE EXPRESSION` → **Formula** (a formula instead of a plain operand) — this is the only place string operations are available. Inside the formula, `EXPRESSION → CREATE FORMULA`, then the function catalog filtered by category **String Functions** → `string length`; the cursor must be inside the brackets before inserting the context attribute `BU_SORT1` from the context (formula functions and context are combined in the same editor).
- Formula must declare a **result/return object of type Number** (string length returns a number); otherwise activation fails with "no result data object set" — same class of error as the Boolean mapping in Part 3.
- Back in the condition the formula result is compared: first attempt `<> 10` (wrong, because that fails exactly at length 10), final logic `<= 10` so that length 0–10 returns true (no message) and 11+ returns false (message). Approve → enable → test: 9 and 10 chars pass, 11 chars triggers the message.
**Key insight:** Operators alone cannot do string work — you must nest a Formula expression object inside the condition, and the formula needs an explicit typed result (Number). Also: "not equal to 10" is a logic trap; the requirement is a boundary, so use `<=`.
**Prereq:** DQM Part 1 and Part 2 (configuration, scope/condition, inverted false=error logic). Part 3 is *not* required — this is the no-code path where Part 3 would otherwise tempt you into ABAP.

### 13. Special characters restriction in DQM (No code)
**ID:** [erS6iiuFE60](https://youtu.be/erS6iiuFE60) | **Length:** 10m | **Level:** beginner

**In one line:** Blocks symbols in a BP field purely with a DQM condition, using the "does not contain any" operator plus an explicit list of special characters.
- Opening context: in the "new supplier organization" app `SORT1` accepts `!@#$%…` with no error — that is the gap the video closes.
- Navigate to the **Validation Rules** tile (in newer releases validations live under their own tile, separate from "business rules") → Create. Rule ID `ST1_RESTRICT`-style, rule name "Special characters are not allowed", base table `B0` / `BU20`, **checked field `BU_SORT1`** ("BP sort 1", found via field help on table `B0`).
- Create the rule first, then `ADD` usage → "Check in Change Request" → `Prepare` (base table is prefilled from the header) → framework creates scope + condition expressions.
- Scope: edit operand → Default Objects → `true = true` (or `false = false`) so it applies to every record; the real check goes in the condition.
- Condition: `EDIT OPERAND` → Direct Value → context `BU_SORT1`, operator **`does not contain any`** (the operator family "contains any" was available; choose the negated one), then type the special-character set (`!@#$%^&*()…`, brackets optional) into the operand. "Contains any" would return true when a symbol is present = no error; "does not contain any" inverts it to false = error.
- Approve → enable → test in Manage Supplier (new organization, internal numbering): "testing" passes, adding one symbol raises "Special characters are not allowed", removing it clears the message.
**Key insight:** This is the cheapest way to get character-level field hygiene without a single line of ABAP — but only because the operator set is a fixed list, i.e. it is a blacklist, not a whitelist. Any character you forget to type into the operand is silently allowed.
**Prereq:** DQM Part 1 (rule header, usage, scope, approve/enable); Part 2 for the idea of a "inverted" condition.

**Checkpoint:** write one rule three ways - BRF+ validation, BAdI validation, DQM rule - for the same requirement (e.g. postal code mandatory for one country). Then say out loud when you would pick each one in a project.

---


## Phase 5 - Search and Duplicate Check

**4 videos · 1h24m**

Short phase, high project value: duplicate check is in almost every MDG scope, and search methods are the usual bug source after go-live.


### 1. Duplicate check configuration in SAP MDG BP
**ID:** [Q3C0ox6EzjI](https://youtu.be/Q3C0ox6EzjI) | **Length:** 17m | **Level:** intermediate

**In one line:** Configures out-of-the-box BP duplicate check end-to-end — search mode, match profile, entity-type threshold and CR-step flag — and adds a display-only "extra attribute" to the duplicate popup.
- MDGIMG → General Settings → Data Quality and Search → Duplicate Check: check **Define Search Configurations** (SAP delivers all search modes; DB mode used), then **Allocation of Search Help to Search Applications** (MCBP_GENERAL already allocated to BP General data — untouched).
- **Define Match Profiles**: data model BP, copy SAP-delivered **BP_CENTRAL**, create `Z_MC_BP_DUPLICATE_CHECK` (BP_CENTRAL_CHECK), entity type **BP_HEADER**, text "BP duplicate check for customer"; in *Relevant Fields* add BP_CENTRAL → attribute **NAME_1 (name of organization)**, flag **mandatory** (check does not fire at all if empty), weight 0 / fuzziness 0, sequence 1.
- **Configure Duplicate Check for Entity Types**: data model BP, entity type BP_HEADER (only type 1), search mode DB, own match profile, **lower/higher threshold** = match % that decides whether the popup appears, search help = match-profile-based UI, then *Check*.
- MDGIMG → Process Modeling → Change Requests → **Configure Properties of Change Request Step**: CR type `Z_CUSTOM_P1`, step **00** (initial), tick **duplicate check relevant** (empty by default on first setup), execution "when data changes"; without this the CR type never checks.
- Extra attribute for the popup: add second entry **BP_SORT1** in the same relevant-fields list and mark it *extra attribute from search help* (not mandatory) — it displays only and contributes nothing to scoring.
**Key insight:** the extra attribute does not appear until you also list **MC_NAME1** next to **NAME_1** — the name field exists in both forms and both must be in the profile; symptom before the fix was a duplicate hit with no sort1 column.
**Prereq:** BP data model/CR type with an initial step and NWBC access (test CR type here was an auto-approval type so submit = activation).

### 2. SAP MDG Defaulting search methods in Customer or Supplier search
**ID:** [FsEfdTpBV84](https://youtu.be/FsEfdTpBV84) | **Length:** 17m | **Level:** advanced

**One line:** Change which search method is preselected when the Customer/Supplier search UIBB opens (Address data → BP roles) via an implicit enhancement.
- Where the dropdown comes from: MDGIMG → General Settings → Data Quality and Search → **Search and Duplicate Check → search modes**; each search mode has search helps allocated (DB search helps vs HANA search helps) per data model. HANA entries are only populated when ESH is enabled.
- Find the feeder class of the search UIBB via technical help → component configuration → general settings → feeder class; open in SE24. Relevant method is the **dropdown-filling method** (`CS_DATA` = structure holding the defaulted selection, `CT_METHOD` = the dropdown list). Hiding a method = delete its row from CT_METHOD; defaulting = fill CS_DATA.
- Debug proof: external breakpoint on the last line of the method, open the search, in desktop 3 fill `CS_DATA-METHOD = '0005'` (BP roles) → the UI switches and the criteria auto-adjust (BP role criteria appear).
- Programmatic fix: SE24 → Edit → **Enhancement → Show implicit enhancement options** → create enhancement `ZEI_...` in that method. `READ TABLE ct_method ... INTO DATA(ls_method)` (loop not needed), key fields are the four of the method/help structure (`METHOD`, `PROVIDER`, `HELP TEXT`, …) — method `0005`, provider `DB`, search help `MCBP`/role help. Then **`MOVE-CORRESPONDING ls_method TO cs_data`** — direct assignment `cs_data = ls_method` dumps because the structures differ.
- Filter by object: `CS_DATA` carries an **OTC (object type code)**; MDGIMG → Data Modeling → Business Object Type Code shows BP, **Customer = 159**, **Supplier = 266**. Adding OTC 159 limits the defaulting to customer governance only (supplier still shows Address data); use 266 for supplier.
**Key insight:** without the OTC filter the change hits *both* customer and supplier governance, because both use the same feeder class — and MOVE-CORRESPONDING (not `=`) is what makes the defaulted row usable.
**Prereq:** working search UIBB / search modes, plus authorization for the implicit enhancement (must be transported, local object only for the demo).

### 3. OVS search helps in SAP MDG
**ID:** [zbKXEvTF0vA](https://youtu.be/zbKXEvTF0vA) | **Length:** 40m | **Level:** advanced

**One line:** Full four-phase OVS implementation for a custom field in a custom feeder class, including filtering by what the user types.
- Get the feeder class from technical help → component configuration → general settings; it is a custom feeder extending SAP's BP form feeder. In SE24 display, *Edit → Enhancement → redefine* each OVS method. Custom table `ZT_MDG_ROUTERS`, line type `ZS_ROUTERS`.
- **Registering the OVS:** in the field-description method, `ET_FIELD_DESCRIPTION` is a table of structures with `NAME_COMP` (component/field name) and `OVS` (OVS class name). Loop it with a field symbol, `IF <fs>-name = 'ZZROUTER'` → `<fs>-ovs = <ovs class>`. After activation the component configuration shows the OVS class under the field's display-type-dependent properties (the field goes from "input help: auto" to that OVS class).
- **Phase 0 – configuration:** `SET_CONFIGURATION` → window title "Router names", table header, column text (group header/label text are obsolete).
- **Phase 1 – `SET_INPUT_STRUCTURE`:** hand over the initial structure (type `ZS_ROUTERS`) so the search popup starts with client/router as filter fields instead of an empty screen.
- **Phase 2 – results:** `IF iv_field_name = 'ZZROUTER'` → declare `lt_routers TYPE TABLE OF ...` / `ls_router TYPE ZS_ROUTERS`, `SELECT * FROM ZT_MDG_ROUTERS INTO TABLE`, assign to the OVS output table. **Remove the `super->` call** — the standard method clears the output table. Read the user's typed values from `io_ovs_callback->wd_ovs->query_parameters` (verify in the debugger, desktop 3) and filter with a select-option table: `SIGN = 'I'`, `OPTION = 'CP'` (constant from `USMD0_CS_...`, not hardcoded), `LOW = router` → so "S*" returns South Africa/South Korea, "I*" India, and a bare "ien" returns nothing (contains needs the star).
- **Phase 3 – write back:** selection arrives as a **reference**, so `ASSIGN` + dereference into `LS_SELECTION` (type of the table's value), then `io_ovs_callback->get_context_element( )->set_attribute( name = 'ZZROUTER', value = ... )` to fill the UIBB field.
**Key insight:** dropping `super->` is mandatory in phase 2/3 (otherwise your output table is wiped) but not in phase 1 (keep standard behaviour), and the OVS class is only visible on the field after the field-description method is redefined and activated.
**Prereq:** custom table + custom feeder class on the UIBB (component configuration), and a field already on the UI.

### 4. Activating HANA search in SAP MDG Customer
**ID:** [SQKZiumvmhU](https://youtu.be/SQKZiumvmhU) | **Length:** 9m | **Level:** intermediate

**One line:** Generate the SAP-delivered "Customer Search HANA" search view and add a non-standard field (Industry) to it and to the FPM search UIBB.
- MDGIMG → General Settings → **Data Quality and Search → Search and Duplicate Check** → the MDG-delivered search views exist but are **saved, not generated**; HANA search is therefore not available in the CR search screen.
- Select the MDG Business Partner node → **Customer search** → Edit → assign package (`ZMDG`) → Next → tick the fields in scope. Industry is not SAP-delivered, so use the *including view* option and switch the other two dependent options off → save into a change request → OK → **Generate** (first generation takes a while; generation is the "activation" step here).
- Refresh the change request search screen: a new entry **"Customer Search HANA"** appears in Search Criteria. (Fields added to the view are not automatically on the search UI.)
- To surface Industry as a criterion: SE80 → Web Dynpro component **`FPM_SEARCH_UIBB`** → configuration "Customers: Dynamic Query for HANA Search" → do **not** edit the SAP component configuration → create a **Customizing**, then drag Industry into the search criteria (he puts it 4th/5th) → save, reset/refresh → Industry appears with a dropdown and can be used to search.
**Key insight:** two independent switches — generating the HANA search view (MDGIMG, entity/field scope) and adding the field to the FPM search UIBB (SE80 customizing). A field visible in the search view but missing from the UIBB simply does not appear on screen.
**Prereq:** HANA/ESH-based search available in the system; a transportable package and an open CR for the search-view change.

**Checkpoint:** enable duplicate check on BP with a search mode and make it block creation on a match; explain the difference between search sequence, search mode and the defaulting search method.

---


## Appendix A - Master watch order (all 54)

| # | Video | Length | Phase |
|---|---|---|---|
| 1 | [MDG Overview for beginners](https://youtu.be/-WjWaGdmuCY) | 6m03s | P0 |
| 2 | [MDG High Level visualization in integration](https://youtu.be/_z3U_uaZ9W4) | 1m51s | P0 |
| 3 | [Adding MDG Apps to NWBC](https://youtu.be/L9nSSBmOhgA) | 12m22s | P0 |
| 4 | [SAP MDG BP Number ranges and CVI config basics](https://youtu.be/c4IXaHVKfuY) | 21m30s | P0 |
| 5 | [Concept of Data modeling( Theory + Practice )](https://youtu.be/0_Zh5l8cRko) | 91m43s | P1 |
| 6 | [Data model extension in SAP MDG Business partner](https://youtu.be/45nxZNTE4HY) | 28m20s | P1 |
| 7 | [Field property badi - Implementation](https://youtu.be/N0ddqPBlIwg) | 22m57s | P1 |
| 8 | [Field property badi - Using custom table](https://youtu.be/HX1CXqzRODI) | 37m27s | P1 |
| 9 | [SAP MDG Data model extension with custom attribute at Customer General Data](https://youtu.be/iC84jBUj3fc) | 27m25s | P1 |
| 10 | [Material data model extension with custom attribute](https://youtu.be/_aPCLXVHhAs) | 22m30s | P1 |
| 11 | [Data model extension with custom entity at staging level in BP](https://youtu.be/-jKrMych1yc) | 28m12s | P1 |
| 12 | [DM extension custom entity and custom table Reuse mode in BP](https://youtu.be/AOShQLm_f6I) | 95m51s | P1 |
| 13 | [UI Modelling in SAP MDG (Intro)](https://youtu.be/bFJtYhM8wxU) | 32m21s | P2 |
| 14 | [MDG UI OVP Component Overview](https://youtu.be/HXY0LNcFDn8) | 15m01s | P2 |
| 15 | [Context based adaptations in MDG](https://youtu.be/ITHM22lgAwE) | 9m02s | P2 |
| 16 | [How to make key appear for BP Grouping or any dropdown in MDG UI](https://youtu.be/BbnjHrh-vtE) | 4m15s | P2 |
| 17 | [Changing Highlight Colors in SAP MDG](https://youtu.be/juIpPuAwOlM) | 7m39s | P2 |
| 18 | [Multi selection F4 help](https://youtu.be/4oNhI695gjM) | 15m22s | P2 |
| 19 | [CR UI extension with attribute](https://youtu.be/pvMsc_cCXQs) | 37m13s | P2 |
| 20 | [SAP MDG CR section default collapsing based on CR type](https://youtu.be/XflP-k9u0tc) | 22m49s | P2 |
| 21 | [Hiding UIBBs according to role](https://youtu.be/E_ouMzBTLEo) | 21m46s | P2 |
| 22 | [Inserting Images in MDG UI](https://youtu.be/gZkhnUdljT0) | 23m44s | P2 |
| 23 | [Simple FPM Form application - Part-1](https://youtu.be/pxfn1s6Yg_0) | 28m44s | P2 |
| 24 | [Simple FPM Form application - Part-2](https://youtu.be/nemZlP1b11k) | 33m55s | P2 |
| 25 | [Simple FPM form application - Part 3](https://youtu.be/yK72NQNf-98) | 18m58s | P2 |
| 26 | [Simple FPM Form Application - Part 4](https://youtu.be/mjoSb4Rrtdo) | 9m45s | P2 |
| 27 | [Creation of Custom CR type in SAP MDG](https://youtu.be/2FvrNfH--4c) | 52m44s | P3 |
| 28 | [Hiding CR types in popup, Making CR attributes as mandatory or default values](https://youtu.be/_Ab39RJ_1uM) | 19m17s | P3 |
| 29 | [Restriction of account group based on CR types in MDG BP](https://youtu.be/RGICx0gfuC4) | 32m08s | P3 |
| 30 | [MDG BP CVI field configurations for address, sales area and company code data](https://youtu.be/6P3zaxPPYv8) | 12m29s | P3 |
| 31 | [Making attachment as mandatory in a CR in SAP MDG](https://youtu.be/PqHVKwlLiDs) | 19m42s | P3 |
| 32 | [SAP MDG Simple parallel workflow](https://youtu.be/aHzAdGHS3g8) | 45m49s | P3 |
| 33 | [Skipping approver step if approver is requestor in SAP MDG](https://youtu.be/pGaG2Ky5_OQ) | 40m40s | P3 |
| 34 | [Eliminating requestor from approver levels in SAP MDG](https://youtu.be/Kxbryjx6opo) | 41m40s | P3 |
| 35 | [Instant rejection from parallel workitems in workflow](https://youtu.be/F_d7f-gcgAA) | 43m05s | P3 |
| 36 | [Email notifications in workflows in MDG using SO10 template](https://youtu.be/QeKQaB19vpo) | 50m29s | P3 |
| 37 | [Creation of follow-up CR for BP](https://youtu.be/pD6rWraKtlE) | 41m04s | P3 |
| 38 | [Validation and derivations in BRF+ in SAP MDG](https://youtu.be/3yeb0Xadj9Y) | 31m34s | P4 |
| 39 | [DB lookup validations in MDG BRF](https://youtu.be/8eP3QOnXh6Q) | 16m37s | P4 |
| 40 | [How to create and execute BRF+ decision tables via ABAP](https://youtu.be/1_foYbVuKco) | 28m47s | P4 |
| 41 | [Rule context badi in MDG, debugging and issue resolving](https://youtu.be/FsYJYx7x7r0) | 52m01s | P4 |
| 42 | [Validations and derivations using Badi - Simple](https://youtu.be/Ll6eQ76z8s0) | 33m29s | P4 |
| 43 | [Dynamic Validations and derivations using badi](https://youtu.be/StXYbdnRzQk) | 52m49s | P4 |
| 44 | [cross entity derivations in SAP MDG](https://youtu.be/jXCGbu5jSxE) | 37m17s | P4 |
| 45 | [Adding attributes for copy scenarios in BP](https://youtu.be/4LzcirabqXo) | 7m31s | P4 |
| 46 | [Simple validations in DQM (DQM Series - Part 1)](https://youtu.be/-27cR_d459o) | 20m16s | P4 |
| 47 | [Single entity validations in DQM(DQM Series - Part 2)](https://youtu.be/-H4fi9dZxAc) | 10m06s | P4 |
| 48 | [Cross entity validations in DQM (DQM Series - Part3 )](https://youtu.be/cK_wysGWOT8) | 37m28s | P4 |
| 49 | [String functions in DQM Validations(No code)](https://youtu.be/WAVZTzNf2bI) | 15m17s | P4 |
| 50 | [Special characters restriction in DQM(No code)](https://youtu.be/erS6iiuFE60) | 10m55s | P4 |
| 51 | [Duplicate check configuration in SAP MDG BP](https://youtu.be/Q3C0ox6EzjI) | 17m57s | P5 |
| 52 | [SAP MDG Defaulting search methods in Customer or Supplier search](https://youtu.be/FsEfdTpBV84) | 17m01s | P5 |
| 53 | [OVS search helps in SAP MDG](https://youtu.be/zbKXEvTF0vA) | 40m39s | P5 |
| 54 | [Activating hana search in SAP MDG Customer](https://youtu.be/SQKZiumvmhU) | 9m18s | P5 |

## Appendix B - The 69 videos on this channel that are NOT SAP MDG

Do not open these while studying MDG - it is a different channel's worth of content sitting in the same feed:

- **C programming** (39): Scanning user input in four languages in 3mins, Addition of two numbers in four languages in two minutes, Hello world of 4 languages in 2 minutes, reverse of a string without using string.h, Selection sort in C, file handling in C …
- **Rubik cube** (4): Rubik's cube beginners method in Telugu, F2L tutorial in telugu, F2L technique in telugu, Rubiks cube last layer tutorial
- **CAD / mechanical (NX, Creo, ANSYS)** (13): Geneva mechanism simulation, designing industrial gear in NX, basic helical gear in NX, basic aeroplane shape in NXCAD, NXCAD hook's joint simulation tutorial in telugu, hookes joint animation …
- **HTML / web** (11): Learn HTML in 30 minutes, audio in HTML, dynamic text and its attributes in HTML, forms in HTML, Tables in HTML, Lists in HTML …
- **Random / unrelated** (2): How to edit ads in YouTube in mobile, shadow fight 2-insane level

## Appendix C - What this channel does NOT teach

The 54 videos are strong on extension, UI, workflow, BRF+/BAdI and DQM validations. They are thin or silent on:

| Not covered | Why it matters | Where to get it |
|---|---|---|
| Key Mapping / Value Mapping | Every real MDG project configures ID mapping for BP/customer/vendor | SAP Help: MDG Key and Value Mapping |
| DRF+ replication | Without it governance has no output - the CR activates but nothing reaches the target system | SAP Help: Replication via DRF+ (the channel has only a 2-minute visualization clip) |
| File upload / mass processing | How the business actually loads and mass-changes data | SAP Help: MDG file upload framework, mass processing |
| Consolidation and mass data | A separate MDG scenario, often in scope | SAP Help: Consolidation |
| Full DQM / address cleansing | The channel covers DQM validations only, not DQM cleansing | SAP Help: Data Quality Management |
| Authorizations | CR-type and entity-based authorizations are a standard interview topic | SAP Help: MDG authorizations |
| S/4HANA specifics, Fiori apps | Current projects are S/4; the videos are ECC-era screens | openSAP MDG course, SAP Help "MDG on S/4HANA" |

**Practical advice:** pair this roadmap with a sandbox/IDES system from Phase 1 onwards, and read the SAP Help configuration guide for the topic of the week. Watching all 54 videos without configuring anything will not make you an MDG consultant.

## Appendix D - Caveats about these notes

- **Transcripts are YouTube auto-captions.** Object names were reconstructed where the speech recognition mangled them (`to 01` -> SU01, `OBP` -> OVP, `janil` -> GenIL, `sap Fury` -> Fiori). A handful could not be resolved and are marked inline: the OVP exit class, the user-to-roles function module, the DQM base table (`B0`), the three entity-cloner classes, and the workflow FMs spoken as "SAP VAPI GET DEPENDENT WORK ITEMS" / "SAP VAPI WORK ITEM COMPLETE" / "RSRA_USERS_OF_AGR_GET".
- **Verify before you rely on them:** `USMD120C` (spoken as "esmd 120c"), `USMD_SSW_RULE`, `USMD_WORKFLOW_CREQUEST_MAPPER`, and the rollback process-pattern number in the custom-CR-type video.
- **Two videos have no captions at all:** `_z3U_uaZ9W4` (1m51s integration visual) and `45nxZNTE4HY` (28m, "Data model extension in MDG Business partner"). Their blocks are title-based only - watch them, do not study from the notes.
- **Two titles mislead:** "Field property badi - Implementation" is the *prerequisite* of "...Using custom table"; and "MDG BP CVI field configurations" is really about S/4 account-group field status, not CVI mapping tables.
- **No timestamps** in these notes: auto-captions carry no chapter data, so bullets follow the flow of the video.

## Appendix E - Channel and playlist facts (at build time)

- **Channel:** Koushik Konda, [@koushikkonda1994](https://www.youtube.com/@koushikkonda1994), ~3,120 subscribers, 123 public videos.
- **54 are SAP MDG**, 69 are unrelated (C, HTML, NX CAD, Rubik's cube).
- **Playlists: 3**
  - *SAP MDG Technical* - all 54 MDG videos, ordered **newest first** (not a curriculum).
  - *Hear and enjoy* - unrelated.
  - *Web designing tutorials* - unrelated.

Most-watched MDG videos (a rough signal of what the community needed most):
1. [Validation and derivations in BRF+ in SAP MDG](https://youtu.be/3yeb0Xadj9Y) - 22,000 views
2. [Instant rejection from parallel workitems in workflow](https://youtu.be/F_d7f-gcgAA) - 18,000 views
3. [Creation of Custom CR type in SAP MDG](https://youtu.be/2FvrNfH--4c) - 15,000 views
4. [SAP MDG Simple parallel workflow](https://youtu.be/aHzAdGHS3g8) - 13,000 views
5. [DM extension custom entity and custom table Reuse mode in BP](https://youtu.be/AOShQLm_f6I) - 12,000 views
6. [Data model extension in SAP MDG Business partner](https://youtu.be/45nxZNTE4HY) - 10,000 views
7. [SAP MDG BP Number ranges and CVI config basics](https://youtu.be/c4IXaHVKfuY) - 9,400 views
8. [Concept of Data modeling( Theory + Practice )](https://youtu.be/0_Zh5l8cRko) - 9,100 views
