from pathlib import Path

from ml.pipeline import analyze_image as run_detection


def analyze_uploaded_file(file_path: str):
    image_path = Path(file_path)
    result = run_detection(image_path)
    return {
        "status": "ok",
        "result": result,
        "metadata": {
            "filename": image_path.name,
            "pipeline": "yolo+sahi",
        },
    }
