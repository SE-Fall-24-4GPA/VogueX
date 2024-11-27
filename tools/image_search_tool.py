from typing import List, Dict
from pydantic import BaseModel
from duckduckgo_search import DDGS
from random import choice

class ImageSearchTool(BaseModel):
    fashion_retailers: Dict[str, List[str]] = {
        'casual': [
            'https://www.asos.com/search/?q=',
            'https://www.zara.com/search?searchTerm=',
            'https://www.hm.com/search?q='
        ],
        'formal': [
            'https://www.nordstrom.com/sr?keyword=',
            'https://www.macys.com/shop/featured/',
            'https://www.brooksbrothers.com/search?q='
        ],
        'sporty': [
            'https://www.nike.com/w?q=',
            'https://www.adidas.com/search?q=',
            'https://www.underarmour.com/search?q='
        ],
        'default': [
            'https://www.amazon.com/s?k=fashion+',
            'https://www.asos.com/search/?q=',
            'https://www.nordstrom.com/sr?keyword='
        ]
    }

    def search_fashion_images(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        with DDGS() as ddgs:
            images = list(ddgs.images(
                query + " fashion_outfit",
                max_results=max_results
            ))
            
            # Get appropriate retailer list and randomly select for each result
            retailer_urls = self._get_retailer_urls(query)
            
            return [
                {
                    'image_url': img['image'],
                    'shopping_url': choice(retailer_urls) + query.replace(' ', '+'),
                    'title': img.get('title', ''),
                    'description': img.get('title', '')
                }
                for img in images
            ]

    def _get_retailer_urls(self, query: str) -> List[str]:
        query_lower = query.lower()
        for style, urls in self.fashion_retailers.items():
            if style in query_lower:
                return urls
        return self.fashion_retailers['default']

# test Image search tool
def test_image_search():
    ist = ImageSearchTool()
    imgs = ist.search_fashion_images(query="casual jackets")
    print(imgs)

if __name__ == '__main__':
    test_image_search()