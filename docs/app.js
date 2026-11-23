/* SAP MDG · Study Register — vanilla JS, no build step, no network calls. */
(function () {
  'use strict';

  var D = window.MDG_DATA;
  var KEY = 'mdg.register.v1';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------------- state ---------------- */

  var saved = {};
  try { saved = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { saved = {}; }

  var state = {
    watched: new Set(Array.isArray(saved.watched) ? saved.watched : []),
    level: 'all',
    q: '',
    unwatchedOnly: false,
    schedule: 1
  };

  function persist() {
    try {
      localStorage.setItem(KEY, JSON.stringify({
        watched: Array.from(state.watched),
        theme: document.documentElement.getAttribute('data-theme') || 'light',
        journal: $('#journal') ? $('#journal').value : (saved.journal || '')
      }));
    } catch (e) { /* private mode */ }
  }

  /* ---------------- helpers ---------------- */

  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  }

  // tiny inline markdown: `code` and **bold**
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
    if (h && m) return h + 'h ' + m + 'm';
    if (h) return h + 'h';
    if (sec < 60) return sec + 's';
    return m + 'm';
  }

  function allVideos() {
    return D.phases.reduce(function (a, p) { return a.concat(p.videos); }, []);
  }

  function phaseById(id) {
    return D.phases.filter(function (p) { return p.id === id; })[0];
  }

  var ALL = allVideos();
  var TOTAL_SECONDS = ALL.reduce(function (s, v) { return s + v.seconds; }, 0);

  /* ---------------- static sections ---------------- */

  function buildTonight() {
    var host = $('#tonight-list');
    host.innerHTML = D.tonight.map(function (t) {
      var watched = state.watched.has(t.id);
      return '<div class="tonight-item">' +
        tickHTML(t.id, watched, 'Mark "' + esc(t.title) + '" watched') +
        '<a href="https://youtu.be/' + esc(t.id) + '" target="_blank" rel="noopener" style="text-decoration:none">' + esc(t.title) + '</a>' +
        '<span class="v-dur">' + esc(t.length) + '</span>' +
        '</div>';
    }).join('');
  }

  function tickHTML(id, watched, label) {
    return '<label class="tick" title="' + esc(label) + '">' +
      '<input type="checkbox" data-watch="' + esc(id) + '"' + (watched ? ' checked' : '') + ' aria-label="' + esc(label) + '">' +
      '<span class="box"><svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5 6.5 12 13 4.5"/></svg></span>' +
      '</label>';
  }

  function buildPhases() {
    var host = $('#phases');
    host.innerHTML = D.phases.map(function (p) {
      var pSec = p.videos.reduce(function (s, v) { return s + v.seconds; }, 0);
      var rows = p.videos.map(function (v) { return videoRow(v); }).join('');
      return '<section class="phase" id="phase-' + p.id + '" data-phase="' + p.id + '">' +
        '<div class="phase-head">' +
        '<div><p class="eyebrow">Phase ' + p.id + ' · ' + p.videos.length + ' videos</p>' +
        '<h2>' + esc(p.title) + '</h2></div>' +
        '<div class="phase-meta"><b data-phase-done="' + p.id + '">0/' + p.videos.length + '</b> watched<br>' + dur(pSec) + '</div>' +
        '</div>' +
        introHTML(p.intro) +
        '<div class="phase-list" data-list="' + p.id + '">' + rows + '</div>' +
        (p.checkpoint ? '<div class="checkpoint"><b>Checkpoint before moving on</b>' + md(cap(p.checkpoint.replace(/^\*\*Checkpoint:\*\*\s*/, ''))) + '</div>' : '') +
        '</section>';
    }).join('');
  }

  function introHTML(text) {
    if (!text) return '';
    var parts = text.split(/\n\n+/).filter(Boolean).map(function (t) { return '<p>' + md(t.replace(/\n/g, ' ')) + '</p>'; });
    return '<div class="phase-intro">' + parts.join('') + '</div>';
  }

  function videoRow(v) {
    var watched = state.watched.has(v.id);
    return '<article class="v-row' + (watched ? ' is-watched' : '') + '" data-id="' + esc(v.id) + '">' +
      tickHTML(v.id, watched, 'Mark "' + esc(v.title) + '" watched') +
      '<button class="v-main" type="button" aria-expanded="false" aria-controls="panel-' + esc(v.id) + '">' +
        '<span class="v-num">' + String(v.n).padStart(2, '0') + '</span>' +
        '<span class="v-text"><span class="v-title">' + esc(v.title) + '</span>' +
        (v.one ? '<span class="v-one">' + md(v.one) + '</span>' : '') + '</span>' +
        '<span class="v-dur">' + esc(v.length) + '</span>' +
        '<span class="stamp ' + esc(v.level) + '">' + esc(v.level) + '</span>' +
        '<svg class="chev" viewBox="0 0 16 16" aria-hidden="true"><path d="M4 6.5 8 10.5 12 6.5"/></svg>' +
      '</button>' +
      '<div class="v-panel" id="panel-' + esc(v.id) + '"><div class="v-panel-inner">' +
        panelHTML(v) +
      '</div></div>' +
      '</article>';
  }

  function panelHTML(v) {
    var h = '<div class="v-body">';
    if (v.bullets && v.bullets.length) {
      h += '<ul class="v-bullets">' + v.bullets.map(function (b) { return '<li>' + md(b) + '</li>'; }).join('') + '</ul>';
    }
    if (v.insight) h += '<div class="insight"><b>Key insight</b>' + md(v.insight) + '</div>';
    if (v.prereq) h += '<p class="vprereq"><b>Prereq</b> ' + md(v.prereq) + '</p>';
    (v.extras || []).forEach(function (x) {
      h += '<p class="v-extra"><b>' + esc(x.label) + '</b>' + md(x.text) + '</p>';
    });
    h += '<div class="v-actions">' +
      '<a class="v-link" href="https://youtu.be/' + esc(v.id) + '" target="_blank" rel="noopener">Watch on YouTube ↗</a>' +
      '</div></div>';
    return h;
  }

  function buildRail() {
    $('#rail-list').innerHTML = D.phases.map(function (p) {
      return '<li><a href="#phase-' + p.id + '" data-rail="' + p.id + '">' +
        '<span class="idx">0' + p.id + '</span>' +
        '<span>' + esc(p.title) + '</span>' +
        '<span class="done" data-rail-done="' + p.id + '">0/' + p.videos.length + '</span>' +
        '</a></li>';
    }).join('');

    $('#meter-bars').innerHTML = D.phases.map(function (p) {
      return '<span class="seg" style="flex:' + p.videos.length + ' 1 0" title="Phase ' + p.id + '">' +
        '<i data-meter="' + p.id + '"></i></span>';
    }).join('');
  }

  function buildSchedule() {
    $('#schedule-tabs').innerHTML = D.schedule.map(function (s, i) {
      return '<button class="tab' + (i === state.schedule ? ' is-on' : '') + '" data-sched="' + i + '" type="button" role="tab" aria-selected="' + (i === state.schedule) + '">' +
        esc(s.name) + ' · ' + esc(s.pace) + '</button>';
    }).join('');

    var s = D.schedule[state.schedule];
    $('#schedule-body').innerHTML = s.days.map(function (d) {
      var phases = d[1].map(phaseById).filter(Boolean);
      var secs = phases.reduce(function (a, p) { return a + p.seconds; }, 0);
      var vids = phases.reduce(function (a, p) { return a + p.videos.length; }, 0);
      return '<div class="sched-row">' +
        '<span class="when">' + esc(d[0]) + '</span>' +
        '<span class="what">' + phases.map(function (p) { return 'Phase ' + p.id + ' — ' + esc(p.title); }).join(' <span style="color:var(--ink-3)">→</span> ') + '</span>' +
        '<span class="howmuch">' + vids + ' videos · ' + dur(secs) + '</span>' +
        '</div>';
    }).join('');
  }

  function buildStatic() {
    $('#gap-list').innerHTML = D.gaps.map(function (g) {
      return '<div class="gap-item">' +
        '<div class="topic">' + esc(g.topic) + '</div>' +
        '<div class="why">' + md(g.why) + '<div class="where">' + md(g.where) + '</div></div>' +
        '</div>';
    }).join('');

    $('#caveat-list').innerHTML = D.caveats.map(function (c) { return '<li>' + md(c) + '</li>'; }).join('');

    $('#top-list').innerHTML = D.top.map(function (t) {
      return '<li><a href="https://youtu.be/' + esc(t.id) + '" target="_blank" rel="noopener">' + esc(t.title) + '</a>' +
        '<span class="views">' + t.views.toLocaleString() + '</span></li>';
    }).join('');
  }

  /* ---------------- progress ---------------- */

  function updateProgress() {
    var watchedVideos = ALL.filter(function (v) { return state.watched.has(v.id); });
    var n = watchedVideos.length;
    var pct = ALL.length ? Math.round((n / ALL.length) * 100) : 0;
    var doneSecs = watchedVideos.reduce(function (s, v) { return s + v.seconds; }, 0);

    $('#pct').textContent = pct + '%';
    $('#count').textContent = n + ' of ' + ALL.length + ' watched';
    $('#time-left').textContent = n === ALL.length ? 'complete' : dur(TOTAL_SECONDS - doneSecs) + ' left';

    D.phases.forEach(function (p) {
      var d = p.videos.filter(function (v) { return state.watched.has(v.id); }).length;
      var pctPhase = p.videos.length ? (d / p.videos.length) * 100 : 0;

      var railDone = $('[data-rail-done="' + p.id + '"]');
      if (railDone) {
        railDone.textContent = d + '/' + p.videos.length;
        var link = railDone.closest('a');
        if (link) link.classList.toggle('is-complete', d === p.videos.length);
      }
      var meta = $('[data-phase-done="' + p.id + '"]');
      if (meta) meta.textContent = d + '/' + p.videos.length;

      var bar = $('[data-meter="' + p.id + '"]');
      if (bar) bar.style.width = pctPhase + '%';
    });
  }

  /* ---------------- filtering ---------------- */

  function match(v) {
    if (state.level !== 'all' && v.level !== state.level) return false;
    if (state.unwatchedOnly && state.watched.has(v.id)) return false;
    if (!state.q) return true;
    var hay = [v.title, v.one, v.length, v.level, v.id, v.insight, v.prereq]
      .concat(v.bullets || [])
      .concat((v.extras || []).map(function (x) { return x.label + ' ' + x.text; }))
      .join(' ')
      .toLowerCase();
    return state.q.toLowerCase().split(/\s+/).filter(Boolean).every(function (t) { return hay.indexOf(t) > -1; });
  }

  function applyFilters() {
    var shown = 0;
    D.phases.forEach(function (p) {
      var visible = 0;
      $$('.v-row', $('[data-list="' + p.id + '"]')).forEach(function (row) {
        var v = p.videos.filter(function (x) { return x.id === row.dataset.id; })[0];
        var ok = v ? match(v) : true;
        row.hidden = !ok;
        if (ok) visible++;
      });
      shown += visible;
      var sec = $('#phase-' + p.id);
      if (sec) sec.hidden = visible === 0;
    });
    $('#result-count').textContent = (state.q || state.level !== 'all' || state.unwatchedOnly)
      ? shown + ' of ' + ALL.length + ' matching'
      : '';
    if (shown === 0) {
      if (!$('.empty')) {
        var e = document.createElement('p');
        e.className = 'empty';
        e.textContent = 'Nothing matches. Clear the search or the level filter.';
        $('#phases').appendChild(e);
      }
    } else {
      var old = $('.empty');
      if (old) old.remove();
    }
  }

  /* ---------------- interactions ---------------- */

  function toggleRow(row, force) {
    var open = force === undefined ? !row.classList.contains('is-open') : force;
    row.classList.toggle('is-open', open);
    var btn = $('.v-main', row);
    if (btn) btn.setAttribute('aria-expanded', String(open));
  }

  function toggleWatch(id, on) {
    if (on) state.watched.add(id); else state.watched.delete(id);
    var row = $('.v-row[data-id="' + id + '"]');
    if (row) row.classList.toggle('is-watched', on);
    persist();
    updateProgress();
    applyFilters();
  }

  function firstUnwatched() {
    for (var i = 0; i < D.phases.length; i++) {
      var p = D.phases[i];
      for (var j = 0; j < p.videos.length; j++) {
        if (!state.watched.has(p.videos[j].id)) return { phase: p, v: p.videos[j] };
      }
    }
    return null;
  }

  function wire() {
    document.addEventListener('click', function (e) {
      var btn = e.target.closest('.v-main');
      if (btn) {
        var row = btn.closest('.v-row');
        var wasOpen = row.classList.contains('is-open');
        // accordion within a phase keeps the page short
        $$('.v-row.is-open').forEach(function (r) { if (r !== row) toggleRow(r, false); });
        toggleRow(row, !wasOpen);
        return;
      }
      var tab = e.target.closest('[data-sched]');
      if (tab) {
        state.schedule = Number(tab.dataset.sched);
        buildSchedule();
        return;
      }
      var chip = e.target.closest('.chip');
      if (chip) {
        state.level = chip.dataset.level;
        $$('.chip').forEach(function (c) { c.classList.toggle('is-on', c === chip); });
        applyFilters();
        return;
      }
    });

    document.addEventListener('change', function (e) {
      var t = e.target;
      if (t.matches('[data-watch]')) {
        toggleWatch(t.dataset.watch, t.checked);
        // keep duplicated checkboxes (tonight strip) in sync
        $$('[data-watch="' + t.dataset.watch + '"]').forEach(function (o) { o.checked = t.checked; });
      }
    });

    var q = $('#q');
    q.addEventListener('input', function () {
      state.q = q.value.trim();
      applyFilters();
    });

    $('#unwatched').addEventListener('change', function (e) {
      state.unwatchedOnly = e.target.checked;
      applyFilters();
    });

    $('#btn-continue').addEventListener('click', function () {
      var next = firstUnwatched();
      if (!next) {
        window.scrollTo({ top: 0, behavior: 'smooth' });
        return;
      }
      state.level = 'all';
      state.unwatchedOnly = false;
      state.q = '';
      q.value = '';
      $('#unwatched').checked = false;
      $$('.chip').forEach(function (c) { c.classList.toggle('is-on', c.dataset.level === 'all'); });
      applyFilters();
      var row = $('.v-row[data-id="' + next.v.id + '"]');
      if (row) {
        row.scrollIntoView({ behavior: 'smooth', block: 'center' });
        toggleRow(row, true);
        row.classList.add('is-ping');
        setTimeout(function () { row.classList.remove('is-ping'); }, 900);
      }
    });

    $('#btn-print').addEventListener('click', function () { window.print(); });

    $('#btn-reset').addEventListener('click', function () {
      if (state.watched.size === 0) return;
      if (!window.confirm('Clear all ' + state.watched.size + ' ticks?\n\nYour night notes stay.')) return;
      state.watched.clear();
      $$('[data-watch]').forEach(function (c) { c.checked = false; });
      $$('.v-row').forEach(function (r) { r.classList.remove('is-watched'); });
      persist();
      updateProgress();
      applyFilters();
    });

    var themeBtn = $('#btn-theme');
    if (themeBtn) {
      themeBtn.addEventListener('click', function () {
        var cur = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', cur);
        themeBtn.textContent = cur === 'dark' ? 'Light' : 'Dark';
        persist();
      });
    }

    var journal = $('#journal');
    if (journal) {
      var t;
      journal.addEventListener('input', function () {
        $('#journal-status').textContent = 'Saving…';
        clearTimeout(t);
        t = setTimeout(function () {
          persist();
          $('#journal-status').textContent = 'Saved locally';
        }, 400);
      });
    }

    $('#btn-export').addEventListener('click', function () {
      var payload = {
        exported: new Date().toISOString(),
        channel: D.channel.url,
        watched: allVideos().filter(function (v) { return state.watched.has(v.id); })
          .map(function (v) { return { phase: v.n, title: v.title, id: v.id }; }),
        journal: $('#journal').value
      };
      var blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
      var a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = 'mdg-progress.json';
      a.click();
      setTimeout(function () { URL.revokeObjectURL(a.href); }, 2000);
    });

    document.addEventListener('keydown', function (e) {
      var tag = (e.target.tagName || '').toLowerCase();
      var typing = tag === 'input' || tag === 'textarea';
      if (e.key === '/' && !typing) {
        e.preventDefault();
        q.focus();
      } else if (e.key === 'Escape' && document.activeElement === q) {
        q.value = '';
        state.q = '';
        applyFilters();
        q.blur();
      }
    });
  }

  /* ---------------- boot ---------------- */

  function boot() {
    var theme = saved.theme || (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', theme);
    var themeBtn = $('#btn-theme');
    if (themeBtn) themeBtn.textContent = theme === 'dark' ? 'Light' : 'Dark';

    buildRail();
    buildTonight();
    buildPhases();
    buildSchedule();
    buildStatic();
    wire();

    if (typeof saved.journal === 'string') $('#journal').value = saved.journal;

    updateProgress();
    applyFilters();
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
  else boot();
})();
