import pytest
from unittest.mock import patch, AsyncMock
from app.services.analysis_service import AnalysisService
from app.models.analysis import AnalysisRequest, AnalysisResult

@pytest.mark.asyncio
async def test_analysis_service():
    mock_request = AnalysisRequest(url="https://example.com", modules=["performance", "ux"])
    mock_performance_result = AnalysisResult(score=85, metrics={"fcp": 1000})
    mock_ux_result = AnalysisResult(score=90, metrics={"click_engagement": 80})

    with patch('app.services.analyzer_factory.AnalyzerFactory.create_analyzer') as mock_create_analyzer:
        mock_performance_analyzer = AsyncMock()
        mock_performance_analyzer.analyze.return_value = mock_performance_result
        mock_ux_analyzer = AsyncMock()
        mock_ux_analyzer.analyze.return_value = mock_ux_result

        mock_create_analyzer.side_effect = [mock_performance_analyzer, mock_ux_analyzer]

        result = await AnalysisService.analyze(mock_request)

    assert result.url == "https://example.com"
    assert "performance" in result.results
    assert result.results["performance"] == mock_performance_result
    assert "ux" in result.results
    assert result.results["ux"] == mock_ux_result

    mock_create_analyzer.assert_any_call("performance")
    mock_create_analyzer.assert_any_call("ux")
    mock_performance_analyzer.analyze.assert_called_once_with("https://example.com")
    mock_ux_analyzer.analyze.assert_called_once_with("https://example.com")
