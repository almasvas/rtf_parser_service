from fastapi import APIRouter, UploadFile, File
from app.service import parse_rtf_file

router = APIRouter()

@router.post("/parse")
async def parse_rtf(file: UploadFile = File(...)):
    content = await file.read()
    result = parse_rtf_file(content)
    return {"parsed": result}
