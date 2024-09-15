from app.models.analysis import AnalysisRequest, AnalysisResponse, AnalysisResult
from app.services.analyzer_factory import AnalyzerFactory

class AnalysisService:
    @staticmethod
    async def analyze(request: AnalysisRequest) -> AnalysisResponse:
        results = {}
        for module in request.modules:
            analyzer = AnalyzerFactory.create_analyzer(module)
            results[module] = await analyzer.analyze(str(request.url))
        
        return AnalysisResponse(url=request.url, results=results)