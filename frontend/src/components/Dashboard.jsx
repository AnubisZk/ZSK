import { useMemo } from 'react';

const number = (value) => (typeof value === 'number' ? value.toFixed(2) : '-');

export default function Dashboard({ detection, climate, risk, waterType }) {
  const hasDetections = useMemo(() => detection?.particle_count > 0, [detection]);

  return (
    <section className="grid">
      <article className="card">
        <h3>Detection</h3>
        <p>Particle Count: <strong>{detection.particle_count}</strong></p>
        <p>Density Score: <strong>{number(detection.density_score)}</strong></p>
        <p>Small Particle Ratio: <strong>{number(detection.small_particle_ratio)}</strong></p>
        <p>Confidence Mean: <strong>{number(detection.confidence_mean)}</strong></p>
        <p>Detections: <strong>{hasDetections ? 'Available' : 'No detections yet'}</strong></p>
      </article>

      <article className="card">
        <h3>Climate Panel</h3>
        <p>Temperature: <strong>{number(climate.temperature)} °C</strong></p>
        <p>Rainfall: <strong>{number(climate.rainfall)} mm</strong></p>
        <p>UV Index: <strong>{number(climate.uv_index)}</strong></p>
        <p>Season: <strong>{climate.season || '-'}</strong></p>
        <p>Water Type: <strong>{waterType}</strong></p>
      </article>

      <article className="card">
        <h3>Risk Card</h3>
        <p>Risk Score: <strong>{number(risk.risk_score)}</strong></p>
        <p>Risk Level: <strong className={`risk ${risk.risk_level}`}>{risk.risk_level}</strong></p>
        <p>Recommendation:</p>
        <p>{risk.recommendation}</p>
      </article>
    </section>
  );
}
