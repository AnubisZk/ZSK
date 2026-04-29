from pathlib import Path

from ml.sahi_integration import merge_predictions, run_sliced_inference
from ml.schemas import StandardDetectionResult
from ml.yolo_inference import YoloDetector


def analyze_image(image_input: str | Path) -> dict:
    detector = YoloDetector()
    yolo_result = detector.infer_from_path(image_input)
    sahi_result = run_sliced_inference(str(image_input))
    merged = merge_predictions(yolo_result, sahi_result)
    validated = StandardDetectionResult(**merged)
    return validated.model_dump()
