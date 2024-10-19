import pytest
from website import shopping

def test_shopping_results():
    image_url="https://www-whattowearonvacation-com.exactdn.com/wp-content/uploads/2019/09/good-walking-shoes-for-Japan.jpg"
    s=shopping.Shopping()
    assert s.shopping_results(image_url)
    