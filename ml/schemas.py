from pydantic import BaseModel, Field


class DetectionItem(BaseModel):
    label: str = Field(default="microplastic")
    confidence: float = Field(default=0.0, ge=0, le=1)
    bbox: list[float] = Field(default_factory=list)
    area_ratio: float = Field(default=0.0, ge=0, le=1)
    source: str = Field(default="yolo")


class StandardDetectionResult(BaseModel):
    particle_count: int = Field(default=0, ge=0)
    detections: list[DetectionItem] = Field(default_factory=list)
    confidence_mean: float = Field(default=0.0, ge=0, le=1)
    small_particle_ratio: float = Field(default=0.0, ge=0, le=1)
    density_score: float = Field(default=0.0, ge=0)


def empty_detection_result() -> dict:
    return StandardDetectionResult().model_dump()
