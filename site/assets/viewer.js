import * as THREE from "three";
import { STLLoader } from "three/addons/loaders/STLLoader.js";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

const loader = new STLLoader();
document.querySelectorAll(".viewer").forEach(init);

function init(root) {
  const files = JSON.parse(root.dataset.files);
  const canvasBox = root.querySelector(".v-canvas"), sel = root.querySelector("select"), status = root.querySelector(".v-status");
  const css = getComputedStyle(document.documentElement);
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  canvasBox.appendChild(renderer.domElement);
  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(35, 1, 0.1, 5000);
  scene.add(new THREE.HemisphereLight(0xffffff, 0x8a8f99, 1.1));
  const key = new THREE.DirectionalLight(0xffffff, 1.6); key.position.set(3, 5, 4); scene.add(key);
  const fill = new THREE.DirectionalLight(0xffffff, 0.5); fill.position.set(-4, -2, -3); scene.add(fill);
  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true; controls.autoRotate = !matchMedia("(prefers-reduced-motion: reduce)").matches; controls.autoRotateSpeed = 1.2;
  controls.addEventListener("start", () => (controls.autoRotate = false));
  let mesh = null, home = null;
  const mat = new THREE.MeshStandardMaterial({ color: 0xb9bec7, metalness: 0.25, roughness: 0.55 });

  function size() {
    const w = canvasBox.clientWidth, h = canvasBox.clientHeight;
    renderer.setSize(w, h, false); camera.aspect = w / h; camera.updateProjectionMatrix();
  }
  function frame() {
    const box = new THREE.Box3().setFromObject(mesh), c = box.getCenter(new THREE.Vector3()), s = box.getSize(new THREE.Vector3());
    mesh.position.sub(c);
    const d = (Math.max(s.x, s.y, s.z) / 2) / Math.tan((camera.fov * Math.PI) / 360) * 1.5;
    camera.near = d / 100; camera.far = d * 100; camera.position.set(d * 0.8, d * 0.55, d * 0.9); camera.updateProjectionMatrix();
    controls.target.set(0, 0, 0); controls.update(); home = { p: camera.position.clone() };
    root.dataset.dim = [s.x, s.y, s.z].map((v) => v.toFixed(0)).join(" × ");
    root.querySelector(".v-dim").textContent = root.dataset.dim + " mm";
  }
  function load(i) {
    status.textContent = "Yükleniyor…"; status.hidden = false;
    loader.load(files[i].url, (geo) => {
      if (mesh) { scene.remove(mesh); mesh.geometry.dispose(); }
      geo.computeVertexNormals();
      geo.rotateX(-Math.PI / 2); // CAD (Z yukarı) -> web (Y yukarı)
      mesh = new THREE.Mesh(geo, mat); scene.add(mesh); frame(); status.hidden = true;
    }, undefined, () => { status.textContent = "Model yüklenemedi."; });
  }
  sel.addEventListener("change", () => load(+sel.value));
  root.querySelector(".v-reset").addEventListener("click", () => { if (home) { camera.position.copy(home.p); controls.target.set(0, 0, 0); controls.update(); } });
  new ResizeObserver(size).observe(canvasBox); size(); load(0);
  (function tick() { requestAnimationFrame(tick); controls.update(); renderer.render(scene, camera); })();
}
