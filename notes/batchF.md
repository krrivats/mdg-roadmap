# Batch F — SAP MDG (Koushik Konda) study notes

## SAP MDG CR section default collapsing based on CR type
**ID:** XflP-k9u0tc | **Length:** 22m | **Level:** advanced
**In one line:** Force the CR overview tabbed UIBB to open collapsed for one specific CR type by enhancing CL_USMD_COMMUNICATOR->ON_START.
- Debug path: SE24 -> `CL_USMD_COMMUNICATOR` (assistance class of MDG Communicator, links the CR to the rest of the UIBBs), break point in `ON_START`. In locals: `action = create`, `io_obp`; inside io_obp the UIBB list lines 39/40 — line 39 = form UIBB inside CR master, line 40 = the CR overview tabbed window UIBB.
- Proof of concept: manually flip the `COLLAPSED` flag of the CR-overview UIBB instance to `X` in debugger -> every CR opens collapsed; therefore the instance is controllable per CR type.
- Implementation: SE24 `CL_USMD_COMMUNICATOR`, Edit -> Enhancement -> Show Implicit Enhancement Options -> create enhancement `ZE_...` ("collapse CR uibb for CR types Z_CUST_1_P1"), local object, inside `ON_START`.
- Code shape: `io_obp->get_uibbs( EXPORTING content_area = 'BS_BP_OVP' IMPORTING et_uibb = DATA(lt_uibb) )` into `TY_T_UIBB`; then `READ TABLE lt_uibb WITH KEY component = 'FPM_TABBED_UIB' interface_view = 'TABBED_WINDOW' config_id = 'USMD_CR_OVERVIEW' INTO DATA(ls_uibb)`; set `ls_uibb-collapsed = 'X'`; types involved `TY_S_UIBB`, `IF_FPM_OVP` structure.
- CR-type filter: `DATA(lo_context) = cl_usmd_app_context=>get_context( )`, guard `IF lo_context IS NOT INITIAL`, then `lo_context->get_attributes( IMPORTING ... = lv_cr_type )`; wrap everything in `IF lv_cr_type = 'Z_CUST_1_P1'`.
**Key insight:** `get_uibbs` must be given the EXPORTING parameter `content_area = 'BS_BP_OVP'`; without it the enhancement compiles and activates but never fires (silent no-effect). Also ON_START is called only once when the UIBB starts, not on every open/close of the CR.
**Prereq:** CR type already existing (here Z_CUST_1_P1) and CR description already being defaulted — this video only handles the collapse.

## MDG BP CVI field configurations for address, sales area and company code data
**ID:** 6P3zaxPPYv8 | **Length:** 12m | **Level:** intermediate
**In one line:** Why fields like Street and Reconciliation account suddenly become mandatory in the ERP-customer block, and how account-group field status in S/4 (not CVI) drives it.
- Table contrast: address lives in `BUT000` separately, whereas `KNA1` holds address fields inline (LAND1, NAME1, NAME2, PSTLZ, SORTL, REGIO) — that mismatch is exactly why a CVI mapping is required; address is only maintained at BP level in MDG.
- Repro: BP grouping that is externally numbered (e.g. 500408 on the "Birla"/external grouping) + customer role `FLCU00`/`FLCU01` added -> the ERP Customer block shows "Standard address" but no address fields, yet Done triggers "Enter a value for Street".
- Cause: SPRO -> Logistics – General -> Business Partner -> Customers -> Control -> **Define account groups and field selection for customers**, account group (000001 in the demo) mapped from the BP grouping, Field status -> General data -> Address -> Street = Required entry.
- Fix demo 1: set Street to Optional entry -> after re-creating the customer, the CR no longer demands Street (country remains mandatory from standard).
- Fix demo 2: Field status -> Company code data -> Account management -> Reconciliation account = Required entry -> after adding a company code in the CR, reconciliation account becomes mandatory.
- Page layout: Settings -> Change page layout -> add UIBBs "ERP Customer Data", "ERP Customer Company Code Data" (or both) to actually see sales area/company code blocks.
**Key insight:** Missing/mandatory fields in the MDG BP UI are frequently S/4 account-group field-status configuration leaking in through CVI, not missing CVI mapping — check S/4 first before touching MDG. This config is S/4 config: in real projects it goes through the functional consultant's transport.
**Prereq:** BP grouping + customer account group + CVI number assignment already working (i.e. the c4IXaHVKfuY basics).

