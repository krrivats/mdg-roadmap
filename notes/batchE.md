# Batch E — Koushik Konda SAP MDG (duplicate check, rule-context BAdI, emails, follow-up CRs, requester exclusion, parallel workflows)

## Duplicate check configuration in SAP MDG BP
**ID:** Q3C0ox6EzjI | **Length:** 17m | **Level:** intermediate
**In one line:** Configures out-of-the-box BP duplicate check end-to-end — search mode, match profile, entity-type threshold and CR-step flag — and adds a display-only "extra attribute" to the duplicate popup.
- MDGIMG → General Settings → Data Quality and Search → Duplicate Check: check **Define Search Configurations** (SAP delivers all search modes; DB mode used), then **Allocation of Search Help to Search Applications** (MCBP_GENERAL already allocated to BP General data — untouched).
- **Define Match Profiles**: data model BP, copy SAP-delivered **BP_CENTRAL**, create `Z_MC_BP_DUPLICATE_CHECK` (BP_CENTRAL_CHECK), entity type **BP_HEADER**, text "BP duplicate check for customer"; in *Relevant Fields* add BP_CENTRAL → attribute **NAME_1 (name of organization)**, flag **mandatory** (check does not fire at all if empty), weight 0 / fuzziness 0, sequence 1.
- **Configure Duplicate Check for Entity Types**: data model BP, entity type BP_HEADER (only type 1), search mode DB, own match profile, **lower/higher threshold** = match % that decides whether the popup appears, search help = match-profile-based UI, then *Check*.
- MDGIMG → Process Modeling → Change Requests → **Configure Properties of Change Request Step**: CR type `Z_CUSTOM_P1`, step **00** (initial), tick **duplicate check relevant** (empty by default on first setup), execution "when data changes"; without this the CR type never checks.
- Extra attribute for the popup: add second entry **BP_SORT1** in the same relevant-fields list and mark it *extra attribute from search help* (not mandatory) — it displays only and contributes nothing to scoring.
**Key insight:** the extra attribute does not appear until you also list **MC_NAME1** next to **NAME_1** — the name field exists in both forms and both must be in the profile; symptom before the fix was a duplicate hit with no sort1 column.
**Prereq:** BP data model/CR type with an initial step and NWBC access (test CR type here was an auto-approval type so submit = activation).

## Rule context badi in MDG, debugging and issue resolving
**ID:** FsYJYx7x7r0 | **Length:** 52m | **Level:** advanced
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

## Email notifications in workflows in MDG using SO10 template
**ID:** QeKQaB19vpo | **Length:** 50m | **Level:** advanced
**In one line:** Builds a "mail requester after activation" step from scratch — service name, synchronous-system-method BAdI, SO10 HTML template, CL_BCS_MESSAGE send — and verifies it in SOST.
- `USMD_SSW_RULE` (or MDGIMG → Process Modeling → Change Requests → Rule-Based Workflow → Configure Rule-Based Workflow) for CR type `Z_CUSTOM_P1`: duplicate the post-activation row, insert a new CR step before **CMP** (completion), agent `EAA`, description "email after activation".
- MDGIMG → **Define Service Names for Rule-Based Workflow** → `Z_EMAIL_TO_REQUESTER`; agent group 0, process pattern **2 = synchronous system method**.
- BAdI: Rule-Based Workflow → Business Add-Ins → the 5 workflow BAdIs → **synchronous system method** one: enhancement `ZEI_...`, impl `ZBI_SEND_EMAIL_TO_REQUESTER`, class `ZCL_SEND_EMAIL_TO_REQUESTER` (local object), filter *service name = Z_EMAIL_TO_REQUESTER, comparator =*.
- **SO10** standard texts `Z_EMAIL_TO_REQUESTER` (body) and a subject text, object `TEXT`, text ID `ST`, language EN — body written with **`<BR>`** breaks because the mail is sent as document type **HTM**; the Word/SAPscript editor line breaks are lost (proved by running FM **READ_TEXT** and seeing the text collapse).
- ABAP: `CL_USMD_MODEL_EXT=>GET_INSTANCE( 'BP' )` → read char values of the CR into a `USMD_TS_SEL` selection (sign I, option EQ, low = CR number) → BP number from the entity row; `READ_TEXT` + `DESCRIBE TABLE ... LINES` loop + `CONCATENATE` into one string; `CL_BCS_MESSAGE` object → `SET_SUBJECT`, `SET_MAIN_DOCUMENT` (type HTM), `ADD_RECIPIENT`, `SET_SEND_IMMEDIATELY( ABAP_TRUE )`, `SEND` in TRY/CATCH; `REPLACE ALL OCCURRENCES OF` for `&customer number` / `&req`.
**Key insight:** recipient is derived from the CR header creator (`USMD_CREQUEST_CREATED_BY` / created-by in the CR table) and then **BAPI_USER_GET_DETAIL** with its RETURN structure — you must pass the RETURN type or the call dumps; debug with an **external breakpoint under user WF-BATCH**.
**Prereq:** rule-based workflow with an activation step and a completion (CMP) row; SOST access to verify.
**Workflow concept covered:** post-activation background step via synchronous system method BAdI (mail on activation).

