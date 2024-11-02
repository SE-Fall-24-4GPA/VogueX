# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

import pytest
from website import shopping


def test_shopping_results():
    image_url = "https://www-whattowearonvacation-com.exactdn.com/wp-content/uploads/2019/09/good-walking-shoes-for-Japan.jpg"
    s = shopping.Shopping()
    assert s.shopping_results(image_url)
