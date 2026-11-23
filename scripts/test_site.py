"""Smoke-test the static site with Playwright: layout shots + interaction checks."""
import json
import os
import sys

from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:8123/index.html"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "shots")
os.makedirs(OUT, exist_ok=True)
errors = []
results = {}

with sync_playwright() as p:
    b = None
    for ch in ("chrome", "msedge", None):
        try:
            b = p.chromium.launch(channel=ch) if ch else p.chromium.launch()
            print("launched:", ch or "bundled")
            break
        except Exception as e:
            print("failed:", ch, str(e).splitlines()[0][:80])
    if b is None:
        raise SystemExit("no browser")
    page = b.new_page(viewport={"width": 1440, "height": 950}, device_scale_factor=1)
    page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.goto(URL, wait_until="load")
    page.wait_for_timeout(700)

    page.screenshot(path=os.path.join(OUT, "01-hero.png"))
    page.evaluate("document.querySelector('#tonight').scrollIntoView({block:'center'})")
    page.wait_for_timeout(250)
    page.screenshot(path=os.path.join(OUT, "01b-tonight.png"))
    page.evaluate("document.querySelector('#phase-0').scrollIntoView()")
    page.wait_for_timeout(300)
    page.screenshot(path=os.path.join(OUT, "02-phase0.png"))

    # expand a video in phase 1
    page.evaluate("document.querySelector('#phase-1 .v-main').click()")
    page.wait_for_timeout(600)
    page.evaluate("document.querySelector('#phase-1 .v-row.is-open').scrollIntoView({block:'start'})")
    page.wait_for_timeout(300)
    page.screenshot(path=os.path.join(OUT, "03-expanded.png"))
    results["panel_height"] = page.evaluate(
        "Math.round(document.querySelector('#phase-1 .v-row.is-open .v-panel').getBoundingClientRect().height)")

    # tick two videos
    page.evaluate("""
      const r = [...document.querySelectorAll('.v-row')].slice(0,2);
      r.forEach(x => x.querySelector('input[data-watch]').click());
    """)
    page.wait_for_timeout(400)
    results["pct_after_tick"] = page.inner_text("#pct")
    results["count_after_tick"] = page.inner_text("#count")
    results["time_after_tick"] = page.inner_text("#time-left")
    results["phase0_meta"] = page.inner_text("[data-phase-done='0']")

    # persistence across reload
    page.reload(wait_until="load")
    page.wait_for_timeout(600)
    results["pct_after_reload"] = page.inner_text("#pct")
    results["watched_rows_after_reload"] = page.evaluate("document.querySelectorAll('.v-row.is-watched').length")

    # search
    page.fill("#q", "BRF+")
    page.wait_for_timeout(350)
    results["search_count"] = page.inner_text("#result-count")
    results["visible_rows_search"] = page.evaluate(
        "[...document.querySelectorAll('.v-row')].filter(r => !r.hidden).length")
    page.screenshot(path=os.path.join(OUT, "04-search.png"))

    # clear search, filter advanced
    page.fill("#q", "")
    page.click(".chip[data-level='advanced']")
    page.wait_for_timeout(300)
    results["advanced_visible"] = page.evaluate(
        "[...document.querySelectorAll('.v-row')].filter(r => !r.hidden).length")
    results["advanced_all_advanced"] = page.evaluate(
        "[...document.querySelectorAll('.v-row')].filter(r => !r.hidden).every(r => r.querySelector('.stamp').textContent === 'advanced')")
    page.click(".chip[data-level='all']")

    # continue button
    page.click("#btn-continue")
    page.wait_for_timeout(800)
    results["continue_opened"] = page.evaluate("document.querySelectorAll('.v-row.is-open').length")
    results["continue_target"] = page.evaluate(
        "(document.querySelector('.v-row.is-open .v-title')||{}).textContent")

    # schedule tabs
    page.evaluate("document.querySelector('#schedule').scrollIntoView()")
    page.wait_for_timeout(300)
    page.click(".tab[data-sched='0']")
    page.wait_for_timeout(300)
    results["sprint_rows"] = page.evaluate("document.querySelectorAll('.sched-row').length")
    page.screenshot(path=os.path.join(OUT, "05-schedule.png"))

    # theme toggle
    page.click("#btn-theme")
    page.wait_for_timeout(300)
    results["theme_after_toggle"] = page.evaluate("document.documentElement.dataset.theme")
    page.evaluate("window.scrollTo(0,0)")
    page.wait_for_timeout(200)
    page.screenshot(path=os.path.join(OUT, "06-light.png"))

    # print stylesheet sanity
    page.click("#btn-theme")
    page.evaluate("document.querySelector('#phase-2').scrollIntoView()")
    page.wait_for_timeout(300)
    page.screenshot(path=os.path.join(OUT, "08-light-phase2.png"))
    page.emulate_media(media="print")
    page.wait_for_timeout(200)
    results["print_hides_rail"] = page.evaluate(
        "getComputedStyle(document.querySelector('.rail')).display")

    # mobile
    m = b.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=2)
    m.goto(URL, wait_until="load")
    m.wait_for_timeout(600)
    m.screenshot(path=os.path.join(OUT, "07-mobile.png"))
    results["mobile_overflow"] = m.evaluate(
        "document.documentElement.scrollWidth - document.documentElement.clientWidth")

    b.close()

print(json.dumps(results, indent=2))
print("CONSOLE ERRORS:", errors if errors else "none")