## SAP MDG BP Number ranges and CVI config basics
**ID:** c4IXaHVKfuY | **Length:** 21m | **Level:** beginner
**In one line:** End-to-end minimum setup to get a BP grouping to also create an ERP customer: groupings, number ranges, account groups and the CVI BP-to-customer number assignment.
- Architecture: XD01/XK01 are obsolete in S/4 and route to BP; `BUT000` is master data, `CVI_CUST_LINK` links BP<->customer, `CVI_VEND_LINK` links BP<->vendor (mapping via `PARTNER_GUID`).
- Groupings: `BUT000-BU_GROUP` (field BU_GROUP in BP tcode) decides which number range the BP gets. SPRO -> Cross-Application Components -> SAP Business Partner -> Business Partner and Basic Settings -> Number Ranges and Groupings -> **Define Groupings and Assign Number Ranges**. Demo: grouping B001 = external, assigned to number range B1 with interval ~541000–600000; entering a number outside gives "number not in interval".
- Customer side: SPRO -> Logistics – General -> Business Partner -> Customers -> Control -> **Define account groups and field selection for customers** — account groups 000001 / ZB; ZB is internally numbered so the customer number is generated automatically.
- The missing link: SPRO -> Cross-Application Components -> Master Data Synchronization -> Customer/Vendor Integration -> Business Partner Settings -> Settings for Customer Integration -> **Define Number Assignment for Direction BP to Customer**; add BP grouping B001 -> customer account group ZB. Before this, the ERP Customer "New" button is disabled with "CVI customizing does not allow creation of customer for business partner grouping B001".
- After activation: check BP in BUPA (BP 545...) and customer in FD03/KNA1-style display; verify the link in table `CVI_CUST_LINK` by pasting `PARTNER_GUID` from BUT000 — that GUID lookup is exactly how MDG resolves the customer number for display.
**Key insight:** The ERP customer is created only at final activation, never at first-level approval — an empty ERP Customer field after approval is normal, not a bug. And both number-range layers must be consistent: BP external range for the grouping, customer internal range for the account group.
**Prereq:** none (this is the foundational CVI/BP-numbering video).

## Making attachment as mandatory in a CR in SAP MDG
**ID:** PqHVKwlLiDs | **Length:** 19m | **Level:** advanced
**In one line:** A USMD_RULE_SERVICE validation BAdI that reads CR attachments and blocks check/submit until at least one attachment exists.
- IMG: MDG -> General Settings -> Data Quality and Search -> Business Add-Ins -> **Validations and Derivations** -> create enhancement implementation `ZEI_...`, BAdI implementation `ZBA_BADI_..._MDG_BP_VALIDATIONS`, class `ZCL_MDGBP_VALIDATIONS`; an enhancement needs at least one BAdI implementation before it can be activated.
- Filter values: `MODEL = BP` and `ENTITY_TYPE = BP_HEADER` (BP_HEADER is the type-1 entity) — filter must be maintained on both.
- Filter conflict: filter values must be unique per BAdI implementation inside an enhancement; identify the clashing SAP implementation via SE18 (`USMD_RULE_SERVICE`), e.g. the standard BP description check on the same filter. Do not deactivate SAP's in SE18 — go to MDGIMG -> Process Modeling and Data Quality -> Data Quality -> Business Add-Ins -> **Activate/Deactivate BAdI implementations** (the "active" flag there is display-only, the deactivate flag is editable).
- Activate every method individually (all four); skipping one causes runtime errors, not just warnings.
- Code: guard `IF io_model IS NOT INITIAL`; get CR type with `CL_USMD_CR_UTIL=>GET_CR_TYPE_BY_CR( i_cr_id )` (alternative `USMD_120C`) and compare to `Z_CUST_1_P1`; then `io_model->read_cr_value( EXPORTING fieldname = 'USMD_CREQUEST' ... )` into `USMD_TS_ATTACHMENT` — the attachment/notes read flag is OFF by default and must be enabled, and the field name must be `USMD_CREQUEST` because CR data (not entity data) is being read.
- If `lt_data IS INITIAL`: build the error at runtime with `CL_D_MESSAGE=>CONVERT_TEXT_TO_MESSAGE` (avoids SE91 message class for a demo) and APPEND it to `et_message`; message surfaces as MSMD5-style error and blocks Submit. With one attachment present, the table has one row (file type, file size, title, content in encrypted form) and no error.
**Key insight:** `read_cr_value` returns nothing unless you explicitly switch on the read-attachments/notes option — otherwise the validation always fails even when an attachment exists.
**Prereq:** a custom CR type (Z_CUST_1_P1) to filter on; SE18/SE24/SE11 basics.

