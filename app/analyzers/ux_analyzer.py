from app.interfaces.analyzer import Analyzer
from app.api_clients.base_api_client import BaseApiClient
from app.models.analysis import AnalysisResult

class UXAnalyzer(Analyzer):
    def __init__(self, api_client: BaseApiClient):
        self.api_client = api_client

    async def analyze(self, url: str) -> AnalysisResult:
        # This is a simplified example. In a real-world scenario,
        # you'd need to make multiple API calls to get comprehensive UX data.
        data = await self.api_client.get("/sites")
        
        site_id = data[0]["id"]
        heatmap_data = await self.api_client.get(f"/sites/{site_id}/heatmaps")

        click_score = len(heatmap_data.get("clicks", [])) / 100  # Normalize to 0-1
        scroll_score = heatmap_data.get("scroll", {}).get("average", 0) / 100

        ux_score = (click_score + scroll_score) / 2 * 100  # Average and convert to 0-100

        return AnalysisResult(
            score=ux_score,
            metrics={
                "click_engagement": click_score * 100,
                "scroll_depth": scroll_score * 100
            }
        )