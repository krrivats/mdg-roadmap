"""Readability pass: raise contrast, raise the type floor, fix iOS input zoom, 44px targets."""
import re
import sys

p = 'docs/styles.css'
s = open(p, encoding='utf-8').read()
orig = s


def sub(old, new, count=1):
    global s
    if old not in s:
        print('!! MISS:', old.split('\n')[0][:70])
        sys.exit(1)
    s = s.replace(old, new, count)


# ---------- 1. tokens: contrast + slightly lifted surfaces ----------
sub("""  --surface:   #12161b;
  --surface-2: #171d24;
  --surface-3: #1e252e;
  --line:      rgba(255,255,255,.075);
  --line-2:    rgba(255,255,255,.14);
  --ink:       #eef3f1;
  --ink-2:     #a3aea9;
  --ink-3:     #6b7772;""",
"""  --surface:   #14181e;
  --surface-2: #1a2028;
  --surface-3: #232b34;
  --line:      rgba(255,255,255,.09);
  --line-2:    rgba(255,255,255,.16);
  --ink:       #f2f6f4;
  --ink-2:     #c2ccc7;
  --ink-3:     #93a09b;""")

sub("""  --surface:   #ffffff;
  --surface-2: #f5f7f5;
  --surface-3: #eceff0;
  --line:      rgba(10,20,16,.10);
  --line-2:    rgba(10,20,16,.18);
  --ink:       #0b1210;
  --ink-2:     #45514c;
  --ink-3:     #74807a;""",
"""  --surface:   #ffffff;
  --surface-2: #f5f7f5;
  --surface-3: #eceff0;
  --line:      rgba(10,20,16,.11);
  --line-2:    rgba(10,20,16,.20);
  --ink:       #0b1210;
  --ink-2:     #384440;
  --ink-3:     #5a6763;""")

# ---------- 2. the grid should not compete with text ----------
sub("  opacity: .28;", "  opacity: .14;")
sub("[data-theme='light'] body::after { opacity: .32; }", "[data-theme='light'] body::after { opacity: .22; }")

# ---------- 3. type scale ----------
sub("""body {
  margin: 0;
  min-height: 100dvh;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font);
  font-size: 15px;
  line-height: 1.55;""",
"""body {
  margin: 0;
  min-height: 100dvh;
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font);
  font-size: 16px;
  line-height: 1.6;""")

sub("""p, li { }""", """p, li { }""") if "p, li { }" in s else None

sub(""".eyebrow {
  margin: 0 0 10px;
  font-family: var(--mono); font-size: 10px; font-weight: 500;
  letter-spacing: .2em; text-transform: uppercase; color: var(--ink-3);
}""",
""".eyebrow {
  margin: 0 0 10px;
  font-family: var(--mono); font-size: 11.5px; font-weight: 500;
  letter-spacing: .13em; text-transform: uppercase; color: var(--ink-3);
}""")

sub(".lede { margin: 0 0 22px; color: var(--ink-2); font-size: 15px; max-width: 46ch; }",
    ".lede { margin: 0 0 22px; color: var(--ink-2); font-size: 16px; line-height: 1.65; max-width: 52ch; text-wrap: pretty; }")

sub(""".sec-note {
  font-family: var(--mono); font-size: 10px; font-weight: 400;
  letter-spacing: .12em; text-transform: uppercase; color: var(--ink-3);
}""",
""".sec-note {
  font-family: var(--mono); font-size: 11px; font-weight: 400;
  letter-spacing: .1em; text-transform: uppercase; color: var(--ink-3);
}""")

sub("""code, kbd {
  font-family: var(--mono); font-size: .86em;""",
"""code, kbd {
  font-family: var(--mono); font-size: .88em;""")

# readouts
sub(".readout .k {\n  display: block; font-family: var(--mono); font-size: 9px; letter-spacing: .14em;",
    ".readout .k {\n  display: block; font-family: var(--mono); font-size: 11px; letter-spacing: .1em;")
sub(".readout b { font-family: var(--mono); font-size: 17px; font-weight: 500; letter-spacing: -.02em; }",
    ".readout b { font-family: var(--mono); font-size: 19px; font-weight: 500; letter-spacing: -.02em; }")

# CTA
sub(""".cta-k {
  display: block; font-family: var(--mono); font-size: 9px; letter-spacing: .18em;""",
""".cta-k {
  display: block; font-family: var(--mono); font-size: 10.5px; letter-spacing: .14em;""")
sub(""".cta-v {
  display: block; font-size: 14.5px; font-weight: 500;""",
""".cta-v {
  display: block; font-size: 16px; font-weight: 500;""")
sub(".cta-time { font-family: var(--mono); font-size: 11px; color: var(--ink-3); }",
    ".cta-time { font-family: var(--mono); font-size: 12px; color: var(--ink-2); }")

