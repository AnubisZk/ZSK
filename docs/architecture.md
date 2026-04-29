# Architecture Notes

## Layers

1. **Frontend (React + Vite)**
   - Dashboard UI, upload flow, API orchestration.
2. **Backend (FastAPI)**
   - REST API for health, image analysis, risk scoring, and climate data.
3. **ML Module (YOLOv8 + SAHI placeholders)**
   - Standardized detection output schema and composable inference pipeline.
4. **Risk Engine**
   - Explainable weighted scoring with configurable water source factors.

## Data Contracts

- Detection output is standardized to:
  - `particle_count`
  - `detections`
  - `confidence_mean`
  - `small_particle_ratio`
  - `density_score`
- Risk output includes:
  - `risk_score`
  - `risk_level`
  - `recommendation`

## Extension Plan

- Replace placeholder YOLO model loading with `ultralytics` runtime.
- Add SAHI confidence calibration and NMS merging.
- Integrate real climate provider and caching.
- Add persistence and observability.
