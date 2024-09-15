from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Dict, Any

class AnalysisRequest(BaseModel):
    url: HttpUrl
    modules: Optional[List[str]] = ["performance", "ux", "content", "visual", "security"]

class AnalysisResult(BaseModel):
    score: float
    metrics: Dict[str, Any]

class AnalysisResponse(BaseModel):
    url: HttpUrl
    results: Dict[str, AnalysisResult]