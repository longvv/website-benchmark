from app.interfaces.analyzer import Analyzer
from app.api_clients.google_pagespeed_client import GooglePageSpeedClient
from app.models.analysis import AnalysisResult

class PerformanceAnalyzer(Analyzer):
    def __init__(self, api_client: GooglePageSpeedClient):
        self.api_client = api_client

    async def analyze(self, url: str) -> AnalysisResult:
        data = await self.api_client.run_pagespeed(url)
        
        lighthouse_result = data.get("lighthouseResult", {})
        performance_score = lighthouse_result.get("categories", {}).get("performance", {}).get("score", 0) * 100

        metrics = lighthouse_result.get("audits", {})
        fcp = metrics.get("first-contentful-paint", {}).get("numericValue")
        lcp = metrics.get("largest-contentful-paint", {}).get("numericValue")
        cls = metrics.get("cumulative-layout-shift", {}).get("numericValue")
        tti = metrics.get("interactive", {}).get("numericValue")

        return AnalysisResult(
            score=performance_score,
            metrics={
                "first_contentful_paint": fcp,
                "largest_contentful_paint": lcp,
                "cumulative_layout_shift": cls,
                "time_to_interactive": tti
            }
        )