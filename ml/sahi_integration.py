from typing import Any


def run_sliced_inference(image_path: str, slice_height: int = 640, slice_width: int = 640) -> dict[str, Any]:
    """Placeholder SAHI sliced inference output for small object detection."""
    _ = (image_path, slice_height, slice_width)
    return {
        "detections": [
            {
                "label": "microplastic",
                "confidence": 0.73,
                "bbox": [402, 122, 419, 138],
                "area_ratio": 0.0015,
                "source": "sahi",
            }
        ]
    }


def merge_predictions(yolo_result: dict, sahi_result: dict) -> dict:
    yolo_detections = list(yolo_result.get("detections", []))
    sahi_detections = list(sahi_result.get("detections", []))
    combined = yolo_detections + sahi_detections

    if combined:
        mean_conf = sum(item.get("confidence", 0) for item in combined) / len(combined)
    else:
        mean_conf = 0.0

    small_count = sum(1 for item in combined if item.get("area_ratio", 0) <= 0.003)
    density_score = sum(item.get("area_ratio", 0) for item in combined)

    return {
        "particle_count": len(combined),
        "detections": combined,
        "confidence_mean": round(mean_conf, 4),
        "small_particle_ratio": round((small_count / len(combined)) if combined else 0.0, 4),
        "density_score": round(density_score, 4),
    }
