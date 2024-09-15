from app.interfaces.analyzer import Analyzer
from app.api_clients.base_api_client import BaseApiClient
from app.models.analysis import AnalysisResult

class SecurityAnalyzer(Analyzer):
    def __init__(self, api_client: BaseApiClient):
        self.api_client = api_client

    async def analyze(self, url: str) -> AnalysisResult:
        params = {"domain": url}
        data = await self.api_client.get("/threats", params)
        
        threats = data.get("threats", [])
        threat_count = len(threats)
        severity_sum = sum(threat["severity"] for threat in threats)
        
        if threat_count == 0:
            security_score = 100
        else:
            average_severity = severity_sum / threat_count
            security_score = max(0, 100 - (average_severity * 10))  # Higher severity lowers the score

        return AnalysisResult(
            score=security_score,
            metrics={
                "threat_count": threat_count,
                "average_severity": average_severity if threat_count > 0 else 0
            }
        )