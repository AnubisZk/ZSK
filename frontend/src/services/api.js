const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

export async function analyzeImage(file) {
  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch(`${API_BASE}/analyze-image`, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    throw new Error('Failed to analyze image');
  }

  return response.json();
}

export async function fetchClimateData() {
  const response = await fetch(`${API_BASE}/climate-data`);
  if (!response.ok) {
    throw new Error('Failed to fetch climate data');
  }
  return response.json();
}

export async function getRiskScore(payload) {
  const response = await fetch(`${API_BASE}/risk-score`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error('Failed to fetch risk score');
  }

  return response.json();
}
