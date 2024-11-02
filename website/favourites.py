# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

from flask import Blueprint, render_template, request, jsonify, session,flash,redirect,url_for

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
@favouritesbp.route("/favourites/", methods=["GET"])
def favourites(userid=None):
    if request.method == "GET":
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

        favourite_query = Favourite.query.filter_by(userid=int(userid))

        favourite_resp = favourite_query.all()

        sorted_fav_list = {}

        for row in favourite_resp:
            fav = json.loads(json.dumps(Favourite.serialize(row)))

            if fav["ratings"] in sorted_fav_list.keys():
                curr_list = list(sorted_fav_list[fav["ratings"]])
                curr_list.append(fav)
                sorted_fav_list[fav["ratings"]] = curr_list
            else:
                sorted_fav_list[fav["ratings"]] = [fav]

        print("hitting api")
        return render_template(
            "favourites.html",
            user=current_user,
            sorted_fav_list=sorted_fav_list,
            enumerate=enumerate,
        )



@favouritesbp.route("/favourites/", methods=["POST"])
def favourites_post(userid=None):
    req_json_body = request.json

    favourite_url = ""
    review = ""

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
        favourite_url = req_json_body[
            contracts.FavouritesContrastRequest.FAVOURITE_URL_KEY
        ]

    if contracts.FavouritesContrastRequest.REVIEW_KEY in req_json_body:
        review = req_json_body[
            contracts.FavouritesContrastRequest.REVIEW_KEY
        ]

    # For the post request.
    if (
        "actionToBePerformed" in req_json_body.keys()
        and req_json_body["actionToBePerformed"] == "ADD_NEW_FAVOURITES"
    ):

        new_favourite = Favourite(
            userid=userid,
            favourite_url=favourite_url,
            review=review,
        )

        db.session.add(new_favourite)
        db.session.commit()

        return "Adding favourite success"

    elif (
        "actionToBePerformed" in req_json_body.keys()
        and req_json_body["actionToBePerformed"] == "FETCH_FAVOURITES"
    ):
        favourite_query = Favourite.query.filter_by(userid=int(userid))
        # print(favourite_list)
        if favourite_url != "":
            favourite_query = favourite_query.filter_by(favourite_url=favourite_url)
        if review != "":
            favourite_query = favourite_query.filter_by(review=review)

        favourite_resp = favourite_query.all()
        # print(favourite_list[0])

        # sorted_fav_list = {}

        # for row in favourite_resp:
        #     fav = json.loads(json.dumps(Favourite.serialize(row)))

        #     if fav["ratings"] in sorted_fav_list.keys():
        #         curr_list = list(sorted_fav_list[fav["ratings"]])
        #         curr_list.append(fav)
        #         sorted_fav_list[fav["ratings"]] = curr_list
        #     else:
        #         sorted_fav_list[fav["ratings"]] = [fav]

        print("hitting api")
        return render_template(
            "favourites.html",
            user=current_user,
            sorted_fav_list=favourite_resp,
            enumerate=enumerate,
        )

        """ else:
        favourite_query = Favourite.query.filter_by(userid=int(userid))
        # print(favourite_list)
        if favourite_url != "":
            favourite_query = favourite_query.filter_by(favourite_url=favourite_url)
        # if search_occasion != "":
        #     favourite_query = favourite_query.filter_by(search_occasion=search_occasion)
        # if search_weather != "":
        #     favourite_query = favourite_query.filter_by(search_weather=search_weather)
        favourite_resp = favourite_query.all()
        for row in favourite_resp:
            db.session.delete(row)
        db.session.commit()
        flash("Favourite deleted", category='success')
        #return redirect(url_for('favourites.favourites', userid=current_user.id))
        
        response = dict()
        response["Message"] = "Delete Success"
        return jsonify(response), 200       """

@favouritesbp.route('/favourites/', methods=['DELETE'])
def delete_favourite():
    data = request.json
    userid = session.get(contracts.SessionParameters.USERID)
    if not userid:
        return jsonify({'error': 'User not logged in'}), 403
        
    favourite_query = Favourite.query.filter_by(userid=int(userid)) 

    favourite_url = data.get('favourite_url')
    if favourite_url:
        favourite_query = favourite_query.filter_by(favourite_url=favourite_url)
        favourite_resp = favourite_query.all()
        for row in favourite_resp:
            db.session.delete(row)
        db.session.commit()
        return jsonify({'message': 'Favourite deleted successfully'}), 200
    else:
        return jsonify({'error': 'Favourite not found'}), 404
    return jsonify({'error': 'Favourite URL not provided'}), 400

@favouritesbp.route('/favreview', methods=['POST'])
def post_review():
    data = request.get_json()
    userid = session.get(contracts.SessionParameters.USERID)

    review = data.get('review')

    # Find the favourite entry by userid and favourite_url
    favourite_url = data.get('url')  # You need to pass the URL from the front end

    favourite_entry = Favourite.query.filter_by(userid=userid, favourite_url=favourite_url).first()
    
    if favourite_entry:
        # Update the existing entry
        favourite_entry.review = review
        db.session.commit()
        return jsonify({'message': 'Review updated successfully'}), 200
    else:
        # Optionally handle cases where the favourite entry does not exist
        return jsonify({'message': 'Favourite entry not found'}), 404