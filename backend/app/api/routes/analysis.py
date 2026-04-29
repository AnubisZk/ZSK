from pathlib import Path
import tempfile

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.schemas.detection import AnalyzeImageResponse
from app.services.analysis_service import analyze_uploaded_file

router = APIRouter()


@router.post("/analyze-image", response_model=AnalyzeImageResponse)
async def analyze_image(file: UploadFile = File(...)) -> AnalyzeImageResponse:
    if not file.filename:
        raise HTTPException(status_code=400, detail="Missing file name")

    suffix = Path(file.filename).suffix or ".jpg"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        content = await file.read()
        temp_file.write(content)
        temp_path = temp_file.name

    try:
        response_payload = analyze_uploaded_file(temp_path)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=f"Image analysis failed: {exc}") from exc

    return AnalyzeImageResponse(**response_payload)
