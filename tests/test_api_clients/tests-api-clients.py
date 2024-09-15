import pytest
from unittest.mock import patch, AsyncMock
from app.api_clients.google_pagespeed_client import GooglePageSpeedClient

@pytest.fixture
def google_pagespeed_client():
    return GooglePageSpeedClient()

@pytest.mark.asyncio
async def test_run_pagespeed(google_pagespeed_client):
    mock_response = {
        "lighthouseResult": {
            "categories": {
                "performance": {"score": 0.85}
            }
        }
    }

    with patch('app.api_clients.base_api_client.BaseApiClient.get', new_callable=AsyncMock) as mock_get:
        mock_get.return_value = mock_response
        result = await google_pagespeed_client.run_pagespeed("https://example.com")

    assert result == mock_response
    mock_get.assert_called_once_with(
        "/pagespeedonline/v5/runPagespeed",
        params={
            "url": "https://example.com",
            "key": google_pagespeed_client.api_key,
            "strategy": "mobile"
        }
    )