## Hiding CR types in popup, making CR attributes mandatory or default values
**ID:** _Ab39RJ_1uM | **Length:** 19m | **Level:** intermediate
**In one line:** One BAdI (MDG_UNCORE_CR_DEFAULTS) does all three CR-header tricks: hide a CR type from the New popup, default the description, and force Priority to mandatory.
- Locate CR type IDs: MDGIMG -> General Settings -> Process Modeling -> Change Request -> **Create Change Request Type** (key + description), e.g. "Create customer parallel" = `ZCUST1_P1`, "Create customer Planet" = `ZCUST1_P2`.
- BAdI: Process Modeling -> Change Request -> CR UI defaults (`MDG_UNCORE_CR_DEFAULTS`); enhancement `ZEI_MDG_UNCORE_CR_DEFAULTS`, implementation `ZBIOR...`, class `ZCL_MDG_CR_UI_PROPS`; filter value = data model `BP`; activate all four methods empty first.
- Method `FILTER_CR_TYPE` (changing table `CT_CR_TYPE`): the table has no structure — its line type is directly the data element `USMD_CREQUEST_TYPE`, so `DELETE ct_cr_type WHERE table_line = 'ZCUST1_P1'`. Debugger proof: deleting one row in the changing table drops 6 CR types to 5 in the popup.
- Method `GET_CR_ATTRIBUTES`: `IF iv_cr_type = 'ZCUST1_P2'` -> `cs_cr_data-cv_description = 'Create Customer ...'`; this is the only hook for CR-header defaulting.
- Method `SET_CR_FIELD_PROPERTIES`: `cs_cr_data-cv_priority_field_prop = 'M'`. Field-property codes (from the domain behind the field-property data element): `C` = optional, `R` = read only, `M` = required, `H` = hidden.
**Key insight:** Do not "hide" a CR type by removing its business activity — that also kills it for the background program. Hiding belongs in FILTER_CR_TYPE. The field-property codes are C/R/M/H; anything else silently does nothing.
**Prereq:** CR types exist and you can read them in MDGIMG; BAdI enhancement basics (SE19/SE18).

## Restriction of account group based on CR types in MDG BP
**ID:** RGICx0gfuC4 | **Length:** 32m | **Level:** advanced
**In one line:** A custom CR-type-to-grouping table plus an implicit enhancement in the grouping dropdown feeder method, trimming the value set at runtime.
- Customizing table in SE11: `ZMDG_CR_ACCOUNT_GROUPS` — MANDT as key (client-dependent), `USMD_CREQUEST_TYPE`, `BP_GROUPING` as second key, foreign key BP_GROUPING -> `TB001`, delivery class C, table maintenance generator created (Utilities -> Table Maintenance Generator, function group, one-step, no auth group) so it can be maintained in SM30.
- Find the feeder class: in the CR UI right-click -> Technical Help -> Component Config -> General Settings -> **Feeder Class** (here the BP root feeder class). The dropdown values are not built on page load — they are supplied by `GET_ATTRIBUTE_VALUE_SET`; debugging shows 159 grouping values arriving in `ET_VALUE_SET` with `IV_ATTRIBUTE_NAME = 'GROUPING'`.
- Enhancement: SE24 on that root feeder class, `GET_ATTRIBUTE_VALUE_SET`, Edit -> Enhancement -> Show Implicit Enhancement Options -> create `ZEI_MDG_RESTRICT_GROUPING`.
- Logic: skip unless `iv_attribute_name = 'GROUPING'`; get CR type via `CL_USMD_APP_CONTEXT=>GET_CONTEXT( )` then `get_attributes` — store the context in a variable and test `IS NOT INITIAL` first, otherwise an empty context dumps. Then `SELECT bp_grouping FROM zmdg_cr_account_groups WHERE crequest_type = lv_cr_type` into a table.
- Build a selection table of type RSDSSELOPT-style `SIGN/OPTION/LOW/HIGH` (`SIGN = 'E'`, no HIGH needed), loop the selected groupings, `APPEND` each, then `DELETE et_value_set WHERE value IN lt_selopt`. Keeping the SELECT-OPTIONS build outside the loop avoids re-appending stale rows.
- Result: only the maintained groupings (e.g. two, then three after adding one row in SM30) appear in the dropdown for CR type `ZCUST1_P2`; the same pattern works for any CR-type-dependent dropdown.
**Key insight:** `ET_VALUE_SET` must be *deleted from*, not rebuilt, and the sign has to be `E` on the select-option, otherwise you show exactly the groupings you meant to hide. Also the same enhancement must be created in the class actually used at runtime — after moving it, delete the leftover duplicate implementation or it fires twice.
**Prereq:** the custom CR type (ZCUST1_P2) and working SE11/SM30 customizing-table skills; implicit enhancement experience.

