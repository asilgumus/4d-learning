const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const context = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(root, "data.js"), "utf8"), context);
const { projects, experiments } = context.window.LEARNING_DATA;

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

assert(projects.length === 6, "Expected six learning tracks");
assert(projects.filter((item) => item.status === "available").length === 5, "Expected five available tracks");
assert(projects.filter((item) => item.status === "coming").length === 1, "Expected one coming-soon track");
assert(fs.existsSync(path.join(root, "assets", "resources", "cybersecurity", "cybersecurity-presentation-tr.pdf")), "Missing cybersecurity presentation");
assert(experiments.length === 19, "Expected 19 Arduino experiments");
assert(!experiments.some((item) => item.id === 10), "Experiment 10 should remain absent to match the source");
assert(new Set(experiments.map((item) => item.id)).size === experiments.length, "Experiment IDs must be unique");

for (const experiment of experiments) {
  for (const key of ["title", "summary", "materials", "wiring", "code", "result", "challenge"]) {
    assert(experiment[key] && experiment[key].length !== 0, `Experiment ${experiment.id} is missing ${key}`);
  }
  const pdf = path.join(root, "assets", "resources", "arduino", `experiment-${String(experiment.id).padStart(2, "0")}.pdf`);
  assert(fs.existsSync(pdf), `Missing source PDF: ${path.relative(root, pdf)}`);
}

for (const html of ["index.html", "project.html", "lesson.html"]) {
  const source = fs.readFileSync(path.join(root, html), "utf8");
  assert(source.includes('lang="en"'), `${html} must declare English`);
  assert(source.includes('href="styles.css"'), `${html} must load the shared stylesheet`);
  assert(source.includes('src="app.js"'), `${html} must load the application script`);
}

console.log(`Validated ${projects.length} tracks and ${experiments.length} Arduino experiments.`);
