from abc import ABC, abstractmethod
from typing import Any, Dict

class ApiClient(ABC):
    @abstractmethod
    async def get(self, endpoint: str, params: Dict[str, Any] = None) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        pass