# rules
sub(".rule p { margin: 0; font-size: 13.5px; color: var(--ink-2); }",
    ".rule p { margin: 0; font-size: 14.5px; line-height: 1.6; color: var(--ink-2); text-wrap: pretty; }")

# card head
sub(""".vtitle {
  display: block; font-size: 15.5px; font-weight: 600; line-height: 1.32;
  letter-spacing: -.012em;
}""",
""".vtitle {
  display: block; font-size: 17px; font-weight: 600; line-height: 1.3;
  letter-spacing: -.014em; text-wrap: pretty;
}""")

sub(""".vone {
  display: block; margin-top: 4px;
  font-size: 13px; line-height: 1.5; color: var(--ink-3);
}""",
""".vone {
  display: block; margin-top: 6px;
  font-size: 14px; line-height: 1.55; color: var(--ink-2); text-wrap: pretty;
}""")

sub(".vnum {\n  font-family: var(--mono); font-size: 10px; color: var(--ink-3);",
    ".vnum {\n  font-family: var(--mono); font-size: 11.5px; color: var(--ink-3);")

# meta row
sub(""".vmeta {
  display: flex; align-items: center; gap: 8px;
  padding: 8px 14px 12px 42px;
  font-family: var(--mono); font-size: 10px; letter-spacing: .06em;
  color: var(--ink-3);
}""",
""".vmeta {
  display: flex; align-items: center; gap: 8px; flex-wrap: wrap;
  padding: 10px 16px 14px 42px;
  font-family: var(--mono); font-size: 12px; letter-spacing: .04em;
  color: var(--ink-2);
}""")

sub("""  padding: 3px 8px; border-radius: 999px;
  border: 1px solid var(--line-2);
  font-size: 9.5px; letter-spacing: .08em;""",
"""  padding: 4px 9px; border-radius: 999px;
  border: 1px solid var(--line-2);
  font-size: 11px; letter-spacing: .06em;""")

sub(".pill.lvl { text-transform: uppercase; letter-spacing: .12em; }",
    ".pill.lvl { text-transform: uppercase; letter-spacing: .09em; }")

# card body
sub(".vbody { padding: 2px 16px 18px 42px; }",
    ".vbody { padding: 6px 18px 20px 42px; }")

sub(""".bullets li {
  position: relative; padding-left: 15px;
  font-size: 13.5px; line-height: 1.6; color: var(--ink-2);
}""",
""".bullets li {
  position: relative; padding-left: 16px;
  font-size: 14.5px; line-height: 1.65; color: var(--ink-2);
  max-width: 68ch; text-wrap: pretty;
}""")

sub(""".insight {
  position: relative;
  padding: 12px 14px; margin: 0 0 12px;
  border-radius: 10px;
  background: var(--mint-dim);
  border: 1px solid rgba(92,233,192,.2);
  font-size: 13px; line-height: 1.6; color: var(--ink);
}""",
""".insight {
  position: relative;
  padding: 14px 16px; margin: 0 0 14px;
  border-radius: 10px;
  background: var(--mint-dim);
  border: 1px solid rgba(92,233,192,.28);
  font-size: 14.5px; line-height: 1.6; color: var(--ink);
  max-width: 68ch; text-wrap: pretty;
}""")

sub("""  font-family: var(--mono); font-size: 9px; letter-spacing: .16em; text-transform: uppercase;
  color: var(--mint);
}""",
"""  font-family: var(--mono); font-size: 10.5px; letter-spacing: .13em; text-transform: uppercase;
  color: var(--mint);
}""")

sub(".prereq { margin: 0 0 12px; font-size: 12px; color: var(--ink-3); line-height: 1.6; }",
    ".prereq { margin: 0 0 12px; font-size: 13.5px; color: var(--ink-2); line-height: 1.6; max-width: 68ch; }")
sub(".prereq b { font-family: var(--mono); font-size: 9px; letter-spacing: .14em;",
    ".prereq b { font-family: var(--mono); font-size: 10.5px; letter-spacing: .12em;")

sub(".extra { margin: 0 0 10px; font-size: 12.5px; color: var(--ink-2); }",
    ".extra { margin: 0 0 10px; font-size: 13.5px; line-height: 1.6; color: var(--ink-2); max-width: 68ch; }")
sub(".extra b { display: block; font-family: var(--mono); font-size: 9px; letter-spacing: .12em;",
    ".extra b { display: block; font-family: var(--mono); font-size: 10.5px; letter-spacing: .1em;")

sub("""  font-family: var(--mono); font-size: 10.5px; font-weight: 500;
  letter-spacing: .1em; text-transform: uppercase; text-decoration: none;""",
"""  font-family: var(--mono); font-size: 12px; font-weight: 500;
  letter-spacing: .08em; text-transform: uppercase; text-decoration: none;""")

