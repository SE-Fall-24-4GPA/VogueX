from typing import List
from pydantic import BaseModel
from duckduckgo_search import DDGS

class ImageSearchTool(BaseModel):
    @staticmethod
    def search_fashion_images(query: str, max_results: int = 5) -> List[str]:
        with DDGS() as ddgs:
            images = list(ddgs.images(
                query + " fashion outfit",
                max_results=max_results
            ))
            return [img['image'] for img in images]
