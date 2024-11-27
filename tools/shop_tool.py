from typing import Dict, List, Optional
from pydantic import BaseModel
from urllib.parse import quote_plus


class ShoppingLinkTool(BaseModel):
    retailers: Dict[str, Dict[str, List[str]]] = {
        'casual': {
            'affordable': [
                'https://www.hm.com/search?q=',
                'https://www.uniqlo.com/search?q=',
                'https://oldnavy.gap.com/browse/search.do?searchText='
            ],
            'midrange': [
                'https://www.zara.com/search?searchTerm=',
                'https://www.madewell.com/search?q=',
                'https://www.asos.com/search/?q='
            ],
            'luxury': [
                'https://www.nordstrom.com/sr?keyword=',
                'https://www.ssense.com/en-us/search?q=',
                'https://www.farfetch.com/shopping/search?q='
            ]
        },
        'formal': {
            'affordable': [
                'https://www.macys.com/shop/search?keyword=',
                'https://bananarepublic.gap.com/browse/search.do?searchText='
            ],
            'midrange': [
                'https://www.jcrew.com/search?q=',
                'https://www.tedbaker.com/search?q='
            ],
            'luxury': [
                'https://www.neimanmarcus.com/search.jsp?q=',
                'https://www.matchesfashion.com/search?q='
            ]
        }
    }

    def generate_shopping_links(
            self,
            query: str,
            style: str = 'casual',
            price_range: str = 'midrange',
            num_links: int = 3
    ) -> List[Dict[str, str]]:
        """
        Generate shopping links for a given fashion query
        """
        style = style.lower()
        price_range = price_range.lower()

        if style not in self.retailers:
            style = 'casual'

        if price_range not in self.retailers[style]:
            price_range = 'midrange'

        base_urls = self.retailers[style][price_range]
        encoded_query = quote_plus(query)

        return [{
            'retailer': url.split('/')[2],
            'url': f"{url}{encoded_query}"
        } for url in base_urls[:num_links]]


def test_shopping_link_tool():
    tool = ShoppingLinkTool()
    links = tool.generate_shopping_links(
        query="blue dress shirt",
        style="formal",
        price_range="midrange"
    )
    print(links)


if __name__ == "__main__":
    test_shopping_link_tool()