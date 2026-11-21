// 3B önizleme kaynağı. Derleme: tools/build_viewer.sh (three.js ile tek dosyaya paketler)
import { WebGLRenderer, Scene, PerspectiveCamera, HemisphereLight, DirectionalLight, MeshStandardMaterial, Mesh, Box3, Vector3 } from "three";
import { STLLoader } from "three/examples/jsm/loaders/STLLoader.js";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls.js";

const loader = new STLLoader();
const EN = document.documentElement.lang === "en";
const L = EN ? { load: "Loading…", fail: "Could not load the model.", nogl: "Your browser does not support 3D. You can download the parts instead." } : { load: "Yükleniyor…", fail: "Model yüklenemedi.", nogl: "Tarayıcın 3B gösterimi desteklemiyor. Parçaları indirme bölümünden alabilirsin." };
document.querySelectorAll(".viewer").forEach(init);

function init(root) {
  const files = JSON.parse(root.dataset.files);
  const box = root.querySelector(".v-canvas"), status = root.querySelector(".v-status"), dim = root.querySelector(".v-dim");
  const btns = [...root.querySelectorAll(".v-part")];
  let renderer;
  try { renderer = new WebGLRenderer({ antialias: true, alpha: true }); } catch (e) { status.textContent = L.nogl; return; }
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  box.appendChild(renderer.domElement);
  const scene = new Scene(), camera = new PerspectiveCamera(35, 1, 0.1, 5000);
  scene.add(new HemisphereLight(0xffffff, 0x8a8f99, 1.1));
  const key = new DirectionalLight(0xffffff, 1.6); key.position.set(3, 5, 4); scene.add(key);
  const fill = new DirectionalLight(0xffffff, 0.5); fill.position.set(-4, -2, -3); scene.add(fill);
  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true; controls.autoRotate = !matchMedia("(prefers-reduced-motion: reduce)").matches; controls.autoRotateSpeed = 1.2;
  controls.addEventListener("start", () => (controls.autoRotate = false));
  const mat = new MeshStandardMaterial({ color: 0xb9bec7, metalness: 0.25, roughness: 0.55 });
  let mesh = null, home = null, visible = true;
  new IntersectionObserver((en) => (visible = en[0].isIntersecting)).observe(box);

  function size() { const w = box.clientWidth, h = box.clientHeight; if (!w || !h) return; renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix(); }
  function frame() {
    const b = new Box3().setFromObject(mesh), c = b.getCenter(new Vector3()), s = b.getSize(new Vector3());
    mesh.position.sub(c);
    const d = (Math.max(s.x, s.y, s.z) / 2) / Math.tan((camera.fov * Math.PI) / 360) * 1.12;
    camera.near = d / 100; camera.far = d * 100; camera.position.set(d * 0.8, d * 0.55, d * 0.9); camera.updateProjectionMatrix();
    controls.target.set(0, 0, 0); controls.update(); home = camera.position.clone();
    dim.textContent = [s.x, s.y, s.z].map((v) => v.toFixed(0)).join(" × ") + " mm";
  }
  const cache = new Map();
  function show(geo) {
    if (mesh) scene.remove(mesh);
    mesh = new Mesh(geo, mat); scene.add(mesh); frame(); status.hidden = true;
  }
  function load(i) {
    btns.forEach((b, n) => b.setAttribute("aria-pressed", n === i));
    if (cache.has(i)) return show(cache.get(i));
    status.textContent = L.load; status.hidden = false;
    loader.load(files[i].url, (geo) => { geo.computeVertexNormals(); cache.set(i, geo); show(geo); }, undefined, () => (status.textContent = L.fail));
  }
  btns.forEach((b, n) => b.addEventListener("click", () => load(n)));
  root.querySelector(".v-reset").addEventListener("click", () => { if (home) { camera.position.copy(home); controls.target.set(0, 0, 0); controls.update(); } });
  new ResizeObserver(size).observe(box); size(); load(0);
  (function tick() { requestAnimationFrame(tick); if (!visible) return; controls.update(); renderer.render(scene, camera); })();
}
