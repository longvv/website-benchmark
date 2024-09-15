from app.interfaces.analyzer import Analyzer
from app.analyzers.performance_analyzer import PerformanceAnalyzer
from app.analyzers.ux_analyzer import UXAnalyzer
from app.analyzers.content_analyzer import ContentAnalyzer
from app.analyzers.visual_analyzer import VisualAnalyzer
from app.analyzers.security_analyzer import SecurityAnalyzer
from app.api_clients.google_pagespeed_client import GooglePageSpeedClient
from app.api_clients.base_api_client import BaseApiClient
from app.config.settings import settings

class AnalyzerFactory:
    @staticmethod
    def create_analyzer(module: str) -> Analyzer:
        if module == "performance":
            return PerformanceAnalyzer(GooglePageSpeedClient())
        elif module == "ux":
            return UXAnalyzer(BaseApiClient("https://insights.hotjar.com/api/v1", settings.HOTJAR_API_KEY))
        elif module == "content":
            return ContentAnalyzer(BaseApiClient("https://api.marketmuse.com/v1", settings.MARKETMUSE_API_KEY))
        elif module == "visual":
            return VisualAnalyzer(BaseApiClient("https://api.eyequant.com/v2", settings.EYEQUANT_API_KEY))
        elif module == "security":
            return SecurityAnalyzer(BaseApiClient("https://api.darktrace.com/v1", settings.DARKTRACE_API_KEY))
        else:
            raise ValueError(f"Unknown module: {module}")