## Creation of follow-up CR for BP
**ID:** pD6rWraKtlE | **Length:** 41m | **Level:** advanced
**In one line:** Creates a follow-up change request automatically just before the main CR completes, using CL_USMD_CREQUEST_API create-by-reference plus convenience API object-list copying.
- Baseline flow: requester S4_MDG7 → role `ZC_MDG_TEST1` (PFCG check) → level 1 check → "Final check to be performed" → **95** activation → **99**.
- `USMD_SSW_RULE` / MDGIMG rule-based workflow: add service `Z_FOLLOWUPS` in **Define Service Names**, insert new step **98** (status 02) right after activation-success row, set the `$` (completion) symbol on it, keep 99/05 rows, agent `Z_FOLLOWUPS` = process pattern 2 (synchronous system method).
- BAdI "calling of system method for rule-based workflow": enhancement `ZEI_CREATE_FOLLOWUPS`, impl `ZBI_CREATE_FOLLOWUP`, class `ZCL_CREATE_FOLLOWUP_CR`, filter service `Z_FOLLOWUP_CR`.
- ABAP: `CL_USMD_CREQUEST_API=>GET_INSTANCE` (do **not** pass a CR ID, model = BP / GP_BP_MODEL) → `CREATE_CREQUEST_BY_REFERENCE` with `IV_CREQUEST_TYPE` = follow-up type, `IV_ATTRIBUTES` empty (`USMD_TS_FIELD_NAME`), attachments/notes ABAP_FALSE → `EV_CREQUEST` = new CR ID; read source objects with `CL_USMD_CONV_SOM_GOV_API=>GET_INSTANCE( 'BP' )→GET_OBJECT_LIST`, loop, `ENTITY = BP_HEADER`, `ASSIGN COMPONENT ... STRUCTURE` → `LV_BP_HEADER` type `BU_PARTNER`.
- Attach to the new CR: `crequest_api->ADD_OBJECT_LIST` with table type `USMD_TS_CREQUEST_ENTITY` (USMD_CREQUEST, USMD_ENTITY (must be a USMD_ENTITY value, not a field name), sequence 1, USMD_VALUE = BP number), then `ENQUEUE`/`DEQUEUE`, `WRITE_VALUE` (field name `GP_BP_HEADER`-style constant) with the generated **/MDG/BP_PP_CORE...** mapping structure, and save.
**Key insight:** `ADD_OBJECT_LIST` rejects a field-name string — passing `GC_FIELD...` gives a type error; you must pass the model entity constant. Second gotcha: `SM12` lock leftovers block the workflow edit ("just delete the lock"), and the new CR appears in the original CR only as an out-of-the-box **follow-up hyperlink** (276 → 277) once the API save succeeds.
**Prereq:** rule-based workflow with activation-success/CMP rows + ABAP knowledge of the MDG CR APIs.
**Workflow concept covered:** follow-up CR creation from a workflow background step (create-by-reference).

