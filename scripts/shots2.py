import os
from playwright.sync_api import sync_playwright
OUT=os.path.join('shots'); URL="http://127.0.0.1:8123/index.html"
with sync_playwright() as p:
    b=p.chromium.launch(channel="chrome")
    pg=b.new_page(viewport={"width":1440,"height":950})
    pg.goto(URL,wait_until="load"); pg.wait_for_timeout(800)
    # expand video 5 of phase 1 and land on it cleanly
    pg.evaluate("document.querySelector('#phase-1').scrollIntoView()"); pg.wait_for_timeout(900)
    pg.evaluate("document.querySelectorAll('#phase-1 .v-main')[4].click()"); pg.wait_for_timeout(700)
    pg.evaluate("document.querySelector('#phase-1 .v-row.is-open').scrollIntoView({block:'start'})"); pg.wait_for_timeout(1400)
    pg.screenshot(path=os.path.join(OUT,"10-panel-clean.png"))
    # tip of page, light theme
    pg.evaluate("window.scrollTo({top:0,behavior:'instant'})"); pg.wait_for_timeout(900)
    pg.screenshot(path=os.path.join(OUT,"11-top-light.png"))
    # mobile with a row open
    m=b.new_page(viewport={"width":390,"height":844},device_scale_factor=2)
    m.goto(URL,wait_until="load"); m.wait_for_timeout(900)
    m.evaluate("document.querySelector('#phase-0 .v-main').click()"); m.wait_for_timeout(600)
    m.evaluate("document.querySelector('#phase-0').scrollIntoView()"); m.wait_for_timeout(1200)
    m.screenshot(path=os.path.join(OUT,"12-mobile-open.png"))
    b.close()
print("ok")
