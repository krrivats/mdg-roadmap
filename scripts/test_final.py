import json, os
from playwright.sync_api import sync_playwright
URL = "http://127.0.0.1:8123/index.html"
FILE = "file:///D:/Claude/Projects/SAP-MDG/docs/index.html"
out = {}
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    pg = b.new_page(viewport={"width": 1440, "height": 950})
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(URL, wait_until="load"); pg.wait_for_timeout(700)

    # italics + no raw asterisks left in rendered text
    out["raw_asterisks"] = pg.evaluate(
        "[...document.querySelectorAll('.v-body')].reduce((n,e)=>n+(e.textContent.split('*').length-1),0)")
    out["em_count"] = pg.evaluate("document.querySelectorAll('.v-body em').length")

    # keyboard: tab to the first row button and press Enter
    pg.evaluate("document.querySelector('.v-main').focus()")
    pg.keyboard.press("Enter"); pg.wait_for_timeout(500)
    out["keyboard_open"] = pg.evaluate("document.querySelectorAll('.v-row.is-open').length")

    # '/' shortcut
    pg.keyboard.press("Escape")
    pg.keyboard.press("/"); pg.wait_for_timeout(200)
    out["slash_focus"] = pg.evaluate("document.activeElement.id")

    # anchors land below the sticky bar
    pg.evaluate("location.hash='#phase-3'"); pg.wait_for_timeout(1200)
    out["anchor_top"] = pg.evaluate("Math.round(document.querySelector('#phase-3 .phase-head').getBoundingClientRect().top)")

    # file:// works
    f = b.new_page(viewport={"width": 1200, "height": 800})
    f.goto(FILE, wait_until="load"); f.wait_for_timeout(800)
    out["file_rows"] = f.evaluate("document.querySelectorAll('.v-row').length")
    out["file_pct"] = f.inner_text("#pct")

    # reduced motion respected
    r = b.new_page(viewport={"width": 1200, "height": 800}, reduced_motion="reduce")
    r.goto(URL, wait_until="load"); r.wait_for_timeout(400)
    out["reduced_transition"] = r.evaluate("getComputedStyle(document.querySelector('.v-panel')).transitionDuration")

    b.close()
out["errors"] = errs or "none"
print(json.dumps(out, indent=2))
