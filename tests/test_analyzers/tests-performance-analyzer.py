import pytest
from unittest.mock import AsyncMock, MagicMock
from app.analyzers.performance_analyzer import PerformanceAnalyzer
from app.api_clients.google_pagespeed_client import GooglePageSpeedClient

@pytest.fixture
def mock_pagespeed_client():
    client = MagicMock(spec=GooglePageSpeedClient)
    client.run_pagespeed = AsyncMock()
    return client

@pytest.fixture
def performance_analyzer(mock_pagespeed_client):
    return PerformanceAnalyzer(mock_pagespeed_client)

@pytest.mark.asyncio
async def test_performance_analyzer(performance_analyzer, mock_pagespeed_client):
    mock_pagespeed_client.run_pagespeed.return_value = {
        "lighthouseResult": {
            "categories": {
                "performance": {"score": 0.85}
            },
            "audits": {
                "first-contentful-paint": {"numericValue": 1000},
                "largest-contentful-paint": {"numericValue": 2000},
                "cumulative-layout-shift": {"numericValue": 0.1},
                "interactive": {"numericValue": 3000}
            }
        }
    }

    result = await performance_analyzer.analyze("https://example.com")

    assert result.score == 85
    assert result.metrics["first_contentful_paint"] == 1000
    assert result.metrics["largest_contentful_paint"] == 2000
    assert result.metrics["cumulative_layout_shift"] == 0.1
    assert result.metrics["time_to_interactive"] == 3000

    mock_pagespeed_client.run_pagespeed.assert_called_once_with("https://example.com")
