from pathlib import Path
from typing import BinaryIO

from ml.schemas import StandardDetectionResult


class YoloDetector:
    def __init__(self, model_path: str | None = None) -> None:
        self.model_path = model_path or "models/yolov8-microplastic.pt"
        self.model = self._load_model()

    def _load_model(self):
        """Placeholder for ultralytics YOLO model loading."""
        if not Path(self.model_path).exists():
            return None
        return {"path": self.model_path, "loaded": False}

    def infer_from_path(self, image_path: str | Path) -> dict:
        image_path = Path(image_path)
        if not image_path.exists():
            raise FileNotFoundError(f"Image not found: {image_path}")
        return self._placeholder_result(source="yolo")

    def infer_from_upload(self, file_obj: BinaryIO) -> dict:
        _ = file_obj.read(1)
        file_obj.seek(0)
        return self._placeholder_result(source="yolo")

    @staticmethod
    def _placeholder_result(source: str) -> dict:
        result = StandardDetectionResult(
            particle_count=2,
            detections=[
                {
                    "label": "microplastic",
                    "confidence": 0.84,
                    "bbox": [120, 200, 180, 255],
                    "area_ratio": 0.008,
                    "source": source,
                },
                {
                    "label": "microplastic",
                    "confidence": 0.79,
                    "bbox": [300, 420, 340, 470],
                    "area_ratio": 0.006,
                    "source": source,
                },
            ],
            confidence_mean=0.815,
            small_particle_ratio=0.5,
            density_score=0.14,
        )
        return result.model_dump()
