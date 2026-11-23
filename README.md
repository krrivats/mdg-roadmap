# MDG Register

A mobile-first study app for the 54 SAP MDG videos on
[Koushik Konda's channel](https://www.youtube.com/@koushikkonda1994), ordered by SAP's own
configuration dependency chain instead of by upload date.

**Live:** https://krrivats.github.io/mdg-roadmap/

The channel has 123 videos; only 54 are MDG, and its "SAP MDG Technical" playlist is sorted
**newest first** — so it opens with a workflow edge case and ends with "MDG Overview for beginners".
This project fixes the order and attaches real notes to every video.

## What it is

| | |
|---|---|
| **Scope** | 6 phases · 54 videos · 25h 14m · 7 deliberately excluded topics listed |
| **Per video** | one-line summary, 3–5 key points with real object names, the gotcha, prerequisites |
| **Per phase** | a checkpoint you must be able to do without the video |
| **App shell** | tabs (Start / Learn / Plan / Notes), works like a native app, installable, offline-capable |
| **Tracking** | progress ring, per-phase bars, "Continue" jumps to your next unwatched video |
| **Search** | across titles *and* note text — try `CVI`, `BRF+`, `workflow` |
| **Privacy** | everything stays in `localStorage`. No accounts, no analytics, no network calls |

## Views

- **Start** — the pitch, four readouts, tonight's 41 minutes, the three ordering rules.
- **Learn** — one phase at a time, phase chips, level filters, search, expandable note cards, checkpoint, prev/next.
- **Plan** — three schedules (Sprint 13 days / Standard 5 weeks / Weekend 2), phase load bars, blind spots.
- **Notes** — a journal for your own notes, export, reset, caveats, most-watched videos.

On a phone the navigation is a bottom tab bar; from 900px up it becomes a floating left dock.

## Structure

```
docs/                    the app (this is what GitHub Pages serves)
  index.html             shell + static copy
  styles.css             design system, dark/light, print, reduced motion
  app.js                 router, rendering, progress, search
  data.js                generated from ROADMAP.md — never edit by hand
  manifest.webmanifest   installable app metadata
  sw.js                  offline shell (stale-while-revalidate)
  icon.svg               app icon
ROADMAP.md               readable roadmap, source of truth for the site
notes/                   raw per-video notes (batchA–F) + curriculum reasoning
data/                    channel metadata (transcripts are gitignored)
scripts/                 build_roadmap.py, build_site.py, test_site.py, test_app.py, test_final.py
```

## Run locally

```bash
cd docs
python -m http.server 8124
# http://127.0.0.1:8124
```

Opening `docs/index.html` from disk also works; only the service worker needs `http(s)`.

## Deploy to GitHub Pages

Plain static files, no build step.

1. Push this folder to a repository.
2. **Settings → Pages → Build and deployment**: source **Deploy from a branch**, branch **main**, folder **/docs**.
3. Open `https://<you>.github.io/<repo>/`.

`docs/.nojekyll` is committed so GitHub serves the files as-is.

### Updating content

`docs/data.js` is generated:

```bash
python scripts/build_roadmap.py   # ROADMAP.md   <- notes/batch*.md
python scripts/build_site.py      # docs/data.js <- ROADMAP.md
```

Commit and push; Pages redeploys. Bump `CACHE` in `docs/sw.js` when you change the shell so
returning visitors get the new version immediately.

## Tested

`scripts/test_app.py` and `test_final.py` drive the page in Chromium and assert: all 54 videos
render, ticks survive reload, the ring/phase bars update, search and level filters return the right
counts, phase chips switch content, "Continue" opens the next unwatched video, the back button
moves between tabs, print hides the chrome, mobile has zero horizontal overflow, and there are no
console errors. Layout is verified at 390×844 and 1440×950 in both themes.

## Accuracy

Object names come from YouTube auto-captions, so some are phonetically reconstructed — the flagged
ones are listed in Appendix D of `ROADMAP.md`. Verify those in SE37 / SE24 before quoting them.
Two videos have no captions and are marked title-based only.
