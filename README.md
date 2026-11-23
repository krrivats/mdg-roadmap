# SAP MDG · Study Register

A single-page study tracker for the 54 SAP MDG videos on
[Koushik Konda's channel](https://www.youtube.com/@koushikkonda1994), ordered by SAP's own
configuration dependency chain instead of by upload date.

The channel has 123 videos; only 54 are MDG, and its "SAP MDG Technical" playlist is sorted
**newest first** — so it opens with a workflow edge case and ends with "MDG Overview for beginners".
This project fixes the order and attaches real notes to every video.

- 6 phases · 54 videos · 25h 14m
- Per video: one-line summary, 3–5 key points with real object names, the gotcha, prerequisites
- Per phase: a checkpoint you must be able to do without the video
- Progress is stored in the browser (localStorage), no accounts, no tracking

## Where things are

```
ROADMAP.md            the readable roadmap (source of truth for the site)
docs/                 the website (this is what gets deployed)
  index.html          markup + copy
  styles.css          ledger design, light + dark, print stylesheet
  app.js              rendering, filtering, progress, notes
  data.js             generated from ROADMAP.md — do not edit by hand
notes/                raw per-video notes (batchA–F) + curriculum reasoning
data/                 channel metadata + video transcripts (vtt/txt)
scripts/              build_roadmap.py, build_site.py, test_*.py
```

## Run it locally

Either just open `docs/index.html` in a browser (it works from `file://`), or serve it:

```bash
cd docs
python -m http.server 8123
# http://127.0.0.1:8123
```

## Deploy to GitHub Pages

The site is plain static files with no build step, so deployment is a settings change.

1. Create a repository and push this folder:

   ```bash
   git init
   git add .
   git commit -m "SAP MDG study register"
   git branch -M main
   git remote add origin https://github.com/<you>/<repo>.git
   git push -u origin main
   ```

2. On GitHub: **Settings → Pages → Build and deployment**
   - Source: **Deploy from a branch**
   - Branch: **main**, folder: **/docs**
   - Save.

3. Wait for the green check, then open `https://<you>.github.io/<repo>/`.

`docs/.nojekyll` is already there, so GitHub serves the files as-is instead of running Jekyll.

> If you would rather deploy from the repository root, move the contents of `docs/` to the root and
> pick **/ (root)** in step 2. Nothing in the site depends on the folder name.

### Updating the content later

`docs/data.js` is generated, never hand-edited:

```bash
python scripts/build_roadmap.py   # ROADMAP.md  <- notes/batch*.md
python scripts/build_site.py      # docs/data.js <- ROADMAP.md
```

Then commit and push; Pages redeploys automatically.

## Tested

`python scripts/test_site.py` and `scripts/test_final.py` drive the page in Chromium and check:
54 rows render, ticks survive reload, search and level filters work, "Continue" jumps to the next
unwatched video, the theme toggle persists, print hides the chrome, mobile has no horizontal
overflow, `file://` works, and there are no console errors.

## Notes on accuracy

Object names come from YouTube auto-captions, so some are phonetically reconstructed — the flagged
ones are listed in `ROADMAP.md` (Appendix D). Verify those in SE37 / SE24 before quoting them in an
interview. Two videos have no captions at all and are marked title-based only.

Progress and night notes live only in your browser. Export them with the **Export progress (.json)**
button before clearing site data.
