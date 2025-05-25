from pydantic import BaseModel

class ParseResponse(BaseModel):
    parsed: str
