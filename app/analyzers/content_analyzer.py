from app.interfaces.analyzer import Analyzer
from app.api_clients.base_api_client import BaseApiClient
from app.models.analysis import AnalysisResult

class ContentAnalyzer(Analyzer):
    def __init__(self, api_client: BaseApiClient):
        self.api_client = api_client

    async def analyze(self, url: str) -> AnalysisResult:
        data = {"url": url}
        response = await self.api_client.post("/projects/analyze", data)
        
        content_score = response.get("contentScore", 0)
        word_count = response.get("wordCount", 0)
        readability = response.get("readabilityScore", 0)
        topic_relevance = response.get("topicRelevanceScore", 0)

        return AnalysisResult(
            score=content_score,
            metrics={
                "word_count": word_count,
                "readability": readability,
                "topic_relevance": topic_relevance
            }
        )