from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    session
)

from flask_login import current_user
from . import db
from . import contracts
from .models import Favourite
import json

favouritesbp = Blueprint("favourites", __name__)

# GET and POST request for favourites page
"""
payload = {
    "occasion" : <occasion_name>
    "weather" : <weather_name>
    "favouriteUrl" : <favouriteUrl>
}
"""


@favouritesbp.route("/favourites/<int:userid>", methods=["POST", "GET"])
def favourites(userid=None):
    if request.method == "GET":
        favourite_query = Favourite.query.filter_by(userid=int(userid))

        favourite_resp = favourite_query.all()

        sorted_fav_list = {}

        for row in favourite_resp:
            fav = json.loads(json.dumps(Favourite.serialize(row)))

            if fav["search_occasion"] in sorted_fav_list.keys():
                curr_list = list(sorted_fav_list[fav["search_occasion"]])
                curr_list.append(fav)
                sorted_fav_list[fav["search_occasion"]] = curr_list
            else:
                sorted_fav_list[fav["search_occasion"]] = [fav]

        print("hitting api")
        return render_template("favourites.html", user=current_user, sorted_fav_list=sorted_fav_list,
                               enumerate=enumerate)

    req_json_body = request.json

    favourite_url = ""
    search_occasion = ""
    search_weather = ""

    userid = session[contracts.SessionParameters.USERID]
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

    if contracts.FavouritesContrastRequest.FAVOURITE_URL_KEY in req_json_body:
        favourite_url = req_json_body[contracts.FavouritesContrastRequest.FAVOURITE_URL_KEY]

    if contracts.FavouritesContrastRequest.SEARCH_OCCASION_KEY in req_json_body:
        search_occasion = req_json_body[contracts.FavouritesContrastRequest.SEARCH_OCCASION_KEY]

    if contracts.FavouritesContrastRequest.SEARCH_WEATHER_KEY in req_json_body:
        search_weather = req_json_body[contracts.FavouritesContrastRequest.SEARCH_WEATHER_KEY]

    # For the post request.
    if "actionToBePerformed" in req_json_body.keys() and req_json_body["actionToBePerformed"] == "ADD_NEW_FAVOURITES":

        new_favourite = Favourite(
            userid=userid,
            favourite_url=favourite_url,
            search_occasion=search_occasion,
            search_weather=search_weather
        )

        db.session.add(new_favourite)
        db.session.commit()

        return "Adding favourite success"

    elif "actionToBePerformed" in req_json_body.keys() and req_json_body["actionToBePerformed"] == "FETCH_FAVOURITES":
        favourite_query = Favourite.query.filter_by(userid=int(userid))
        # print(favourite_list)
        if favourite_url != "":
            favourite_query = favourite_query.filter_by(
                favourite_url=favourite_url)
        if search_occasion != "":
            favourite_query = favourite_query.filter_by(
                search_occasion=search_occasion)
        if search_weather != "":
            favourite_query = favourite_query.filter_by(
                search_weather=search_weather)

        favourite_resp = favourite_query.all()
        # print(favourite_list[0])

        sorted_fav_list = {}

        for row in favourite_resp:
            fav = json.loads(json.dumps(Favourite.serialize(row)))

            if fav["search_occasion"] in sorted_fav_list.keys():
                curr_list = list(sorted_fav_list[fav["search_occasion"]])
                curr_list.append(fav)
                sorted_fav_list[fav["search_occasion"]] = curr_list
            else:
                sorted_fav_list[fav["search_occasion"]] = [fav]

        print("hitting api")
        return render_template("favourites.html", user=current_user, sorted_fav_list=sorted_fav_list,
                               enumerate=enumerate)

    else:
        favourite_query = Favourite.query.filter_by(userid=int(userid))
        # print(favourite_list)
        if favourite_url != "":
            favourite_query = favourite_query.filter_by(
                favourite_url=favourite_url)
        # if search_occasion != "":
        #     favourite_query = favourite_query.filter_by(search_occasion=search_occasion)
        # if search_weather != "":
        #     favourite_query = favourite_query.filter_by(search_weather=search_weather)

        favourite_resp = favourite_query.all()
        for row in favourite_resp:
            db.session.delete(row)
        db.session.commit()
        response = dict()
        response["Message"] = "Delete Success"
        return jsonify(response), 200