## Multi selection F4 help
**ID:** 4oNhI695gjM | **Length:** 15m | **Level:** intermediate
**In one line:** Turning an existing single-value F4 exit class into a multi-select one, and rewriting the returned data as a comma list.
- Starting point: existing custom F4 class (`ZCL_CUST_SET_F4`-style) bound to the `SET_STEMS`-like attribute; Go returns 3 values, clicking one immediately navigates back with one value. This is a follow-up to his earlier "Object F4 helps in MDG" video.
- Phase 0 (configuration): set the field's multi-select property to `ABAP_TRUE` (`'X'`) — after this the dialog stays open, allows multi-selection, and only navigates on OK.
- Phase 3 (handle selection): the selection now arrives as a **table**, not a structure, so the old `ASSIGN COMPONENT ... OF STRUCTURE <ls_selection>` leaves the short-form empty and the attribute ends up blank (OK does nothing). Fix: declare the field symbol `TYPE ANY TABLE`, `LOOP AT <lt_selection> ASSIGNING <ls_selection>`, then `ASSIGN COMPONENT 'SHORT_FORM' OF STRUCTURE <ls_selection> TO <lv_short_form>`.
- Build the display string: `IF sy-tabix = 1. lv_result = lv_short_form. ELSE. CONCATENATE lv_result ',' lv_short_form INTO lv_result. ENDIF.` -> selecting C then A yields "C,A" in the field.
- Guard with `IF lv_short_form IS ASSIGNED` before use; bind the result with `set_attribute` at the end of the loop so the UI shows "C, A" after Continue.
**Key insight:** Multi-select silently breaks single-select code with no dump at all — the field just comes back empty, because a table cannot be assigned to a structure-based field symbol. The only symptom is an empty attribute after OK.
**Prereq:** an already-working single-value F4 help exit class (Phase 0 + Phase 3) for that attribute.

## CR UI extension with attribute
**ID:** pvMsc_cCXQs | **Length:** 37m | **Level:** advanced
**In one line:** Add a brand-new custom field (CR category, CHAR1) into CR General Data, make it editable, and persist it two-way through a Z table because USMD120C cannot be appended.
- Discover the anchor: CR UI right-click -> Technical Help -> Component Config -> General Settings -> **Feeder Class Parameters**; the CR block is the General component, whose root object is `CR_ROOT` (model browser -> CR display -> root objects) with attribute structure `BSS_CR_ROOT_ATTRIBUTES` (BS_* root attributes structure).
- Extend: append structure `ZCR_CAT`-style ("custom CR UI extension") to that attribute structure with field `ZZ_CR_CAT` (char1; text alternative also possible), enhancement category "Can Be Enhanced (Deep)" to clear the warning. Refresh: `ZZ_CR_CAT` appears in Component Config and can be drag-dropped under Description, label "CR Category", saved. Field is greyed out/read-only at this stage.
- Make it editable (recommended = runs once): handler class of the CR root, method that handles **attribute properties** (`GET_ATTRIBUTES` / `CHANGE_OBJECT` / attribute-properties area), implicit enhancement -> `iv_property_object->set_property_by_name( name = 'ZZ_CR_CAT' value = 'CHANGEABLE' )`. Do not use the other, multiple-times-per-process option.
- Persistence blocker: `USMD120C` is the CR header table (CR type, status, created by...) but its structure is flagged "cannot be enhanced" — appending `ZZ_CR_CAT` fails with "structure USMD120C cannot be enhanced".
- Custom table in SE11: `ZT_CR_CAT` — MANDT + `CR_ID` (`USMD_CREQUEST`) as primary key, `ZZ_CR_CAT` CHAR1, data class Master data, size category 0/minimum, enhancement category "Can Be Enhanced (Deep)". Note the field-name rule: an underscore is not permitted in 2nd/3rd position, hence `ZT_CR_CAT` not `Z_USMD_CR_...`.
- Feeder class `CL_USMD_CR_UIBB_GENERALDATA` (CR General Data), `GET_DATA`: at the TOP of the method add an enhancement that extracts `ZZ_CR_CAT` and `CR_ID` from `CS_DATA` via `ASSIGN COMPONENT` and does `MODIFY zt_cr_cat` (set MANDT = `sy-mandt`). This is written before the superclass runs, so it is still valid — but the value is then overwritten in `CS_DATA` by the standard call, hence a second enhancement at the END of `GET_DATA`: `SELECT SINGLE * FROM zt_cr_cat WHERE cr_id = lv_cr_id`, then assign back into `CS_DATA` field symbol.
**Key insight:** One-way binding looks "broken" — the value is in ZT_CR_CAT after Submit but blank in the UI. The fix is two enhancements in the same implementation: write at the top of `GET_DATA`, read back at the end. And because USMD120C is locked, any CR-header extension must go to a side table.
**Prereq:** FPM/component-config access in the CR UI, SE11 table creation, implicit enhancement basics.

