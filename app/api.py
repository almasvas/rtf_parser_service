from fastapi import APIRouter, UploadFile, File
from .service import parse_rtf_file

router = APIRouter()

@router.post("/parse")
async def parse_rtf(file: UploadFile = File(...)):
    content = await file.read()
    result = parse_rtf_file(content)
    return {"parsed": result}
