from fastapi import APIRouter, HTTPException

from app.schemas.climate import ClimateDataResponse
from app.services.climate_service import get_climate_data

router = APIRouter()


@router.get("/climate-data", response_model=ClimateDataResponse)
def climate_data() -> ClimateDataResponse:
    try:
        return ClimateDataResponse(**get_climate_data())
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=f"Climate data retrieval failed: {exc}") from exc
