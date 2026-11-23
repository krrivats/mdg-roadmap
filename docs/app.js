/* MDG Register — app shell, router, progress. No dependencies, no network calls. */
(function () {
  'use strict';

  var D = window.MDG_DATA;
  var KEY = 'mdg.register.v2';
  var RING = 163.36;
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  var saved = {};
  try { saved = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { saved = {}; }

  var S = {
    view: 'start',
    phase: '0',
    level: 'all',
    q: '',
    unwatched: false,
    plan: 1,
    watched: new Set(Array.isArray(saved.watched) ? saved.watched : []),
    open: null
  };

  var ALL = D.phases.reduce(function (a, p) { return a.concat(p.videos); }, []);
  var TOTAL = ALL.reduce(function (s, v) { return s + v.seconds; }, 0);

  /* ---------------- utilities ---------------- */

  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  function md(s) {
    return esc(s)
      .replace(/`([^`]+)`/g, '<code>$1</code>')
      .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
      .replace(/(^|[^*])\*([^*\n]{1,120}?)\*(?!\*)/g, '$1<em>$2</em>');
  }

  function cap(s) { return s ? s.charAt(0).toUpperCase() + s.slice(1) : s; }

  function dur(sec) {
    sec = Math.max(0, Math.round(sec));
    var h = Math.floor(sec / 3600), m = Math.floor((sec % 3600) / 60);
    if (h) return h + 'h ' + m + 'm';
    if (sec < 60) return sec + 's';
    return m + 'm';
  }

  function phaseOf(id) {
    for (var i = 0; i < D.phases.length; i++) {
      if (D.phases[i].videos.some(function (v) { return v.id === id; })) return D.phases[i];
    }
    return null;
  }

  function persist() {
    try {
      localStorage.setItem(KEY, JSON.stringify({
        watched: Array.from(S.watched),
        theme: document.documentElement.getAttribute('data-theme'),
        journal: $('#journal') ? $('#journal').value : (saved.journal || '')
      }));
    } catch (e) { /* storage disabled */ }
  }

  function label(v) { return 'Mark "' + v.title + '" watched'; }

  /* ---------------- card + list builders ---------------- */

  function tickHTML(v, cls) {
    var on = S.watched.has(v.id);
    return '<label class="tick' + (cls ? ' ' + cls : '') + '" title="' + esc(label(v)) + '">' +
      '<input type="checkbox" data-watch="' + esc(v.id) + '"' + (on ? ' checked' : '') +
      ' aria-label="' + esc(label(v)) + '">' +
      '<span class="tbox"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5 6.5 12 13 4.5"/></svg></span></label>';
  }

  function cardHTML(v, opts) {
    opts = opts || {};
    var on = S.watched.has(v.id);
    var open = S.open === v.id;
    var pts = (v.bullets || []).length;
    return '<article class="vcard' + (on ? ' is-done' : '') + (open ? ' is-open' : '') + '" data-id="' + esc(v.id) + '">' +
      '<div class="vhead">' +
        '<button class="vexp" type="button" aria-expanded="' + open + '" aria-controls="p-' + esc(v.id) + '">' +
          '<span class="vnum">' + String(v.n).padStart(2, '0') + '</span>' +
          '<span class="vtext">' +
            '<span class="vtitle">' + esc(v.title) + '</span>' +
            (v.one ? '<span class="vone">' + md(v.one) + '</span>' : '') +
          '</span>' +
        '</button>' +
        tickHTML(v) +
      '</div>' +
      '<div class="vmeta">' +
        '<span class="pill">' + esc(v.length) + '</span>' +
        '<span class="pill lvl ' + esc(v.level) + '">' + esc(v.level) + '</span>' +
        (opts.phaseTag ? '<span class="pill">P' + esc(opts.phaseTag) + '</span>' : '') +
        '<span class="grow">' + pts + (pts === 1 ? ' note' : ' notes') +
          '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg></span>' +
      '</div>' +
      '<div class="vpanel" id="p-' + esc(v.id) + '"><div class="vinner">' + panelHTML(v) + '</div></div>' +
    '</article>';
  }

  function panelHTML(v) {
    var h = '<div class="vbody">';
    if (v.bullets && v.bullets.length) {
      h += '<ul class="bullets">' + v.bullets.map(function (b) { return '<li>' + md(b) + '</li>'; }).join('') + '</ul>';
    }
    if (v.insight) h += '<div class="insight"><b>Key insight</b>' + md(v.insight) + '</div>';
    if (v.prereq) h += '<p class="prereq"><b>Prereq</b>' + md(v.prereq) + '</p>';
    (v.extras || []).forEach(function (x) {
      h += '<p class="extra"><b>' + esc(x.label) + '</b>' + md(x.text) + '</p>';
    });
    h += '<div class="vactions"><a class="ylink" href="https://youtu.be/' + esc(v.id) + '" target="_blank" rel="noopener">Watch' +
      '<svg viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M7 17 17 7M9 7h8v8"/></svg></a></div>';
    h += '</div>';
    return h;
  }

  /* ---------------- views ---------------- */

  function buildTonight() {
    var host = $('#tonight-list');
    host.innerHTML = D.tonight.map(function (t) {
      var v = { id: t.id, title: t.title };
      return '<div class="trow" data-id="' + esc(t.id) + '">' +
        tickHTML(v) +
        '<a href="https://youtu.be/' + esc(t.id) + '" target="_blank" rel="noopener">' + esc(t.title) + '</a>' +
        '<span class="mins">' + esc(t.length) + '</span>' +
        '</div>';
    }).join('');
  }

  function buildChips() {
    $('#phase-chips').innerHTML = D.phases.map(function (p) {
      return '<button class="chip' + (S.phase === p.id ? ' is-on' : '') + '" data-phase="' + p.id + '" type="button" role="tab" aria-selected="' + (S.phase === p.id) + '">' +
        'P' + p.id + '<span class="c-n">' + p.videos.length + '</span></button>';
    }).join('');
  }

  function matches(v) {
    if (S.level !== 'all' && v.level !== S.level) return false;
    if (S.unwatched && S.watched.has(v.id)) return false;
    if (!S.q) return true;
    var hay = [v.title, v.one, v.length, v.level, v.id, v.insight, v.prereq]
      .concat(v.bullets || [])
      .concat((v.extras || []).map(function (x) { return x.label + ' ' + x.text; }))
      .join(' ').toLowerCase();
    return S.q.toLowerCase().split(/\s+/).filter(Boolean).every(function (t) { return hay.indexOf(t) > -1; });
  }

  function renderLearn() {
    var filtering = !!S.q || S.level !== 'all' || S.unwatched;
    var body = $('#learn-body');
    var p = D.phases.filter(function (x) { return x.id === S.phase; })[0];
    var foot = $('#phase-foot');
    var res = $('#result-line');

    if (filtering) {
      var hits = [];
      D.phases.forEach(function (ph) {
        ph.videos.forEach(function (v) { if (matches(v)) hits.push({ v: v, ph: ph }); });
      });
      $('#learn-eyebrow').textContent = 'Search';
      $('#learn-title').textContent = S.q ? '“' + S.q + '”' : 'Filtered';
      $('#phase-pct').textContent = hits.length;
      $('#phase-count').textContent = 'matches';
      res.textContent = hits.length + ' of ' + ALL.length + ' videos';
      body.innerHTML = hits.length
        ? hits.map(function (h) { return cardHTML(h.v, { phaseTag: h.ph.id }); }).join('')
        : '<p class="empty">Nothing matches. Clear the search or the level filter.</p>';
      foot.innerHTML = '';
    } else {
      $('#learn-eyebrow').textContent = 'Phase ' + p.id + ' · ' + p.videos.length + ' videos · ' + dur(p.seconds);
      $('#learn-title').textContent = p.title;
      res.textContent = '';
      body.innerHTML = p.videos.map(function (v) { return cardHTML(v); }).join('') +
        (p.checkpoint ? '<div class="checkpoint"><b>Checkpoint before moving on</b>' + md(cap(p.checkpoint.replace(/^\*\*Checkpoint:\*\*\s*/, ''))) + '</div>' : '');

      var idx = D.phases.indexOf(p);
      var prev = D.phases[idx - 1], next = D.phases[idx + 1];
      foot.innerHTML =
        '<button class="btn" data-nav="' + (prev ? prev.id : '') + '" type="button"' + (prev ? '' : ' disabled') + '>‹ Prev</button>' +
        '<button class="btn" id="btn-print" type="button">Print</button>' +
        '<button class="btn btn-next" data-nav="' + (next ? next.id : '') + '" type="button"' + (next ? '' : ' disabled') + '>' +
          (next ? 'Phase ' + next.id + ' ›' : 'Done') + '</button>';
    }

    buildChips();
    markScrollable();
    updateProgress();
  }

  function markScrollable() {
    $$('.chiprow').forEach(function (row) {
      row.classList.toggle('is-scrollable', row.scrollWidth - row.clientWidth > 4);
    });
  }

  function buildPlan() {
    $('#plan-tabs').innerHTML = D.schedule.map(function (s, i) {
      return '<button class="seg' + (i === S.plan ? ' is-on' : '') + '" data-plan="' + i + '" type="button" role="tab" aria-selected="' + (i === S.plan) + '">' + esc(s.name) + '</button>';
    }).join('');

    var sch = D.schedule[S.plan];
    $('#plan-body').innerHTML = sch.days.map(function (d) {
      var phs = d[1].map(function (id) { return D.phases.filter(function (p) { return p.id === id; })[0]; }).filter(Boolean);
      var vids = phs.reduce(function (a, p) { return a + p.videos.length; }, 0);
      var secs = phs.reduce(function (a, p) { return a + p.seconds; }, 0);
      return '<div class="plan-row">' +
        '<span class="when">' + esc(d[0]) + '</span>' +
        '<span class="what">' + phs.map(function (p) { return 'P' + p.id + ' <span>' + esc(p.title) + '</span>'; }).join('<br>') + '</span>' +
        '<span class="amt">' + vids + ' vid · ' + dur(secs) + '</span>' +
        '</div>';
    }).join('');

    $('#load-list').innerHTML = D.phases.map(function (p) {
      return '<div class="load" data-load="' + p.id + '">' +
        '<span class="lb">P' + p.id + ' · ' + esc(p.title) + '</span>' +
        '<span class="lv" data-load-n="' + p.id + '">0/' + p.videos.length + '</span>' +
        '<span class="bar"><i data-load-bar="' + p.id + '"></i></span>' +
        '</div>';
    }).join('');

    $('#gap-list').innerHTML = D.gaps.map(function (g) {
      return '<div class="gap"><h3>' + esc(g.topic) + '</h3><p>' + md(g.why) + '</p><div class="where">' + md(g.where) + '</div></div>';
    }).join('');

    $('#caveat-list').innerHTML = D.caveats.map(function (c) { return '<li>' + md(c) + '</li>'; }).join('');

    $('#top-list').innerHTML = D.top.map(function (t, i) {
      return '<div class="top-row"><span class="rank">' + String(i + 1).padStart(2, '0') + '</span>' +
        '<a href="https://youtu.be/' + esc(t.id) + '" target="_blank" rel="noopener">' + esc(t.title) + '</a>' +
        '<span class="views">' + (t.views / 1000).toFixed(1) + 'k</span></div>';
    }).join('');
  }

  /* ---------------- progress ---------------- */

  function updateProgress() {
    var n = ALL.filter(function (v) { return S.watched.has(v.id); }).length;
    var pct = ALL.length ? n / ALL.length : 0;

    var fg = $('#ring-fg');
    if (fg) fg.style.strokeDashoffset = String(RING * (1 - pct));
    $('#ring-pct').textContent = Math.round(pct * 100) + '%';
    $('#appbar-meta').textContent = n + ' / ' + ALL.length;

    D.phases.forEach(function (p) {
      var d = p.videos.filter(function (v) { return S.watched.has(v.id); }).length;
      var seg = $('[data-strip="' + p.id + '"]');
      if (seg) seg.style.width = (p.videos.length ? (d / p.videos.length) * 100 : 0) + '%';
      var cp = $('[data-chip-count="' + p.id + '"]');

      var ln = $('[data-load-n="' + p.id + '"]');
      if (ln) ln.textContent = d + '/' + p.videos.length;
      var lb = $('[data-load-bar="' + p.id + '"]');
      if (lb) lb.style.width = (p.videos.length ? (d / p.videos.length) * 100 : 0) + '%';
    });

    var cur = D.phases.filter(function (p) { return p.id === S.phase; })[0];
    if (cur && !S.q) {
      var cd = cur.videos.filter(function (v) { return S.watched.has(v.id); }).length;
      $('#phase-pct').textContent = Math.round((cd / cur.videos.length) * 100) + '%';
      $('#phase-count').textContent = cd + ' / ' + cur.videos.length;
    }

    // next unwatched
    var next = nextVideo();
    if (next) {
      $('#cta-next').textContent = next.v.title;
      $('#cta-time').textContent = next.v.length;
    } else {
      $('#cta-next').textContent = 'All 54 watched — review mode';
      $('#cta-time').textContent = '✓';
    }

    // sync rendered ticks + cards
    $$('.vcard').forEach(function (c) {
      var on = S.watched.has(c.dataset.id);
      c.classList.toggle('is-done', on);
      var inp = $('input[data-watch]', c);
      if (inp && inp.checked !== on) inp.checked = on;
    });
    $$('.trow').forEach(function (r) {
      var inp = $('input[data-watch]', r);
      if (inp) inp.checked = S.watched.has(r.dataset.id);
    });
  }

  function nextVideo() {
    for (var i = 0; i < D.phases.length; i++) {
      var p = D.phases[i];
      for (var j = 0; j < p.videos.length; j++) {
        if (!S.watched.has(p.videos[j].id)) return { v: p.videos[j], phase: p };
      }
    }
    return null;
  }

  /* ---------------- router ---------------- */

  function go(view, opts) {
    opts = opts || {};
    S.view = view;
    $$('.view').forEach(function (s) { s.classList.toggle('is-active', s.dataset.view === view); });
    $$('.tab').forEach(function (t) {
      var on = t.dataset.go === view;
      t.classList.toggle('is-on', on);
      if (on) t.setAttribute('aria-current', 'page'); else t.removeAttribute('aria-current');
    });
    if (location.hash !== '#' + view && !opts.silent) {
      try { history.pushState({ view: view }, '', '#' + view); } catch (e) { location.hash = view; }
    }
    if (!opts.keepScroll) window.scrollTo({ top: 0, behavior: opts.instant ? 'auto' : 'smooth' });
  }

  /* ---------------- interactions ---------------- */

  function openCard(id, opts) {
    S.open = S.open === id ? null : id;
    $$('.vcard').forEach(function (c) {
      var on = c.dataset.id === S.open;
      c.classList.toggle('is-open', on);
      var b = $('.vexp', c);
      if (b) b.setAttribute('aria-expanded', String(on));
    });
    if (S.open && opts && opts.scroll) {
      var el = $('.vcard[data-id="' + S.open + '"]');
      if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  function jumpToNext() {
    var nx = nextVideo();
    if (!nx) { go('learn'); return; }
    S.q = ''; S.level = 'all'; S.unwatched = false;
    $('#q').value = '';
    $$('.chip[data-level]').forEach(function (c) { c.classList.toggle('is-on', c.dataset.level === 'all'); });
    S.phase = nx.phase.id;
    S.open = nx.v.id;
    go('learn', { instant: true });
    renderLearn();
    var card = $('.vcard[data-id="' + nx.v.id + '"]');
    if (card) {
      card.scrollIntoView({ behavior: 'smooth', block: 'center' });
      card.classList.add('is-ping');
      setTimeout(function () { card.classList.remove('is-ping'); }, 1000);
    }
  }

  function wire() {
    document.addEventListener('click', function (e) {
      var tab = e.target.closest('.tab');
      if (tab) { go(tab.dataset.go); return; }

      var exp = e.target.closest('.vexp');
      if (exp) { openCard(exp.closest('.vcard').dataset.id); return; }

      var meta = e.target.closest('.vmeta');
      if (meta && !e.target.closest('a')) { openCard(meta.closest('.vcard').dataset.id); return; }

      var chip = e.target.closest('.chip');
      if (chip) {
        if (chip.dataset.phase !== undefined) {
          S.phase = chip.dataset.phase;
          renderLearn();
          var vh = document.querySelector('.view.is-active .view-head');
          if (vh) window.scrollTo({ top: Math.max(0, vh.getBoundingClientRect().top + window.scrollY - 70), behavior: 'smooth' });
          return;
        }
        if (chip.dataset.level !== undefined) {
          S.level = chip.dataset.level;
          $$('.chip[data-level]').forEach(function (c) { c.classList.toggle('is-on', c === chip); });
          renderLearn(); return;
        }
        if (chip.dataset.toggle === 'unwatched') {
          S.unwatched = !S.unwatched;
          chip.classList.toggle('is-on', S.unwatched);
          chip.setAttribute('aria-pressed', String(S.unwatched));
          renderLearn(); return;
        }
      }

      var nav = e.target.closest('[data-nav]');
      if (nav && nav.dataset.nav) { S.phase = nav.dataset.nav; S.q = ''; $('#q').value = ''; renderLearn(); window.scrollTo({ top: 0, behavior: 'smooth' }); return; }

      if (e.target.closest('#btn-print')) { window.print(); return; }

      var plan = e.target.closest('[data-plan]');
      if (plan) { S.plan = Number(plan.dataset.plan); buildPlan(); return; }

      if (e.target.closest('#btn-continue')) { jumpToNext(); return; }
      if (e.target.closest('#btn-progress')) { go('plan'); return; }
      if (e.target.closest('#q-clear')) { S.q = ''; $('#q').value = ''; $('#q-clear').hidden = true; renderLearn(); return; }
    });

    document.addEventListener('change', function (e) {
      if (!e.target.matches('[data-watch]')) return;
      var id = e.target.dataset.watch;
      if (e.target.checked) S.watched.add(id); else S.watched.delete(id);
      persist();
      updateProgress();
    });

    var q = $('#q');
    q.addEventListener('input', function () {
      S.q = q.value.trim();
      $('#q-clear').hidden = !S.q;
      renderLearn();
    });

    $('#btn-theme').addEventListener('click', function () {
      var cur = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', cur);
      var m = document.querySelector('meta[name="theme-color"]');
      if (m) m.setAttribute('content', cur === 'dark' ? '#0a0c0f' : '#e9edea');
      persist();
    });

    var j = $('#journal');
    var t;
    j.addEventListener('input', function () {
      $('#journal-status').textContent = 'saving…';
      var words = j.value.trim() ? j.value.trim().split(/\s+/).length : 0;
      $('#journal-count').textContent = words + ' words';
      clearTimeout(t);
      t = setTimeout(function () { persist(); $('#journal-status').textContent = 'saved locally'; }, 400);
    });

    $('#btn-export').addEventListener('click', function () {
      var payload = {
        exported: new Date().toISOString(),
        source: D.channel.url,
        watched: ALL.filter(function (v) { return S.watched.has(v.id); }).map(function (v) { return v.title + ' | ' + v.id; }),
        journal: j.value
      };
      var blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'mdg-progress.json';
      a.click();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 2000);
    });

    $('#btn-reset').addEventListener('click', function () {
      if (!S.watched.size) return;
      if (!window.confirm('Clear all ' + S.watched.size + ' ticks? Your notes stay.')) return;
      S.watched.clear();
      persist();
      updateProgress();
    });

    window.addEventListener('popstate', function () {
      var v = (location.hash || '').replace('#', '');
      go(['start', 'learn', 'plan', 'notes'].indexOf(v) > -1 ? v : 'start', { silent: true });
    });

    document.addEventListener('keydown', function (e) {
      var tag = (e.target.tagName || '').toLowerCase();
      var typing = tag === 'input' || tag === 'textarea';
      if (e.key === '/' && !typing) { e.preventDefault(); go('learn'); q.focus(); }
      if (e.key === 'Escape' && document.activeElement === q) {
        q.value = ''; S.q = ''; $('#q-clear').hidden = true; renderLearn(); q.blur();
      }
    });
  }

  /* ---------------- boot ---------------- */

  function boot() {
    var theme = saved.theme || 'dark';
    document.documentElement.setAttribute('data-theme', theme);

    $('#progress-strip').innerHTML = D.phases.map(function (p) {
      return '<span class="seg" style="flex:' + p.videos.length + ' 1 0"><i data-strip="' + p.id + '"></i></span>';
    }).join('');

    buildTonight();
    buildChips();
    buildPlan();
    renderLearn();
    wire();
    markScrollable();
    window.addEventListener('resize', markScrollable);
    updateProgress();

    var j = $('#journal');
    if (typeof saved.journal === 'string') {
      j.value = saved.journal;
      var w = j.value.trim() ? j.value.trim().split(/\s+/).length : 0;
      $('#journal-count').textContent = w + ' words';
    }

    var startView = (location.hash || '').replace('#', '');
    go(['start', 'learn', 'plan', 'notes'].indexOf(startView) > -1 ? startView : 'start', { instant: true, keepScroll: true });

    if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) {
      navigator.serviceWorker.register('sw.js').catch(function () {});
    }
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
