from fastapi import APIRouter, HTTPException

from app.schemas.risk import RiskScoreRequest, RiskScoreResponse
from app.services.risk_service import score_risk

router = APIRouter()


@router.post("/risk-score", response_model=RiskScoreResponse)
def risk_score(payload: RiskScoreRequest) -> RiskScoreResponse:
    try:
        result = score_risk(
            detection=payload.detection.model_dump(),
            climate=payload.climate.model_dump(),
            water_type=payload.water_type,
        )
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=f"Risk scoring failed: {exc}") from exc

    return RiskScoreResponse(**result)