# ---------- 4. iOS zoom: inputs and textarea must be >=16px ----------
sub("""  padding: 13px 10px; color: var(--ink); font-family: var(--font); font-size: 14px;
}""",
"""  padding: 13px 10px; color: var(--ink); font-family: var(--font); font-size: 16px;
}""")
sub("""  font-family: var(--mono); font-size: 12.5px; line-height: 1.9;
  padding: 12px 14px;""",
"""  font-family: var(--mono); font-size: 16px; line-height: 1.9;
  padding: 12px 14px;""")

# ---------- 5. touch targets ----------
sub("""  padding: 8px 13px; border-radius: 999px;
  border: 1px solid var(--line); background: var(--surface);
  color: var(--ink-2); cursor: pointer;
  font-family: var(--mono); font-size: 10.5px; letter-spacing: .08em; text-transform: uppercase;""",
"""  min-height: 44px; display: inline-flex; align-items: center;
  padding: 10px 15px; border-radius: 999px;
  border: 1px solid var(--line); background: var(--surface);
  color: var(--ink-2); cursor: pointer;
  font-family: var(--mono); font-size: 12px; letter-spacing: .06em; text-transform: uppercase;""")

sub(".chiprow-sub .chip { font-size: 10px; padding: 7px 11px; }",
    ".chiprow-sub .chip { font-size: 11.5px; padding: 9px 13px; }")

sub(""".result-line {
  margin: 0 0 10px; min-height: 16px;
  font-family: var(--mono); font-size: 10.5px; letter-spacing: .06em; color: var(--ink-3);
}""",
""".result-line {
  margin: 0 0 10px; min-height: 18px;
  font-family: var(--mono); font-size: 12px; letter-spacing: .04em; color: var(--ink-2);
}""")

sub(""".btn {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 11px 15px; border-radius: 12px;""",
""".btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 8px;
  min-height: 44px; padding: 11px 16px; border-radius: 12px;""")
sub("""  font-family: var(--mono); font-size: 10.5px; letter-spacing: .1em; text-transform: uppercase;
  cursor: pointer; transition: border-color .2s, background .2s, transform .16s;""",
"""  font-family: var(--mono); font-size: 12px; letter-spacing: .08em; text-transform: uppercase;
  cursor: pointer; transition: border-color .2s, background .2s, transform .16s;""")

sub(""".seg {
  padding: 9px 6px; border: 0; border-radius: 11px; cursor: pointer;
  background: none; color: var(--ink-2);
  font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase;""",
""".seg {
  min-height: 44px; padding: 10px 6px; border: 0; border-radius: 11px; cursor: pointer;
  background: none; color: var(--ink-2);
  font-family: var(--mono); font-size: 11.5px; letter-spacing: .06em; text-transform: uppercase;""")

# checkpoint / plan / notes text
sub("""  background: color-mix(in srgb, var(--surface) 60%, transparent);
  font-size: 13px; line-height: 1.6; color: var(--ink-2);
}""",
"""  background: color-mix(in srgb, var(--surface) 60%, transparent);
  font-size: 14.5px; line-height: 1.6; color: var(--ink-2); text-wrap: pretty;
}""")
sub("""  font-family: var(--mono); font-size: 9px; letter-spacing: .16em; text-transform: uppercase;
  color: var(--amber);
}""",
"""  font-family: var(--mono); font-size: 10.5px; letter-spacing: .13em; text-transform: uppercase;
  color: var(--amber);
}""")

sub(".plan-row .when { font-family: var(--mono); font-size: 10px; letter-spacing: .08em; text-transform: uppercase; color: var(--mint); }",
    ".plan-row .when { font-family: var(--mono); font-size: 11.5px; letter-spacing: .06em; text-transform: uppercase; color: var(--mint); }")
sub(".plan-row .what { font-size: 13px; }", ".plan-row .what { font-size: 14px; line-height: 1.5; }")
sub(".plan-row .amt { font-family: var(--mono); font-size: 10px; color: var(--ink-3); white-space: nowrap; }",
    ".plan-row .amt { font-family: var(--mono); font-size: 11.5px; color: var(--ink-2); white-space: nowrap; }")

sub(".load .lb { font-size: 13px; color: var(--ink-2); }", ".load .lb { font-size: 14px; color: var(--ink-2); }")
sub(".load .lv { font-family: var(--mono); font-size: 10px; color: var(--ink-3); align-self: center; }",
    ".load .lv { font-family: var(--mono); font-size: 11.5px; color: var(--ink-2); align-self: center; }")

