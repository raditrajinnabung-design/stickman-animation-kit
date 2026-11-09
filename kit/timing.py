import * as THREE from "three";

export function createScene() {
  const scene = new THREE.Scene();

  scene.background = new THREE.Color("#ffffff");

  const camera = new THREE.PerspectiveCamera(
    75,
    16 / 9,
    0.1,
    1000
  );

  camera.position.z = 5;

  const renderer = new THREE.WebGLRenderer({
    antialias: true
  });

  renderer.setSize(1280, 720);

  const light = new THREE.AmbientLight(0xffffff, 1);
  scene.add(light);

  return {
    scene,
    camera,
    renderer
  };
}

export function animateScene(renderer, scene, camera) {
  renderer.render(scene, camera);
}
