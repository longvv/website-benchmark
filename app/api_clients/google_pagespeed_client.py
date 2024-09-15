from app.api_clients.base_api_client import BaseApiClient
from app.config.settings import settings
from typing import Dict, Any

class GooglePageSpeedClient(BaseApiClient):
    def __init__(self):
        super().__init__("https://www.googleapis.com", settings.GOOGLE_PAGESPEED_API_KEY)

    async def run_pagespeed(self, url: str) -> Dict[str, Any]:
        params = {
            "url": url,
            "key": self.api_key,
            "strategy": "mobile"
        }
        return await self.get("/pagespeedonline/v5/runPagespeed", params)