sub(".gap h3 { font-size: 14px; font-weight: 600; margin-bottom: 3px; }",
    ".gap h3 { font-size: 15.5px; font-weight: 600; margin-bottom: 4px; }")
sub(".gap p { margin: 0; font-size: 12.5px; color: var(--ink-2); }",
    ".gap p { margin: 0; font-size: 13.5px; line-height: 1.6; color: var(--ink-2); }")
sub(".gap .where { margin-top: 5px; font-family: var(--mono); font-size: 10px; color: var(--mint); letter-spacing: .04em; }",
    ".gap .where { margin-top: 6px; font-family: var(--mono); font-size: 11.5px; color: var(--mint); letter-spacing: .02em; }")

sub(""".caveats li {
  position: relative; padding: 12px 14px 12px 34px;
  border-radius: 12px; background: var(--surface); border: 1px solid var(--line);
  font-size: 12.5px; line-height: 1.55; color: var(--ink-2);
}""",
""".caveats li {
  position: relative; padding: 14px 16px 14px 36px;
  border-radius: 12px; background: var(--surface); border: 1px solid var(--line);
  font-size: 13.5px; line-height: 1.6; color: var(--ink-2); text-wrap: pretty;
}""")

sub(".top-row a { font-size: 13px; text-decoration: none; }", ".top-row a { font-size: 14px; text-decoration: none; }")
sub(".top-row .views { font-family: var(--mono); font-size: 10px; color: var(--ink-3); }",
    ".top-row .views { font-family: var(--mono); font-size: 11.5px; color: var(--ink-2); }")
sub(".top-row .rank { font-family: var(--mono); font-size: 10px; color: var(--ink-3); }",
    ".top-row .rank { font-family: var(--mono); font-size: 11.5px; color: var(--ink-3); }")

sub(".foot-note { margin: 28px 0 0; font-size: 11.5px; color: var(--ink-3); line-height: 1.6; }",
    ".foot-note { margin: 28px 0 0; font-size: 13px; color: var(--ink-3); line-height: 1.6; max-width: 68ch; }")

sub(".journal-meta {\n  display: flex; justify-content: space-between; padding: 0 14px;\n  font-family: var(--mono); font-size: 9.5px;",
    ".journal-meta {\n  display: flex; justify-content: space-between; padding: 0 14px;\n  font-family: var(--mono); font-size: 11.5px;")

# tab labels
sub("""  font-family: var(--mono); font-size: 9px; letter-spacing: .1em; text-transform: uppercase;
  transition: color .2s, background .2s;""",
"""  font-family: var(--mono); font-size: 10.5px; letter-spacing: .08em; text-transform: uppercase;
  transition: color .2s, background .2s;""")

# tonight rows
sub(".trow a {\n  flex: 1; min-width: 0; font-size: 13.5px; text-decoration: none;",
    ".trow a {\n  flex: 1; min-width: 0; font-size: 14.5px; text-decoration: none;")
sub(".trow .mins { font-family: var(--mono); font-size: 10px; color: var(--ink-3); }",
    ".trow .mins { font-family: var(--mono); font-size: 12px; color: var(--ink-2); }")

# search clear button target
sub(""".search-clear {
  border: 0; background: var(--surface-3); color: var(--ink-2);
  width: 24px; height: 24px; border-radius: 50%; cursor: pointer;""",
""".search-clear {
  border: 0; background: var(--surface-3); color: var(--ink-2);
  width: 30px; height: 30px; border-radius: 50%; cursor: pointer;""")

# ---------- 6. desktop: title scale + measure ----------
sub("""  .display { font-size: 58px; }
  .lede { font-size: 16px; }
  .vtitle { font-size: 16.5px; }""",
"""  .display { font-size: 58px; }
  .lede { font-size: 17px; }
  .vtitle { font-size: 18px; }
  .vone { font-size: 14.5px; }""")

# ---------- 7. pretty wrapping + 320px safety ----------
s += """

/* ---------------- readability pass ---------------- */

h1, h2, h3 { text-wrap: balance; }
p, li { text-wrap: pretty; }

@media (max-width: 360px) {
  #screen { padding-left: 14px; padding-right: 14px; }
  .display { font-size: 30px; }
  .vtitle { font-size: 16px; }
  .vhead { padding: 12px 10px 0; }
  .vmeta { padding-left: 36px; padding-right: 12px; }
  .vbody { padding-left: 16px; padding-right: 12px; }
  .readouts { grid-template-columns: repeat(2, 1fr); }
  .cta { gap: 10px; padding: 12px 12px; }
}

@media (max-width: 899px) {
  .vbody { padding-left: 16px; padding-right: 14px; }
}
"""

if s == orig:
    print('no changes applied'); sys.exit(1)
open(p, 'w', encoding='utf-8').write(s)
print('styles patched,', len(s), 'bytes')
