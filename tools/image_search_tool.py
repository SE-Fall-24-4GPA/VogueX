from typing import List
from pydantic import BaseModel
from duckduckgo_search import DDGS


class ImageSearchTool(BaseModel):
    def search_fashion_images(self, query: str, max_results: int = 5) -> List[str]:
        with DDGS() as ddgs:
            images = list(ddgs.images(
                query + "fashion_outfit",
                max_results=max_results
            ))
            return [img['image'] for img in images]


# test Image search tool
def test_image_search():
    ist = ImageSearchTool()
    imgs = ist.search_fashion_images(query="jackets")
    print(imgs)

if __name__ == '__main__':
    test_image_search()