## Skipping approver step if approver is requestor in SAP MDG
**ID:** pGaG2Ky5_OQ | **Length:** 40m | **Level:** advanced
**In one line:** When the requester is also in the level-1 role, the whole level is skipped via the **dynamic agent selection** BAdI so the CR jumps straight to level 2.
- Setup: role `ZC_MDG_TEST` = level 1 (users S4_MDG7 + ZS4_MDG71), `ZC_MDG_TEST1` = level 2 (ZS4_MDG71 only, has Activate/Reject; level 2 status showed as "Final check to be performed").
- MDGIMG → Define Service Names for Rule-Based Workflow → `Z_SKIP_GLOBAL_SPECIALIST`, description "to skip global specialist if requester is also global specialist"; then put that service into the BRF+ decision table's **dynamic agent selection** column (first restore the hidden dynamic columns), save + activate.
- BAdI: Rule-Based Workflow → Business Add-Ins → **Dynamic Agent Selection in Rule-Based Workflow**: enhancement `ZEI_SKIP_GLOBAL_SPECIALIST`, class `ZCL_SKIP_GLOBAL_SPECIALIST`, filter *service = Z_SKIP_GLOBAL_SPECIALIST*; must first generate/implement the empty interface method in SE24 and activate the class, otherwise the BAdI shows "not implemented".
- Code on changing parameter `CT_USER_AGENT_GROUP`: loop groups → inner loop `USER_AGENT`; where `USER_TYPE = 'AG'` (role), call FM **RSRA_USERS_OF_AGR_GET** (role → users, time-dependent) into table type **AGR_USERS**; compare UNAME with the CR creator read via `SELECT SINGLE USMD_CREQUEST_CREATED_BY ... FROM ... ESMD120C WHERE usmd_crequest = lv_cr_number`.
- On match: FREE ct_user_agent_group, rebuild the row with step type 8 / agent group 000 and user agent type **AG**, user value `ZC_MDG_TEST1` (append to `LT_USER_AGENT_GROUP`, then assign back), and also set `CV_NEW_CR_STATUS = '00'` and `CV_NEW_CR_STEP = '10'` — forgetting these two leaves the CR on the old step.
**Key insight:** pass only the **first 30 characters** of the role name (USER_VALUE is 100 chars long) to RSRA_USERS_OF_AGR_GET or the call dumps; and you cannot FREE/MODIFY the table you are looping over — copy to a local table first.
**Prereq:** two-level rule-based workflow with role-based agents; PFCG role/user knowledge.
**Workflow concept covered:** dynamic agent selection BAdI used to skip an approval level when the requester is in the approver role.

## Eliminating requestor from approver levels in SAP MDG
**ID:** Kxbryjx6opo | **Length:** 41m | **Level:** advanced
**In one line:** Instead of skipping a level, it strips the requester out of the level-1 role and re-writes the agent as explicit users, so only the remaining users see the work item.
- Requirement demo: user S4_MDG7 is both requester and member of role `ZC_MDG_TEST`; rule = "anyone who requests a CR must not process any further step", so the CR must route only to ZS4_MDG71.
- BAdI choice: Rule-Based Workflow → Business Add-Ins → the **general BAdI that executes at every step** ("MDG user determination"), enhancement `ZEI_MDG_USER_DETERMINATION`, impl `ZBI_REQUESTER_EXCLUDE`, class `ZCL_REQUESTER_EXCLUDE`.
- Filter values must pin both dimensions: **CR type = Z_CUSTOM_P1** and **model = BP** (comparator `=`), so the code needs no CASE/IF on CR type.
- Inside the loop over `CT_USER_AGENT_GROUP`: where `USER_TYPE = 'AG'`, call FM **RSRA_USERS_OF_AGR_GET** (time-dependent) into `AGR_USERS`; `continue` when `UNAME = LV_CREATED_BY` (requester read with `SELECT SINGLE ... USMD_CREQUEST_CREATED_BY ... esmd120c WHERE usmd_crequest = iv_cr_number`).
- Then **convert the role agent into single users**: build `LS_USER_AGENT` rows with user type **US** and user value = each remaining user ID into a `USMD_TS_USER_AGENT`-style table, append into the group's USER_AGENT, and append the group back — instead of leaving one AG/role entry.
**Key insight:** the role must be exploded into US entries, otherwise deleting one UNAME does nothing (BRF+ still resolves the whole role). Also never FREE/MODIFY the internal table you are inside — doing so dumped; move the assignment outside the loop, verified by debugging the class from **SM50**.
**Prereq:** the parallel/level workflow with role-based agents; PFCG + AGR_USERS knowledge.
**Workflow concept covered:** requestor exclusion from role-based agent determination (role → user conversion).

