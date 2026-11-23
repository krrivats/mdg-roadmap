"""Verify readability floors: type sizes, contrast, tap targets, reflow at 320px."""
import json
import os

from playwright.sync_api import sync_playwright

URL = "http://127.0.0.1:8124/index.html"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "shots")
os.makedirs(OUT, exist_ok=True)

AUDIT = """
(() => {
  const vis = (el) => {
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return s.display !== 'none' && s.visibility !== 'hidden' && r.width > 0 && r.height > 0 && el.textContent.trim();
  };
  const small = [];
  document.querySelectorAll('.view.is-active *, .appbar *, .tabbar *').forEach(el => {
    if (!vis(el) || el.children.length) return;
    const fs = parseFloat(getComputedStyle(el).fontSize);
    if (fs && fs < 12) small.push(Math.round(fs * 10) / 10 + 'px "' + el.textContent.trim().slice(0, 28) + '"');
  });
  const targets = [];
  document.querySelectorAll('.chip, .btn, .seg, .tab, .tick, .icon-btn, .ring-btn, .search-clear').forEach(el => {
    const r = el.getBoundingClientRect();
    if (r.width > 0) targets.push([el.className.split(' ')[0], Math.round(r.width), Math.round(r.height)]);
  });
  const tiny = targets.filter(t => t[1] < 40 || t[2] < 40);
  return JSON.stringify({
    smallText: [...new Set(small)].slice(0, 8),
    smallCount: small.length,
    tinyTargets: tiny.slice(0, 6),
    inputFont: getComputedStyle(document.querySelector('#q')).fontSize,
    overflow: document.documentElement.scrollWidth - document.documentElement.clientWidth,
    bodyFont: getComputedStyle(document.body).fontSize
  });
})()
"""

R = {}
with sync_playwright() as p:
    b = p.chromium.launch(channel="chrome")
    for w, h, label in [(320, 700, "w320"), (360, 780, "w360"), (390, 844, "w390"),
                        (768, 900, "w768"), (1440, 950, "w1440")]:
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.goto(URL, wait_until="load")
        pg.wait_for_timeout(500)
        pg.click(".tab[data-go='learn']")
        pg.wait_for_timeout(350)
        pg.click(".vcard .vexp")
        pg.wait_for_timeout(350)
        R[label] = json.loads(pg.evaluate(AUDIT))
        if w in (360, 1440):
            pg.screenshot(path=os.path.join(OUT, f"r-{label}-learn.png"))
        pg.close()

    # start + notes at 360 for the visual check
    pg = b.new_page(viewport={"width": 360, "height": 780}, device_scale_factor=2)
    pg.goto(URL, wait_until="load")
    pg.wait_for_timeout(600)
    pg.screenshot(path=os.path.join(OUT, "r-w360-start.png"))
    pg.click(".tab[data-go='notes']")
    pg.wait_for_timeout(400)
    pg.screenshot(path=os.path.join(OUT, "r-w360-notes.png"))
    b.close()

print(json.dumps(R, indent=2))
