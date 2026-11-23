"""Parse ROADMAP.md into docs/data.js for the static site."""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SRC = open('ROADMAP.md', encoding='utf-8').read()

LABELS = {
    'Key insight': 'insight',
    'Prereq': 'prereq',
}


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def split_phases(text):
    out = []
    for m in re.finditer(r'^## (Phase \d .+)$', text, re.M):
        start = m.end()
        nxt = re.search(r'^## ', text[start:], re.M)
        body = text[start:start + nxt.start()] if nxt else text[start:]
        out.append((m.group(1).strip(), body))
    return out


def parse_video(block):
    head, _, rest = block.partition('\n')
    m = re.match(r'### (\d+)\. (.+)$', head)
    num, title = int(m.group(1)), m.group(2).strip()

    meta = re.search(r'\*\*ID:\*\* \[(\S+)\]\(\S+\) \| \*\*Length:\*\* ([^|]+)\| \*\*Level:\*\* (\w+)', rest)
    vid, length, level = meta.group(1), meta.group(2).strip(), meta.group(3)

    one = ''
    m = re.search(r'\*\*(?:In one line|One line):\*\*\s*(.+)', rest)
    if m:
        one = norm(m.group(1))

    bullets = [norm(x) for x in re.findall(r'^- (.+)$', rest, re.M)]

    fields = []
    cur = None
    for line in rest.splitlines():
        line = line.rstrip()
        if not line or line.startswith('---') or line.startswith('### '):
            continue
        mm = re.match(r'^\*\*([A-Za-z][^*]{1,45}):\*\*\s*(.*)$', line)
        if mm:
            cur = [mm.group(1).strip(), mm.group(2).strip()]
            fields.append(cur)
            continue
        if cur is not None:
            cur[1] = (cur[1] + ' ' + line.strip()).strip()

    insight = prereq = ''
    extras = []
    for label, txt in fields:
        key = LABELS.get(label)
        if key == 'insight':
            insight = norm(txt)
        elif key == 'prereq':
            prereq = norm(txt)
        elif label not in ('ID', 'Length', 'Level', 'In one line'):
            extras.append({'label': label, 'text': norm(txt)})

    def secs(s):
        s = s.strip()
        m = re.match(r'^(\d+)h(\d+)?m?$', s)
        if m:
            return int(m.group(1)) * 3600 + int(m.group(2) or 0) * 60
        m = re.match(r'^(\d+)m(\d+)s$', s)
        if m:
            return int(m.group(1)) * 60 + int(m.group(2))
        m = re.match(r'^(\d+)m$', s)
        if m:
            return int(m.group(1)) * 60
        return 0

    return {
        'n': num, 'title': title, 'id': vid, 'length': length, 'seconds': secs(length),
        'level': level, 'one': one, 'bullets': bullets,
        'insight': insight, 'prereq': prereq, 'extras': extras,
    }


phases = []
for title, body in split_phases(SRC):
    intro_lines = []
    for line in body.splitlines():
        if line.startswith('### ') or line.startswith('**Checkpoint:'):
            break
        intro_lines.append(line)
    intro = '\n'.join(intro_lines)
    intro = re.sub(r'^\s*\*\*\d+ videos[^\n]*\*\*\s*', '', intro).strip()
    done = re.search(r'\*\*Checkpoint:\*\*\s*(.+?)(?:\n\n---|\n---|$)', body, re.S)
    checkpoint = norm(done.group(1)) if done else ''
    raw_videos = re.split(r'\n(?=### \d+\. )', body)
    videos = [parse_video(b) for b in raw_videos if b.lstrip().startswith('### ')]
    pid = title.split()[1]
    phases.append({
        'id': pid, 'title': re.sub(r'^Phase \d+ - ', '', title), 'full': title,
        'intro': intro, 'checkpoint': checkpoint, 'videos': videos,
        'seconds': sum(v['seconds'] for v in videos),
    })

# ---- extras parsed from appendices ----
app_c = SRC.split('## Appendix C')[1].split('## Appendix D')[0]
gaps = []
for line in app_c.splitlines():
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    if len(cells) == 3 and cells[0] not in ('Not covered', '---') and not cells[0].startswith('---'):
        gaps.append({'topic': cells[0], 'why': cells[1], 'where': cells[2]})

