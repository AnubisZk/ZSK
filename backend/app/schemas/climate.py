from pydantic import BaseModel, Field


class ClimateDataResponse(BaseModel):
    temperature: float = Field(..., description="Normalized temperature in Celsius")
    rainfall: float = Field(..., ge=0, description="Normalized rainfall in mm")
    uv_index: float = Field(..., ge=0, description="Normalized UV index")
    season: str = Field(..., description="Season")
    source: str = Field(..., description="mock or api")
