from fastapi import FastAPI, HTTPException
from app.models.analysis import AnalysisRequest, AnalysisResponse
from app.services.analysis_service import AnalysisService

app = FastAPI()

@app.post("/api/v1/analyze", response_model=AnalysisResponse)
async def analyze(request: AnalysisRequest):
    try:
        return await AnalysisService.analyze(request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/v1/analyze/{module}", response_model=AnalysisResponse)
async def analyze_module(module: str, url: str):
    try:
        request = AnalysisRequest(url=url, modules=[module])
        return await AnalysisService.analyze(request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)