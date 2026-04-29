from typing import Any

from pydantic import BaseModel, Field


class DetectionItem(BaseModel):
    label: str = Field(..., description="Detected class label")
    confidence: float = Field(..., ge=0, le=1, description="Model confidence for this detection")
    bbox: list[float] = Field(
        default_factory=list,
        description="Bounding box as [x1, y1, x2, y2] in pixel coordinates",
    )
    area_ratio: float = Field(
        default=0,
        ge=0,
        le=1,
        description="Bounding box area divided by total image area",
    )
    source: str = Field(default="yolo", description="Origin detector: yolo or sahi")


class DetectionResult(BaseModel):
    particle_count: int = Field(0, ge=0, description="Total number of microplastic particles")
    detections: list[DetectionItem] = Field(default_factory=list, description="Detailed detections")
    confidence_mean: float = Field(0, ge=0, le=1, description="Mean confidence across detections")
    small_particle_ratio: float = Field(
        0,
        ge=0,
        le=1,
        description="Ratio of particles considered small",
    )
    density_score: float = Field(0, ge=0, description="Density score derived from particle area coverage")


class AnalyzeImageResponse(BaseModel):
    status: str = Field(default="ok")
    result: DetectionResult
    metadata: dict[str, Any] = Field(default_factory=dict)
