"""Build ROADMAP.md from the per-video note batches."""
import re, glob, json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

V = json.load(open('data/videos.json', encoding='utf-8'))['entries']
v = {x['id']: x for x in V}

blocks = {}
for f in glob.glob('notes/batch*.md'):
    for b in re.split(r'\n(?=## )', open(f, encoding='utf-8').read()):
        if b.startswith('## '):
            m = re.search(r'\*\*ID:\*\*\s*(\S+)', b)
            if m:
                blocks[m.group(1)] = b.strip()

PH = [
    ("P0", "Phase 0 - Orientation and environment",
     "Goal: know what MDG is, where you actually work, and how BP relates to customer/vendor. "
     "Nothing here is hard - do not skip it, because every later video assumes these four facts.",
     ["-WjWaGdmuCY", "_z3U_uaZ9W4", "L9nSSBmOhgA", "c4IXaHVKfuY"],
     "**Checkpoint:** create one BP grouping (external, number range) and one customer account group "
     "(internal), wire CVI number assignment, create a BP and find its customer in `CVI_CUST_LINK`. "
     "If you can explain BUT000 vs KNA1 vs CVI_CUST_LINK out loud, Phase 0 is done.",
     "Know what MDG is, log in to a CR screen, explain BP vs customer/vendor"),

    ("P1", "Phase 1 - Data Modeling (the backbone)",
     "This is the phase that decides whether the rest makes sense. Order inside the phase is strict: "
     "theory -> simplest custom attribute -> the Field Property BAdI -> the same pattern on other objects "
     "-> custom entity (type 4) -> the 95-minute reuse-mode build last.\n\n"
     "Two warnings from the transcripts: the 91-minute theory video ends at \"visualize the data model\" - "
     "it does **not** cover UI or process modeling. And the two Field Property videos are mislabelled: "
     "`N0ddqPBlIwg` (\"Implementation\") is the prerequisite, `HX1CXqzRODI` (\"Using custom table\") builds on it.",
     ["0_Zh5l8cRko", "45nxZNTE4HY", "N0ddqPBlIwg", "HX1CXqzRODI", "iC84jBUj3fc",
      "_aPCLXVHhAs", "-jKrMych1yc", "AOShQLm_f6I"],
     "**Checkpoint:** extend BP with your own attribute, see it in staging and active tables, put it on a "
     "CR screen, activate one CR. Then repeat the same on material without re-watching the video.",
     "Extend BP / customer / material, add a custom entity, drive field properties by table"),

    ("P2", "Phase 2 - UI and Floorplan",
     "Watch the architecture video first even though it is 70% theory - it is the only place that explains "
     "WebDynpro -> FPM -> OVP -> GenIL and why `Z` data models behave differently from BP/MM. After that the "
     "phase runs easy-to-hard: 4-10 minute no-code wins, then CR-screen changes, then the 88-minute FPM form build.\n\n"
     "The FPM series is one continuous build: Part 1 creates the app, Part 2 is a display-type catalogue, "
     "Part 3 adds an action, Part 4 adds a right-click context menu. Never split them across weeks.",
     ["bFJtYhM8wxU", "HXY0LNcFDn8", "ITHM22lgAwE", "BbnjHrh-vtE", "juIpPuAwOlM", "4oNhI695gjM",
      "pvMsc_cCXQs", "XflP-k9u0tc", "E_ouMzBTLEo", "gZkhnUdljT0", "pxfn1s6Yg_0", "nemZlP1b11k",
      "yK72NQNf-98", "mjoSb4Rrtdo"],
     "**Checkpoint:** hide one UIBB by role, add a multi-select F4 to a field, add a custom field to the CR "
     "header with your own label. You should be able to say which layer you touched each time "
     "(UIBB config vs CR UI vs FPM app).",
     "Change any MDG screen, hide/adapt by role and CR type, build a form UIBB"),

    ("P3", "Phase 3 - Process Modeling: CR types and workflow",
     "Custom CR type is the pivot of the whole implementation - everything in Phase 3 and 4 filters on a CR "
     "type. Do it first and keep that CR type (`ZCUST1_P1`/`ZCUST1_P2` in the videos) for every later exercise.\n\n"
     "Workflow videos are ordered by the problem they solve, not by upload date: build a parallel workflow -> "
     "the three requestor/approver edge cases -> instant rejection -> notification and follow-up CR.",
     ["2FvrNfH--4c", "_Ab39RJ_1uM", "RGICx0gfuC4", "6P3zaxPPYv8", "PqHVKwlLiDs", "aHzAdGHS3g8",
      "pGaG2Ky5_OQ", "Kxbryjx6opo", "F_d7f-gcgAA", "QeKQaB19vpo", "pD6rWraKtlE"],
     "**Checkpoint:** build your own CR type with 3-step approval (level 1 parallel, level 2 single), force "
     "the requester out of an approver level, and make one field block submission until filled. That "
     "combination is exactly the interview-level scenario.",
     "Build a CR type end-to-end, design a multi-level workflow, handle requester/approver edge cases"),

    ("P4", "Phase 4 - Validations and Derivations",
     "Deliberate order: BRF+ (config, no ABAP) -> calling BRF+ from ABAP -> rule context BAdI -> simple BAdI "
     "-> dynamic BAdI -> cross-entity -> DQM three-parter -> DQM formulas.\n\n"
     "Do not start with BAdI. The BAdI videos assume you already know how a rule is triggered, what the rule "
     "context provides, and what MDG does when a validation returns an error. The DQM series likewise assumes "
     "BRF+ fluency - its conditions are BRF+ conditions.",
     ["3yeb0Xadj9Y", "8eP3QOnXh6Q", "1_foYbVuKco", "FsYJYx7x7r0", "Ll6eQ76z8s0", "StXYbdnRzQk",
      "jXCGbu5jSxE", "4LzcirabqXo", "-27cR_d459o", "-H4fi9dZxAc", "cK_wysGWOT8", "WAVZTzNf2bI",
      "erS6iiuFE60"],
     "**Checkpoint:** write one rule three ways - BRF+ validation, BAdI validation, DQM rule - for the same "
     "requirement (e.g. postal code mandatory for one country). Then say out loud when you would pick each "
     "one in a project.",
     "Write validations/derivations in BRF+, BAdI and DQM, and know when to use which"),

    ("P5", "Phase 5 - Search and Duplicate Check",
     "Short phase, high project value: duplicate check is in almost every MDG scope, and search methods are "
     "the usual bug source after go-live.",
     ["Q3C0ox6EzjI", "FsEfdTpBV84", "zbKXEvTF0vA", "SQKZiumvmhU"],
     "**Checkpoint:** enable duplicate check on BP with a search mode and make it block creation on a match; "
     "explain the difference between search sequence, search mode and the defaulting search method.",
     "Configure duplicate check and search (OVS, HANA search, defaulting methods)"),
]


