from abc import ABC, abstractmethod
from app.models.analysis import AnalysisResult

class Analyzer(ABC):
    @abstractmethod
    async def analyze(self, url: str) -> AnalysisResult:
        pass