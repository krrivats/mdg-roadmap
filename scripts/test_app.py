"""Test the app-style rebuild: views, cards, persistence, PWA bits."""
import json
import os

from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:8124/index.html"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "shots")
os.makedirs(OUT, exist_ok=True)
R = {}
errs = []

with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    ctx = b.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2,
                        service_workers="block")
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.on("console", lambda m: errs.append("console: " + m.text) if m.type == "error" else None)
    pg.goto(URL, wait_until="load")
    pg.wait_for_timeout(700)

    R["view_on_load"] = pg.get_attribute(".view.is-active", "data-view")
    R["cards_start_view"] = pg.evaluate("document.querySelectorAll('#tonight-list .trow').length")
    pg.screenshot(path=os.path.join(OUT, "m1-start.png"))

    # learn view
    pg.click(".tab[data-go='learn']")
    pg.wait_for_timeout(500)
    R["learn_cards"] = pg.evaluate("document.querySelectorAll('#learn-body .vcard').length")
    R["learn_title"] = pg.inner_text("#learn-title")
    pg.screenshot(path=os.path.join(OUT, "m2-learn.png"))

    # expand first card
    pg.click(".vcard .vexp")
    pg.wait_for_timeout(500)
    R["expanded_h"] = pg.evaluate("Math.round(document.querySelector('.vcard.is-open .vpanel').getBoundingClientRect().height)")
    pg.evaluate("document.querySelector('.vcard.is-open').scrollIntoView({block:'start'})")
    pg.wait_for_timeout(400)
    pg.screenshot(path=os.path.join(OUT, "m3-card-open.png"))

    # tick two, check ring + persistence
    pg.evaluate("""
      const t=[...document.querySelectorAll('#learn-body .tick input')].slice(0,2);
      t.forEach(x=>x.click());
    """)
    pg.wait_for_timeout(400)
    R["ring_after"] = pg.inner_text("#ring-pct")
    R["meta_after"] = pg.inner_text("#appbar-meta")
    pg.reload(wait_until="load"); pg.wait_for_timeout(700)
    R["view_after_reload"] = pg.get_attribute(".view.is-active", "data-view")
    R["ring_after_reload"] = pg.inner_text("#ring-pct")
    R["done_cards_after_reload"] = pg.evaluate("document.querySelectorAll('.vcard.is-done').length")

    # search
    pg.fill("#q", "CVI")
    pg.wait_for_timeout(400)
    R["search_hits"] = pg.evaluate("document.querySelectorAll('#learn-body .vcard').length")
    R["search_line"] = pg.inner_text("#result-line")
    pg.screenshot(path=os.path.join(OUT, "m4-search.png"))
    pg.click("#q-clear")
    pg.wait_for_timeout(300)

    # phase chips
    pg.click(".chip[data-phase='3']")
    pg.wait_for_timeout(400)
    R["phase3_title"] = pg.inner_text("#learn-title")
    R["phase3_cards"] = pg.evaluate("document.querySelectorAll('#learn-body .vcard').length")

    # level filter
    pg.click("#btn-filters"); pg.wait_for_timeout(250); pg.click(".chip[data-level='advanced']")
    pg.wait_for_timeout(300)
    R["advanced_hits"] = pg.evaluate("document.querySelectorAll('#learn-body .vcard').length")
    R["advanced_only"] = pg.evaluate("[...document.querySelectorAll('#learn-body .vcard .pill.lvl')].every(e=>e.textContent.trim()==='advanced')")
    pg.click(".chip[data-level='all']")
    pg.wait_for_timeout(200)

    # plan + notes
    pg.click(".tab[data-go='plan']")
    pg.wait_for_timeout(400)
    R["plan_rows"] = pg.evaluate("document.querySelectorAll('.plan-row').length")
    R["gaps"] = pg.evaluate("document.querySelectorAll('.gap').length")
    pg.screenshot(path=os.path.join(OUT, "m5-plan.png"))

    pg.click(".tab[data-go='notes']")
    pg.wait_for_timeout(400)
    R["caveats"] = pg.evaluate("document.querySelectorAll('.caveats li').length")
    pg.screenshot(path=os.path.join(OUT, "m6-notes.png"))

    # continue jumps to next unwatched
    pg.click(".tab[data-go='start']"); pg.wait_for_timeout(300)
    R["cta_next"] = pg.inner_text("#cta-next")
    pg.click("#btn-continue"); pg.wait_for_timeout(900)
    R["continue_view"] = pg.get_attribute(".view.is-active", "data-view")
    R["continue_open"] = pg.evaluate("document.querySelectorAll('.vcard.is-open').length")

    # overflow check
    R["mobile_overflow"] = pg.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
    ctx.close()

    # desktop
    d = b.new_context(viewport={"width": 1440, "height": 950}, service_workers="block")
    dp = d.new_page()
    dp.goto(URL, wait_until="load"); dp.wait_for_timeout(700)
    dp.screenshot(path=os.path.join(OUT, "d1-start.png"))
    dp.click(".tab[data-go='learn']"); dp.wait_for_timeout(500)
    dp.screenshot(path=os.path.join(OUT, "d2-learn.png"))
    R["dock_position"] = dp.evaluate("getComputedStyle(document.querySelector('.tabbar')).position")

    # light theme
    dp.click("#btn-theme"); dp.wait_for_timeout(400)
    dp.screenshot(path=os.path.join(OUT, "d3-light.png"))
    R["theme"] = dp.evaluate("document.documentElement.dataset.theme")
    b.close()

R["errors"] = errs or "none"
print(json.dumps(R, indent=2))
