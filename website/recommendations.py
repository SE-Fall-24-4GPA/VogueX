# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

import functools
from flask import (
    Blueprint,
    flash,
    g,
    jsonify,
    redirect,
    render_template,
    request,
    session,
    url_for,
    send_from_directory,
)

from . import contracts

from werkzeug.security import check_password_hash, generate_password_hash
from . import models
from datetime import datetime

recommendationsbp = Blueprint("recommendationsbp", __name__, url_prefix="/")


"""
newpayload = {
    "gender" : <gender>
    "masterCategory" : <mastercategory>
    "subCategory" : <subcategory>
    "articleType" : <articletype>
    "baseColour" : <basecolour>
    "season" : <season>
    "usage" : <usage>
}
"""


@recommendationsbp.route("/newrecommendations", methods=["POST"])
def get_newrecommendations():
    req_json_body = request.json
    gender = ""
    masterCategory = ""
    subCategory = ""
    articleType = ""
    baseColour = ""
    season = ""
    usage = ""

    if contracts.SessionParameters.USERID not in session:
        return (
            jsonify(
                {
                    "error": "user not logged in",
                    "error_code": contracts.ErrorCodes.USER_NOT_LOGGED_IN,
                }
            ),
            403,
        )

    userid = session[contracts.SessionParameters.USERID]

    if contracts.NewRecommendationContractRequest.GENDER_KEY in req_json_body:
        gender = req_json_body[contracts.NewRecommendationContractRequest.GENDER_KEY]

    if contracts.NewRecommendationContractRequest.MASTER_CATEGORY_KEY in req_json_body:
        masterCategory = req_json_body[
            contracts.NewRecommendationContractRequest.MASTER_CATEGORY_KEY
        ]

    if contracts.NewRecommendationContractRequest.SUB_CATEGORY_KEY in req_json_body:
        subCategory = req_json_body[
            contracts.NewRecommendationContractRequest.SUB_CATEGORY_KEY
        ]

    if contracts.NewRecommendationContractRequest.ARTICLE_TYPE_KEY in req_json_body:
        articleType = req_json_body[
            contracts.NewRecommendationContractRequest.ARTICLE_TYPE_KEY
        ]

    if contracts.NewRecommendationContractRequest.BASE_COLOUR_KEY in req_json_body:
        baseColour = req_json_body[
            contracts.NewRecommendationContractRequest.BASE_COLOUR_KEY
        ]

    if contracts.NewRecommendationContractRequest.SEASON_KEY in req_json_body:
        season = req_json_body[contracts.NewRecommendationContractRequest.SEASON_KEY]

    if contracts.NewRecommendationContractRequest.USAGE_KEY in req_json_body:
        usage = req_json_body[contracts.NewRecommendationContractRequest.USAGE_KEY]

    from . import helper

    help = helper.NewRecommendationHelper()
    images = help.giveRecommendations(
        userid,
        gender,
        masterCategory,
        subCategory,
        articleType,
        baseColour,
        season,
        usage,
    )
    # print(images)

    recommendations = {contracts.NewRecommendationContractResponse.IMAGES: []}

    # Create a list of image paths relative to the web server's base directory
    for image in images:
        recommendations[contracts.NewRecommendationContractResponse.IMAGES].append(
            image
        )

    return jsonify(recommendations), 200

    # recommendations = dict()
    # recommendations[contracts.NewRecommendationContractResponse.IMAGES] = []
    # for image in images:
    #     img_path = 'datasets/fashion-dataset/images/' +  image
    #     recommendations[contracts.NewRecommendationContractResponse.IMAGES].append(img_path)
    # return jsonify(recommendations), 200

    # return the image path as a response to be displayed in the webpage


# ___________________________________________________________________________________________________________________________

"""
payload = {
    "occasion" : <occasion_name>
    "culture" : <culture>
    "gender": <gender>
    "ageGroup": <ageGroup>
    "city":<city>
    "dateTimeInput":<dateTimeInput> format : YYYY-MM-DDTHH:MM:SS
}
"""


@recommendationsbp.route("/recommendations", methods=["POST"])
def get_recommendations():
    req_json_body = request.json
    culture = ""
    occasion = ""
    gender = ""
    ageGroup = ""
    city = ""
    userid = "1"

    print(req_json_body)

    if contracts.SessionParameters.USERID not in session:
        return (
            jsonify(
                {
                    "error": "user not logged in",
                    "error_code": contracts.ErrorCodes.USER_NOT_LOGGED_IN,
                }
            ),
            403,
        )

    userid = session[contracts.SessionParameters.USERID]

    user = models.User.query.filter_by(id=int(userid)).first()
    if contracts.RecommendationContractRequest.CULTURE_KEY in req_json_body:
        culture = req_json_body[contracts.RecommendationContractRequest.CULTURE_KEY]

    # take from the user table
    city = user.city

    if contracts.RecommendationContractRequest.DATE_TIME_KEY in req_json_body:
        dateTimeInput = req_json_body[
            contracts.RecommendationContractRequest.DATE_TIME_KEY
        ]
        dateInput = str(dateTimeInput).split("T")[0]
        timeInput = str(dateTimeInput).split("T")[1]

    else:
        dateInput = datetime.today().strftime("%Y-%m-%d")
        timeInput = datetime.now()

    if contracts.RecommendationContractRequest.GENDER_KEY in req_json_body:
        gender = req_json_body[
            contracts.RecommendationContractRequest.GENDER_KEY
        ].lower()
    else:
        # take from the user table
        gender = "Female"

    if contracts.RecommendationContractRequest.OCCASION_KEY in req_json_body:
        occasion = req_json_body[contracts.RecommendationContractRequest.OCCASION_KEY]

    # Age
    if contracts.RecommendationContractRequest.AGE_GROUP_KEY in req_json_body:
        ageGroup = req_json_body[contracts.RecommendationContractRequest.AGE_GROUP_KEY]

    from . import helper

    help = helper.RecommendationHelper()
    links = help.giveRecommendations(
        userid=userid,
        gender=gender,
        occasion=occasion,
        city=city,
        culture=culture,
        ageGroup=ageGroup,
        date=dateInput,
        time=timeInput,
    )

    recommendations = dict()
    recommendations[contracts.RecommendationContractResponse.LINKS] = []
    for link in links:
        recommendations[contracts.RecommendationContractResponse.LINKS].append(link)
    return jsonify(recommendations), 200
