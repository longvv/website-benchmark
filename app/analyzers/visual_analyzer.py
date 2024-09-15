from app.interfaces.analyzer import Analyzer
from app.api_clients.base_api_client import BaseApiClient
from app.models.analysis import AnalysisResult

class VisualAnalyzer(Analyzer):
    def __init__(self, api_client: BaseApiClient):
        self.api_client = api_client

    async def analyze(self, url: str) -> AnalysisResult:
        data = {"url": url}
        response = await self.api_client.post("/analyze", data)
        
        clarity_score = response.get("clarity", 0)
        excitingness_score = response.get("excitingness", 0)
        aesthetic_score = (clarity_score + excitingness_score) / 2

        return AnalysisResult(
            score=aesthetic_score,
            metrics={
                "clarity": clarity_score,
                "excitingness": excitingness_score
            }
        )