app_d = SRC.split('## Appendix D')[1].split('## Appendix E')[0]
caveats = [norm(x) for x in re.findall(r'^- (.+)$', app_d, re.M)]

app_b = SRC.split('## Appendix B')[1].split('## Appendix C')[0]
nonmdg = []
for line in app_b.splitlines():
    m = re.match(r'^- \*\*(.+?)\*\* \((\d+)\): (.+)$', line)
    if m:
        nonmdg.append({'group': m.group(1), 'count': int(m.group(2)), 'items': m.group(3)})

app_e = SRC.split('## Appendix E')[1]
top = []
for m in re.finditer(r'^\d+\. \[(.+?)\]\(https://youtu\.be/(\S+?)\) - ([\d,]+) views', app_e, re.M):
    top.append({'title': m.group(1), 'id': m.group(2), 'views': int(m.group(3).replace(',', ''))})

tonight = re.findall(r'^\d+\. \[(.+?)\]\(https://youtu\.be/(\S+?)\) - (\d+m)', SRC.split('## Start here')[1].split('## At a glance')[0], re.M)

total_secs = sum(p['seconds'] for p in phases)

# authoritative durations from the YouTube metadata (notes round to whole minutes)
REAL = {x['id']: (x['duration'] or 0) for x in json.load(open('data/videos.json', encoding='utf-8'))['entries']}
for p in phases:
    for v in p['videos']:
        if REAL.get(v['id']):
            v['seconds'] = int(REAL[v['id']])
    p['seconds'] = sum(v['seconds'] for v in p['videos'])
total_secs = sum(p['seconds'] for p in phases)
data = {
    'channel': {
        'name': 'Koushik Konda',
        'handle': '@koushikkonda1994',
        'url': 'https://www.youtube.com/@koushikkonda1994',
        'videos': 123,
        'mdg': len([v for p in phases for v in p['videos']]),
        'seconds': total_secs,
    },
    'phases': [{
        'id': p['id'], 'title': p['title'], 'intro': p['intro'],
        'checkpoint': p['checkpoint'], 'seconds': p['seconds'],
        'videos': p['videos'],
    } for p in phases],
    'tonight': [{'title': t, 'id': i, 'length': l} for t, i, l in tonight],
    'gaps': gaps, 'caveats': caveats, 'nonmdg': nonmdg, 'top': top,
    'schedule': [
        {'name': 'Sprint', 'pace': '~2h/day · 13 days', 'days': [
            ['Day 1', ['P0']], ['Days 2-4', ['P1']], ['Days 5-7', ['P2']],
            ['Days 8-10', ['P3']], ['Days 11-12', ['P4']], ['Day 13', ['P5']]]},
        {'name': 'Standard', 'pace': '~1h/day · 5 weeks', 'days': [
            ['Week 1', ['P0', 'P1']], ['Week 2', ['P2']], ['Week 3', ['P3']],
            ['Week 4', ['P4']], ['Week 5', ['P5']]]},
        {'name': 'Weekend', 'pace': '~6h/day · 2 weekends', 'days': [
            ['Weekend 1', ['P0', 'P1', 'P2']], ['Weekend 2', ['P3', 'P4', 'P5']]]},
    ],
}

os.makedirs('docs', exist_ok=True)
with open('docs/data.js', 'w', encoding='utf-8') as f:
    f.write('window.MDG_DATA = ')
    json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
    f.write(';\n')

nv = sum(len(p['videos']) for p in phases)
bad = [v['title'] for p in phases for v in p['videos'] if not v['one'] or not v['bullets']]
print('phases', len(phases), '| videos', nv, '| total', total_secs // 3600, 'h', (total_secs % 3600) // 60, 'm')
print('incomplete blocks:', bad)
print('gaps', len(gaps), '| caveats', len(caveats), '| nonmdg groups', len(nonmdg), '| top', len(top), '| tonight', len(tonight))
print('per phase:', [(p['id'], len(p['videos'])) for p in phases])
