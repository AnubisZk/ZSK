import { useEffect, useState } from 'react';

import Dashboard from './components/Dashboard';
import { analyzeImage, fetchClimateData, getRiskScore } from './services/api';
import { emptyDetection, emptyRisk } from './types/defaultState';

const WATER_TYPES = [
  'drinking_water',
  'bottled_water',
  'treated_water',
  'lake_water',
  'rainwater',
  'river_water',
  'wastewater',
];

export default function App() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState('');
  const [waterType, setWaterType] = useState('treated_water');
  const [detection, setDetection] = useState(emptyDetection);
  const [climate, setClimate] = useState({ temperature: 0, rainfall: 0, uv_index: 0, season: '-' });
  const [risk, setRisk] = useState(emptyRisk);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchClimateData()
      .then((data) => setClimate(data))
      .catch(() => setError('Climate data could not be loaded.'));
  }, []);

  const onFileChange = (event) => {
    const file = event.target.files?.[0];
    if (!file) return;
    setSelectedFile(file);
    setPreviewUrl(URL.createObjectURL(file));
    setError('');
  };

  const onAnalyze = async () => {
    if (!selectedFile) {
      setError('Please choose an image first.');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const analysis = await analyzeImage(selectedFile);
      const detectionResult = analysis.result;
      setDetection(detectionResult);

      const riskResult = await getRiskScore({
        detection: detectionResult,
        climate,
        water_type: waterType,
      });

      setRisk(riskResult);
    } catch (err) {
      setError(err.message || 'Unexpected error occurred.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="container">
      <header>
        <h1>Climate-Aware Microplastic Risk Dashboard</h1>
        <p>Upload an image, run detection, and evaluate environmental risk.</p>
      </header>

      <section className="card upload-area">
        <label htmlFor="image-upload">Image Upload</label>
        <input id="image-upload" type="file" accept="image/*" onChange={onFileChange} />

        <label htmlFor="water-type">Water Type</label>
        <select id="water-type" value={waterType} onChange={(e) => setWaterType(e.target.value)}>
          {WATER_TYPES.map((type) => (
            <option key={type} value={type}>{type}</option>
          ))}
        </select>

        <button onClick={onAnalyze} disabled={loading}>
          {loading ? 'Analyzing...' : 'Analyze & Score'}
        </button>

        {error ? <p className="error">{error}</p> : null}
      </section>

      {previewUrl ? (
        <section className="card">
          <h3>Detection Image Preview</h3>
          <img src={previewUrl} alt="Uploaded sample" className="preview" />
        </section>
      ) : null}

      <Dashboard detection={detection} climate={climate} risk={risk} waterType={waterType} />
    </main>
  );
}
