import React, { useRef, useEffect } from 'react';
import * as THREE from 'three';

function Wormhole3D({ simulationData }) {
  const mountRef = useRef(null);

  useEffect(() => {
    // Estrai dati dalla simulazione
    const { r, b_r, Phi_r, b0 } = simulationData;

    // Configurazione scena
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(window.innerWidth * 0.8, window.innerHeight * 0.8);
    mountRef.current.appendChild(renderer.domElement);

    // Geometria della gola (torus semplificato)
    const geometry = new THREE.TorusGeometry(b0, 0.5, 16, 100);
    const material = new THREE.MeshPhongMaterial({ color: 0x00ff00, wireframe: true });
    const wormhole = new THREE.Mesh(geometry, material);
    scene.add(wormhole);

    // Aggiungi una superficie curva basata su b(r)
    const curvePoints = r.map((radius, i) => {
      const z = Phi_r[i] * 5; // Scala Phi(r) per visibilità
      return new THREE.Vector3(radius - b0, 0, z); // Centra su b0
    });
    const curve = new THREE.CatmullRomCurve3(curvePoints);
    const tubeGeometry = new THREE.TubeGeometry(curve, 64, 0.2, 8, false);
    const tubeMaterial = new THREE.MeshPhongMaterial({ color: 0xff0000, transparent: true, opacity: 0.5 });
    const tube = new THREE.Mesh(tubeGeometry, tubeMaterial);
    scene.add(tube);

    // Luci
    const light = new THREE.PointLight(0xffffff, 1, 100);
    light.position.set(10, 10, 10);
    scene.add(light);

    // Posizione camera
    camera.position.z = b0 * 2;

    // Animazione
    const animate = () => {
      requestAnimationFrame(animate);
      wormhole.rotation.x += 0.01;
      wormhole.rotation.y += 0.01;
      renderer.render(scene, camera);
    };
    animate();

    // Cleanup
    return () => {
      mountRef.current.removeChild(renderer.domElement);
    };
  }, [simulationData]);

  return <div ref={mountRef} style={{ width: '100%', height: '100%' }} />;
}

export default Wormhole3D;