def dur(ids):
    s = sum(v[i]['duration'] or 0 for i in ids)
    return "%dh%02dm" % (s // 3600, (s % 3600) // 60)


def fmt(b, i):
    b = re.sub(r'^## (.+)$', lambda m: '### %d. %s' % (i, m.group(1)), b, count=1, flags=re.M)
    b = re.sub(r'\*\*ID:\*\*\s*(\S+)',
               lambda m: '**ID:** [%s](https://youtu.be/%s)' % (m.group(1), m.group(1)), b, count=1)
    # keep the ID/Length/Level line as its own paragraph
    b = re.sub(r'(\*\*Level:\*\* \w+)\n', r'\1\n\n', b, count=1)
    return b


secs = []
for code, title, intro, ids, chk, after in PH:
    secs.append("## %s\n\n**%d videos · %s**\n\n%s\n" % (title, len(ids), dur(ids), intro))
    for n, i in enumerate(ids, 1):
        secs.append(fmt(blocks[i], n))
    secs.append(chk + "\n\n---\n")

ALL = [i for p in PH for i in p[3]]
total = sum(v[i]['duration'] or 0 for i in ALL)
ph_of = {i: p[0] for p in PH for i in p[3]}

rows = []
for n, i in enumerate(ALL, 1):
    d = v[i]['duration']
    rows.append("| %d | [%s](https://youtu.be/%s) | %dm%02ds | %s |"
                % (n, v[i]['title'], i, d // 60, d % 60, ph_of[i]))


def cat(t):
    s = t.lower()
    if 'rubik' in s or 'f2l' in s:
        return 'Rubik cube'
    if any(k in s for k in ['nx', 'creo', 'gear', 'joint', 'aeroplane', 'geneva', 'ansys', 'beam', 'truss', 'industrial']):
        return 'CAD / mechanical (NX, Creo, ANSYS)'
    if any(k in s for k in ['html', 'web design', 'css']):
        return 'HTML / web'
    if 'youtube' in s or 'shadow fight' in s:
        return 'Random / unrelated'
    return 'C programming'


elsewhere = {}
for x in V[54:]:
    elsewhere.setdefault(cat(x['title']), []).append(x['title'])

GAPS = """| Not covered | Why it matters | Where to get it |
|---|---|---|
| Key Mapping / Value Mapping | Every real MDG project configures ID mapping for BP/customer/vendor | SAP Help: MDG Key and Value Mapping |
| DRF+ replication | Without it governance has no output - the CR activates but nothing reaches the target system | SAP Help: Replication via DRF+ (the channel has only a 2-minute visualization clip) |
| File upload / mass processing | How the business actually loads and mass-changes data | SAP Help: MDG file upload framework, mass processing |
| Consolidation and mass data | A separate MDG scenario, often in scope | SAP Help: Consolidation |
| Full DQM / address cleansing | The channel covers DQM validations only, not DQM cleansing | SAP Help: Data Quality Management |
| Authorizations | CR-type and entity-based authorizations are a standard interview topic | SAP Help: MDG authorizations |
| S/4HANA specifics, Fiori apps | Current projects are S/4; the videos are ECC-era screens | openSAP MDG course, SAP Help "MDG on S/4HANA" |"""

doc = """# SAP MDG - Study Roadmap

**Channel:** Koushik Konda ([@koushikkonda1994](https://www.youtube.com/@koushikkonda1994))
**Scope:** 54 SAP MDG videos · **%dh%02dm** of video · notes built from the transcripts of all 54
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
| Phase 0 - Orientation | 4 | %s | %s |
| Phase 1 - Data Modeling | 8 | %s | %s |
| Phase 2 - UI / Floorplan | 14 | %s | %s |
| Phase 3 - Process Modeling / Workflow | 11 | %s | %s |
| Phase 4 - Validations / Derivations | 13 | %s | %s |
| Phase 5 - Search / Duplicate Check | 4 | %s | %s |
| **Total** | **54** | **%dh%02dm** | |

**Three schedules - pick one**

| Plan | Pace | How it maps |
|---|---|---|
| **Sprint** | ~2h/day, 13 days | P0 day 1 · P1 days 2-4 · P2 days 5-7 · P3 days 8-10 · P4 days 11-12 · P5 day 13. Only works if you have a sandbox system. |
| **Standard** (recommended) | ~1h/day, 5 weeks | One phase per week; P1 and P4 take a full week each. Leaves time to actually configure. |
| **Weekend** | 2 weekends, ~6h/day | Weekend 1: P0+P1+P2 · Weekend 2: P3+P4+P5. Do the checkpoints on weekday evenings. |

---

""" % (
    total // 3600, (total % 3600) // 60,
    dur(PH[0][3]), PH[0][5], dur(PH[1][3]), PH[1][5], dur(PH[2][3]), PH[2][5],
    dur(PH[3][3]), PH[3][5], dur(PH[4][3]), PH[4][5], dur(PH[5][3]), PH[5][5],
    total // 3600, (total % 3600) // 60
) + "\n\n".join(secs) + """

## Appendix A - Master watch order (all 54)

| # | Video | Length | Phase |
|---|---|---|---|
""" + "\n".join(rows) + """

## Appendix B - The %d videos on this channel that are NOT SAP MDG

Do not open these while studying MDG - it is a different channel's worth of content sitting in the same feed:

""" % (len(V) - 54) + "\n".join(
    "- **%s** (%d): %s%s" % (k, len(t), ", ".join(t[:6]), " …" if len(t) > 6 else "")
    for k, t in elsewhere.items()
) + """

## Appendix C - What this channel does NOT teach

The 54 videos are strong on extension, UI, workflow, BRF+/BAdI and DQM validations. They are thin or silent on:

""" + GAPS + """

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
""" + "\n".join(
    "%d. [%s](https://youtu.be/%s) - %s views" % (n, x['title'], x['id'], format(x.get('view_count') or 0, ','))
    for n, x in enumerate(sorted((v[i] for i in ALL), key=lambda y: y.get('view_count') or 0, reverse=True)[:8], 1)
) + "\n"

open('ROADMAP.md', 'w', encoding='utf-8').write(doc)
print("ROADMAP.md:", len(doc), "chars |", len(ALL), "videos |", dur(ALL))
