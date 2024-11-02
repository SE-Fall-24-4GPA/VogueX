# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

import pytest
from website import preferences


def login_user(client):
    mimetype = "application/x-www-form-urlencoded"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    # This user is not present in the db
    data = {"email": "test@gmail.com", "password": "password123"}
    url = "/login"

    response = client.post(url, data=data, headers=headers)
    if response.status_code == 200:
        return True
    return False


def test_get_default_preferences(app):
    client = app.test_client()
    if not login_user(client):
        assert False
    result = client.get("/default-preferences")
    assert result.json


def test_post_preferences(app):
    client = app.test_client()
    if not login_user(client):
        assert False
    payload = {
        "preferences": {
            "formal": [
                {
                    "type": "suit",
                    "color": "black",
                }
            ],
            "beach": [
                {
                    "type": "tshirt",
                    "color": "blue",
                }
            ],
            "date": [
                {
                    "type": "shirt",
                    "color": "navy-blue",
                }
            ],
        }
    }

    mimetype = "application/x-www-form-urlencoded"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    url = "/preferences"

    response = client.post(url, data=payload, headers=headers)
    assert response.status_code == 200