## Creation of Custom CR type in SAP MDG
**ID:** 2FvrNfH--4c | **Length:** 52m | **Level:** intermediate
**In one line:** Build CR type ZCUST1_P2 from scratch and wire a complete BRFplus rule-based workflow (submit -> approve -> background activation -> final check approved, plus reject -> rollback).
- CR type: MDGIMG -> General Settings -> Process Modeling -> Change Request -> **Create Change Request Type**: data model `BP`, description "Create Customer Plan", main entity type `BP_HEADER` (type 1), plus `ADDRESS`, `BP_RELATIONSHIP` etc. Entry type must contain the main entity type first or the entry is not saved; omitting ADDRESS gives "address cannot be changed via change request". Workflow template `WS...` (always used with BRFplus), business activity e.g. CREATECUSTOMER — that activity is what makes the CR appear in the NWBC New popup.
- Workflow config: Rule-based workflow -> "Configure your rule based workflow" for `ZCUST1_P2` (local object). Three decision tables: **Single Validation** (the controller), **User Resolution**, **Non-User Resolution**. Hide the unused columns via table settings so only ~5 remain: Workflow Step, CR Status, Condition Area, Next Step, Previous Action.
- Single Validation rows: (step 00, condition 1) -> next step 30, CR status "Final Approval"/custom "To be approved by manager"; (30 + previous action 03 approve) -> 50; (30 + 04 reject) -> 60; (50 + action "Activation Successful") -> 99 with status Final Check Approved; (50 + activation failed) -> back to 30; (60 rollback) -> 99 with Final Check Rejected. Action codes: approve = 03, reject = 04. Condition Area is just an alphanumeric key that must exist in whichever table handles that step.
- User Resolution: condition area 1, agent group `01` (always), **step type `02`** (= approve 03 + reject 04 buttons, in that order), agent type `US`, agent = SAP user `TEST_MDG1`. Step types themselves live in MDGIMG -> Change Request -> **Change Request Types and Actions** (step type 02 exposes actions 03/04).
- Non-User Resolution (background): condition area 2, agent group 01, **process pattern 06** (05 is the near-identical alternative) = activate; process pattern **99** = complete workflow; process pattern for rollback on reject. Verify all three tables are in active state before testing.
- Test: submit -> status Final Approval, workflow log shows pending with TEST_MDG1; log in as TEST_MDG1 -> approve and reject buttons appear (from step type 02) -> approve -> background step activates and completes -> Final Check Approved, BP number generated, CR closed and re-usable. Reject path: reason note recorded -> Final Check Rejected -> data rolled back and disappears from the system.
**Key insight:** Never map "approve" straight to CR status Final Check Approved. Approval must go to a **background/non-user step** that runs activation and then a completion step — otherwise the CR stays locked and no further CRs of that type can be processed. Main entity type missing from Entry Types silently blocks saving too.
**Prereq:** a BP data model with business activities; BRFplus access; NWBC with the two test users.

## MDG High Level visualization in integration
**ID:** _z3U_uaZ9W4 | **Length:** 1m51s | **Level:** beginner
**In one line:** NO TRANSCRIPT - title-based only.
- Short (1m51s) clip, no captions available on the channel: by title it is a high-level visual overview of MDG integration with the target/ERP system (data flow MDG -> CVI -> customer/vendor), not a step-by-step config video.
**Key insight:** Nothing extractable beyond the title; do not treat as configuration guidance.
**Prereq:** none
