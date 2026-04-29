from pydantic import BaseModel, Field

from app.schemas.detection import DetectionResult


class ClimateData(BaseModel):
    temperature: float = Field(..., description="Air/water temperature in Celsius")
    rainfall: float = Field(..., ge=0, description="Rainfall level in mm")
    uv_index: float = Field(..., ge=0, description="UV index")
    season: str = Field(..., description="Season label")


class RiskScoreRequest(BaseModel):
    detection: DetectionResult
    climate: ClimateData
    water_type: str = Field(default="treated_water")


class RiskScoreResponse(BaseModel):
    risk_score: float = Field(..., ge=0, le=100)
    risk_level: str
    recommendation: str
    inputs: dict = Field(default_factory=dict)
