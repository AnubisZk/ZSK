# Climate-Aware Microplastic Decision Support Platform

This repository scaffolds a modular, production-oriented full-stack architecture for detecting microplastics and converting findings into climate-aware risk insights.

## Modules

- **frontend/**: React dashboard for image upload, detection visualization, climate inputs, and risk outputs.
- **backend/**: FastAPI service exposing health, detection, risk scoring, and climate data endpoints.
- **ml/**: YOLOv8 + SAHI-ready inference pipeline with standardized detection output.
- **risk_engine/**: Rule-based scoring engine and configurable water-type factors.
- **docs/**: Project documentation and architecture notes.
- **tests/**: Initial backend and risk-engine tests.

## Quick Start

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## API Endpoints

- `GET /health`
- `POST /analyze-image`
- `POST /risk-score`
- `GET /climate-data`


## Single HTML Version

For a no-build prototype, open `frontend/dashboard.html` directly in your browser.
This file provides upload, climate fetch, analyze, and risk-score flows via backend APIs.

## Status

This is an initial scaffold. Core scientific model weights, SAHI production tuning, and external climate API integration are intentionally left as placeholders.
