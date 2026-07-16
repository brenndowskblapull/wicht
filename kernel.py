import React, { useRef, useEffect, useState } from "react";

// Zeichen und Farben
const CHARS = ["'", ",", "-", "`"];
const COLORS = ["black", "grey", "orange"];

// Hilfsfunktion für Zufall
function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

export default function WichtApp() {
  const canvasRef = useRef(null);
  const [width, setWidth] = useState(window.innerWidth);
  const [height, setHeight] = useState(window.innerHeight);

  const posRef = useRef({ x: width / 2, y: height / 2, dirX: 1, dirY: 1 });
  const figureModeRef = useRef(false);
  const figurePositionsRef = useRef([]);
  const figureTimerRef = useRef(0);
  const nextFigureTimeRef = useRef(Math.random() * 7000 + 8000);

  // Sound
  const beepRef = useRef(null);

  // Initialisierung
  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");
    ctx.font = "20px monospace";
    ctx.textBaseline = "top";

    canvas.width = width;
    canvas.height = height;

    beepRef.current = new Audio("/sounds/beep.mp3"); // Pfad zu deinem Sound

    // Figur generieren
    const generateFigure = (cx, cy, size) => {
      const positions = [];
      const nPoints = randomInt(6, 12);
      for (let i = 0; i < nPoints; i++) {
        const angle = Math.random() * 2 * Math.PI;
        const r = Math.random() * size;
        const px = Math.max(0, Math.min(width, cx + r * Math.cos(angle)));
        const py = Math.max(0, Math.min(height, cy + r * Math.sin(angle)));
        positions.push({ x: px, y: py });
      }
      return positions;
    };

    const animate = () => {
      ctx.clearRect(0, 0, width, height);

      figureTimerRef.current += 30;

      // Figure Mode starten
      if (!figureModeRef.current && figureTimerRef.current > nextFigureTimeRef.current) {
        figureModeRef.current = true;
        figurePositionsRef.current = generateFigure(width / 2, height / 2, Math.min(width, height) / 4);
        figureTimerRef.current = 0;
        nextFigureTimeRef.current = Math.random() * 7000 + 5000;
        beepRef.current?.play();
      }

      let pos = posRef.current;

      if (figureModeRef.current && figurePositionsRef.current.length > 0) {
        // Zufälliger Punkt der Figur
        let idx = randomInt(0, figurePositionsRef.current.length - 1);
        pos.x = figurePositionsRef.current[idx].x;
        pos.y = figurePositionsRef.current[idx].y;

        if (figureTimerRef.current > randomInt(3000, 5000)) {
          figureModeRef.current = false;
          figureTimerRef.current = 0;
          beepRef.current?.play();
        }
      } else {
        // Normaler Chaos-Flitzer
        pos.x += pos.dirX * randomInt(3, 15);
        pos.y += pos.dirY * randomInt(1, 5);

        if (pos.x >= width) { pos.x = width; pos.dirX = -1; beepRef.current?.play(); }
        if (pos.x <= 0) { pos.x = 0; pos.dirX = 1; beepRef.current?.play(); }
        if (pos.y >= height) { pos.y = height; pos.dirY = -1; beepRef.current?.play(); }
        if (pos.y <= 0) { pos.y = 0; pos.dirY = 1; beepRef.current?.play(); }
      }

      // Zeichnen
      ctx.fillStyle = COLORS[randomInt(0, COLORS.length - 1)];
      ctx.fillText(CHARS[randomInt(0, CHARS.length - 1)], pos.x, pos.y);

      requestAnimationFrame(animate);
    };

    animate();

    // Sensoren
    const handleMotion = (e) => {
      if (e.accelerationIncludingGravity) {
        posRef.current.x += e.accelerationIncludingGravity.x || 0;
        posRef.current.y -= e.accelerationIncludingGravity.y || 0;
      }
    };

    const handleMouse = (e) => {
      posRef.current.x = e.clientX;
      posRef.current.y = e.clientY;
    };

    window.addEventListener("devicemotion", handleMotion);
    window.addEventListener("mousemove", handleMouse);

    return () => {
      window.removeEventListener("devicemotion", handleMotion);
      window.removeEventListener("mousemove", handleMouse);
    };
  }, [width, height]);

  return (
    <canvas
      ref={canvasRef}
      style={{ display: "block", width: "100vw", height: "100vh", background: "#000" }}
    />
  );
}