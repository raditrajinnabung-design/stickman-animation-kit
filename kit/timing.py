s

  return {
    scene,
    camera,
    renderer
  };
}

export function animateScene(renderer, scene, camera) {
  renderer.render(scene, camera);
}
