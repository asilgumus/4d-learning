(function () {
  "use strict";

  const data = window.LEARNING_DATA;
  if (!data) return;

  const escapeHtml = (value) => String(value).replace(/[&<>'"]/g, (char) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;"
  }[char]));

  function initMenu() {
    const toggle = document.querySelector(".menu-toggle");
    const nav = document.querySelector(".main-nav");
    if (!toggle || !nav) return;
    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", String(open));
    });
    nav.addEventListener("click", () => {
      nav.classList.remove("open");
      toggle.setAttribute("aria-expanded", "false");
    });
  }

  function projectCard(project) {
    const statusText = project.status === "available" ? "Available" : "Coming soon";
    const href = `project.html?id=${encodeURIComponent(project.id)}`;
    return `<article class="project-card" data-status="${project.status}" data-search="${escapeHtml(`${project.title} ${project.kicker} ${project.tags.join(" ")}`.toLowerCase())}">
      <div class="card-top"><span class="card-index">${project.index}</span><span class="status ${project.status === "coming" ? "coming" : ""}">${statusText}</span></div>
      ${project.index === "01" ? '<span class="card-graphic" aria-hidden="true">NB</span>' : ""}
      <p class="card-kicker">${escapeHtml(project.kicker)}</p>
      <h3 class="card-title">${escapeHtml(project.title)}</h3>
      <p class="card-description">${escapeHtml(project.summary)}</p>
      <div class="card-meta">${project.tags.map((tag) => `<span>${escapeHtml(tag)}</span>`).join("")}</div>
      <a class="card-link" href="${href}" aria-label="${project.status === "available" ? "Open" : "View"} ${escapeHtml(project.title)}">${project.status === "available" ? "Open field guide" : "View track"} →</a>
    </article>`;
  }

  function initHome() {
    const grid = document.querySelector("#project-grid");
    if (!grid) return;
    grid.innerHTML = data.projects.map(projectCard).join("");
    const buttons = [...document.querySelectorAll("[data-filter]")];
    const search = document.querySelector("#library-search");
    const empty = document.querySelector("#empty-state");
    let activeFilter = "all";

    function applyFilters() {
      const query = search.value.trim().toLowerCase();
      let count = 0;
      grid.querySelectorAll(".project-card").forEach((card) => {
        const statusMatch = activeFilter === "all" || card.dataset.status === activeFilter;
        const searchMatch = !query || card.dataset.search.includes(query);
        const visible = statusMatch && searchMatch;
        card.hidden = !visible;
        if (visible) count += 1;
      });
      empty.hidden = count !== 0;
    }

    buttons.forEach((button) => button.addEventListener("click", () => {
      activeFilter = button.dataset.filter;
      buttons.forEach((item) => {
        const selected = item === button;
        item.classList.toggle("active", selected);
        item.setAttribute("aria-pressed", String(selected));
      });
      applyFilters();
    }));
    search.addEventListener("input", applyFilters);
  }

  function notFound(kind) {
    return `<section class="not-found"><div><p class="eyebrow">404 / Not found</p><h1>${escapeHtml(kind)} not found</h1><p>The requested learning resource does not exist.</p><a class="button button-primary" href="index.html#library">Return to the library</a></div></section>`;
  }

  function guideFacts(project) {
    return `<dl class="guide-facts">
      <div><dt>Audience</dt><dd>${escapeHtml(project.audience)}</dd></div>
      <div><dt>Format</dt><dd>${escapeHtml(project.duration)}</dd></div>
      <div><dt>Level</dt><dd>${escapeHtml(project.level)}</dd></div>
      <div><dt>Status</dt><dd>${project.status === "available" ? "Ready to use" : "In preparation"}</dd></div>
    </dl>`;
  }

  function guideSection(section, index) {
    const id = `section-${index + 1}`;
    return `<section class="guide-section" id="${id}">
      <span class="section-number">${String(index + 1).padStart(2, "0")}</span>
      <h2>${escapeHtml(section.title)}</h2>
      ${(section.body || []).map((paragraph) => `<p>${escapeHtml(paragraph)}</p>`).join("")}
      ${section.list ? `<ul>${section.list.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul>` : ""}
      ${section.steps ? `<ol>${section.steps.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ol>` : ""}
      ${section.note ? `<aside class="note"><strong>Field note:</strong> ${escapeHtml(section.note)}</aside>` : ""}
    </section>`;
  }

  function experimentRows() {
    return `<div class="experiments-head"><div><span class="section-number">03</span><h2>All experiments</h2></div><span class="status">19 lessons</span></div>
      <div class="experiment-list">${data.experiments.map((experiment) => `<a class="experiment-row" href="lesson.html?id=${experiment.id}">
        <span class="num">${String(experiment.id).padStart(2, "0")}</span>
        <span><strong>${escapeHtml(experiment.title)}</strong><small>${escapeHtml(experiment.concept)} · ${escapeHtml(experiment.time)}</small></span>
        <span class="level">${escapeHtml(experiment.level)}</span><span aria-hidden="true">→</span>
      </a>`).join("")}</div>`;
  }

  function initProject() {
    const view = document.querySelector("#project-view");
    if (!view) return;
    const id = new URLSearchParams(location.search).get("id");
    const project = data.projects.find((item) => item.id === id);
    if (!project) { view.innerHTML = notFound("Project"); return; }
    document.title = `${project.title} | 4D Learning Platform`;

    if (project.status === "coming") {
      view.innerHTML = `<section class="coming-panel"><span class="coming-code">${project.index}</span><p class="eyebrow">${escapeHtml(project.kicker)}</p><h1>${escapeHtml(project.title)}</h1><p>${escapeHtml(project.intro)}</p><span class="status coming">Coming soon</span><br><br><a class="text-link" href="index.html#library">← Return to project library</a></section>`;
      return;
    }

    const sections = project.sections || [];
    const toc = sections.map((section, index) => `<a href="#section-${index + 1}">${String(index + 1).padStart(2, "0")} ${escapeHtml(section.title)}</a>`).join("");
    const sources = project.sourceLinks ? `<section class="guide-section" id="source-links"><span class="section-number">RESOURCES</span><h2>Continue exploring</h2><p>Use the original project resources to investigate further or build on the work.</p><div class="hero-actions">${project.sourceLinks.map((link) => `<a class="button button-secondary" href="${escapeHtml(link.url)}" target="_blank" rel="noopener">${escapeHtml(link.label)} ↗</a>`).join("")}</div></section>` : "";
    view.innerHTML = `<header class="guide-hero"><div class="guide-hero-inner">
      <a class="guide-crumb" href="index.html#library">← Project library</a>
      <div class="guide-hero-grid"><div><p class="eyebrow">${escapeHtml(project.kicker)}</p><h1>${escapeHtml(project.title)}</h1><p class="guide-tagline">${escapeHtml(project.intro)}</p></div>${guideFacts(project)}</div>
    </div></header>
    <div class="guide-layout">
      <aside class="guide-toc"><p>In this field guide</p><nav aria-label="Guide contents">${toc}${project.isArduino ? '<a href="#experiments">03 All experiments</a>' : ""}${project.sourceLinks ? '<a href="#source-links">Resources</a>' : ""}</nav></aside>
      <article class="guide-content">${sections.map(guideSection).join("")}${project.isArduino ? `<section id="experiments">${experimentRows()}</section>` : ""}${sources}</article>
    </div>`;
  }

  function initLesson() {
    const view = document.querySelector("#lesson-view");
    if (!view) return;
    const id = Number(new URLSearchParams(location.search).get("id"));
    const lessonIndex = data.experiments.findIndex((item) => item.id === id);
    const lesson = data.experiments[lessonIndex];
    if (!lesson) { view.innerHTML = notFound("Experiment"); return; }
    document.title = `${lesson.title} | 4D Learning Platform`;
    const previous = data.experiments[lessonIndex - 1];
    const next = data.experiments[lessonIndex + 1];
    const pdfName = `experiment-${String(lesson.id).padStart(2, "0")}.pdf`;
    view.innerHTML = `<header class="lesson-hero"><div class="lesson-hero-inner">
      <a class="lesson-breadcrumb" href="project.html?id=arduino-experiments">← Arduino experiments</a>
      <span class="lesson-no">EXPERIMENT ${String(lesson.id).padStart(2, "0")}</span><h1>${escapeHtml(lesson.title)}</h1><p class="lesson-summary">${escapeHtml(lesson.summary)}</p>
      <div class="lesson-meta"><span>${escapeHtml(lesson.level)}</span><span>${escapeHtml(lesson.time)}</span><span>${escapeHtml(lesson.concept)}</span></div>
    </div></header>
    <div class="lesson-layout"><article>
      <section class="lesson-block"><h2>What you will build</h2><p>${escapeHtml(lesson.summary)}</p></section>
      <section class="lesson-block"><h2>Wire the circuit</h2><ol>${lesson.wiring.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ol>${lesson.safety ? `<aside class="safety-note"><strong>Safety:</strong> ${escapeHtml(lesson.safety)}</aside>` : '<aside class="safety-note"><strong>Safety:</strong> Disconnect USB power before changing the circuit. Ask a mentor to inspect the wiring before reconnecting it.</aside>'}</section>
      <section class="lesson-block"><h2>Upload the code</h2><div class="code-wrap"><button class="copy-code" type="button">Copy code</button><pre><code>${escapeHtml(lesson.code)}</code></pre></div></section>
      <section class="lesson-block"><h2>Test and observe</h2><p>${escapeHtml(lesson.result)}</p><div class="note"><strong>Try next:</strong> ${escapeHtml(lesson.challenge)}</div></section>
      <section class="lesson-block"><h2>Troubleshooting</h2><ul><li>Confirm the selected board and port in the Arduino IDE.</li><li>Check that every component shares the intended ground connection.</li><li>Verify LED, diode, sensor and supply polarity before powering the circuit.</li><li>Compare every wire with the pin numbers used in the code.</li></ul></section>
      <nav class="lesson-nav" aria-label="Experiment navigation">${previous ? `<a href="lesson.html?id=${previous.id}">← Experiment ${String(previous.id).padStart(2,"0")}<br>${escapeHtml(previous.title)}</a>` : "<span></span>"}${next ? `<a href="lesson.html?id=${next.id}">Experiment ${String(next.id).padStart(2,"0")} →<br>${escapeHtml(next.title)}</a>` : '<a href="project.html?id=arduino-experiments">All experiments →</a>'}</nav>
    </article><aside class="lesson-side">
      <section class="lesson-card"><h2>Materials</h2><ul>${lesson.materials.map((item) => `<li>${escapeHtml(item)}</li>`).join("")}</ul></section>
      <section class="lesson-card"><h2>Original source</h2><p>The original Turkish worksheet is saved with this platform.</p><a class="button button-secondary" href="assets/resources/arduino/${pdfName}" target="_blank">Open PDF</a></section>
    </aside></div>`;

    const copyButton = view.querySelector(".copy-code");
    copyButton.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(lesson.code);
        copyButton.textContent = "Copied";
        setTimeout(() => { copyButton.textContent = "Copy code"; }, 1600);
      } catch (_) {
        copyButton.textContent = "Select code to copy";
      }
    });
  }

  initMenu();
  const page = document.body.dataset.page;
  if (page === "home") initHome();
  if (page === "project") initProject();
  if (page === "lesson") initLesson();
}());
