# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_flask_backend():
    async def mock_flask_app():
        class MockApp:
            @staticmethod
            async def test_route():
                return {"message": "This is a test message"}
        
        return MockApp()

    async with AsyncClient(app=mock_flask_app()) as client:
        response = await client.get("/test")

    assert response.status_code == 200
    assert response.json() == {"message": "This is a test message"}

@pytest.mark.asyncio
async def test_flask_backend_with_params():
    async def mock_flask_app():
        class MockApp:
            @staticmethod
            async def test_route(param1: str, param2: int):
                return {"param1": param1, "param2": param2}
        
        return MockApp()

    async with AsyncClient(app=mock_flask_app()) as client:
        response = await client.get("/test", params={"p1": "value1", "p2": 42})

    assert response.status_code == 200
    assert response.json() == {"param1": "value1", "param2": 42}

@pytest.mark.asyncio
async def test_flask_backend_error_handling():
    async def mock_flask_app():
        class MockApp:
            @staticmethod
            async def test_route():
                raise ValueError("Mock error occurred")
        
        return MockApp()

    async with AsyncClient(app=mock_flask_app()) as client:
        response = await client.get("/test")

    assert response.status_code == 500
    assert "Mock error occurred" in str(response.content)