## Instant rejection from parallel workitems in workflow
**ID:** F_d7f-gcgAA | **Length:** 43m | **Level:** advanced
**In one line:** Fixes the "reject one, wait for the others" flaw of parallel approval by closing every sibling work item and sub-workflow programmatically the moment one approver rejects.
- Workflow hierarchy first: SWIA shows the requester's **top/main work item** (type W = workflow), each parallel branch is a **sub-workflow work item (W)**, and inside it **dialog items (F)** for each approver; background steps show as type **B**.
- Top work item lookup in SE24: class **CL_USMD_WORKFLOW_CREQUEST_MAPPER**, method *get work item by CR (single)* → returns the parent work item ID for a CR number (427333 for CR 877) — no table digging needed.
- FMs: **SAP_WAPI_GET_DEPENDENT_WORK_ITEMS** (input work item ID; result rows type **SWR_WIHDR** with WI_ID, WI_TYPE, status text) and **SAP_WAPI_WORKITEM_COMPLETE** (only WI_ID mandatory) to finish each item.
- BRF+ changes: new service `Z_MDG_CUSTOMER_PARALLEL_REJECT` in Define Service Names; split reject from approve into its own row (duplicate row, remove approve/reject from each), new condition alias **REJ**, previous step 60 → new CR step 60, then a **99** row, plus parent step 20; agent REJ = agent group 1, process pattern 2, service `Z_MDG_CUSTOMER_PARALLEL_REJECT`.
- BAdI "calling of system method for rule-based workflow": enhancement `ZEI_MDG_...`, class `ZCL_MDG_SYNC_SYSTEM_METHOD`-style, filter = the reject service; code: get top work item → get dependent items → loop → if `WI_TYPE = 'W'` (or `'F'`) and status text = READY (also "in process") → `SAP_WAPI_WORKITEM_COMPLETE( wi_id = ls_items-wi_id )`; closing the sub-workflows fires the **merge (match) BAdI**, which carries the reject decision and closes the CR.
**Key insight:** you must close the sub-workflow items, not just the dialog items — otherwise the merge BAdI never runs and the CR hangs; and status text is compared as text ("READY"), so both dialog and workflow types need the check.
**Prereq:** a working 3-approver parallel workflow with merge BAdI and BRF+ step table.
**Workflow concept covered:** parallel work items + instant rejection (programmatic closing of sibling work items).

## SAP MDG Simple parallel workflow
**ID:** aHzAdGHS3g8 | **Length:** 45m | **Level:** advanced
**In one line:** Designs and builds a 3-approver parallel workflow from a copied CR type: BRF+ step matrix, agent table with 3 agent groups, merge BAdI, plus approve-all and reject-one test runs.
- Design first: step **00** requester → **20** parallel split to approvers → **30** merge → **90** Act → **31** activation successful → **99** Final check approved; reject path → **RLB** (rollback) → **95** → **99** Final check rejected.
- Copy CR type `Z_CUST_P1` → new "create customer parallel" type, then `USMD_SSW_RULE` → single evaluation table rows: previous 00 / condition alias **AP1** / CR step **20** / status "to be approved by data steward" / process pattern **2** + parameter = service name for matching; keep the **parallel step / parent step = 20** and branches for agent groups 1, 2, 3; action **03** (approve) from step 20 → **30**; **CMP** (completion) → 99; step 30 + action **31** → 99 final check approved; step 30 + action `<>31` (activation failed) → agent **REQ** with status **07** and CR step 00/01; step 30 + action **04** (reject) → **RLB**, parent AP1, CR step **95**; step 95 → CMP → 99 final check rejected.
- Agent assignment table: `AP1` entered **three times** with agent groups 1/2/3, user type **US**, users TEST_MDG1/2/3, step type **2** (approve + reject); `REQ` with agent group 1, user type **SU**, value **INIT** (initiator), step type **7** "finalist processing" = the only single-button step; **CMP** = process pattern *completion*, **RLB** = *rollback*, **ACT** = *activation bypass snapshot*.
- Merge BAdI: MDGIMG → Rule-Based Workflow → Business Add-Ins → **Handling of Parallel Results in Rule-Based Workflow**: enhancement `ZEI_MDG_MATCH...`, class `ZCL_MDG_MATCH`-style; filter value = the service name (must be maintained first, activation fails without it).
- Merge code signature `IT_STEP_ACTION` / `EV_MERGE_ACTION`: loop actions → any **04 (reject)** sets merge action 04 and `RETURN` immediately; otherwise **03 (approve)**; the returned action drives step 30 onward (approve → Act → 99 approved; reject → rollback → 95 → 99 rejected, staging data deleted).
**Key insight:** approval is only reached after **all three** work items are decided — that is why the merge BAdI must return reject as soon as it sees one reject; also the whole thing cannot be tested until the merge BAdI exists, the BRF+ table validates but the workflow stops at merge time.
**Prereq:** CR type copy + BRF+ USMD_SSW_RULE basics; three test users; activation/rollback step types understood.
**Workflow concept covered:** parallel workitems with 3 agent groups, merge (match) BAdI decision, rollback and activation-failure branches.
