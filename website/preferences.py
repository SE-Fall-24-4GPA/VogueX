# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

import json
from flask import (
    Blueprint,
    flash,
    jsonify,
    render_template,
    session,
    request,
)
from flask_login import login_required, current_user

from website import contracts
from . import models
from . import db

preferencesbp = Blueprint("preferences", __name__, url_prefix="/")


@preferencesbp.route("/default-preferences", methods=["GET"])
def get_default_preferences():
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
    default_preferences = {
        "male": {
            "preferences": [
                {"type": "suit", "color": "black", "occasion": "formal"},
                {"type": "tshirt", "color": "blue", "occasion": "beach"},
                {"type": "shirt", "color": "navy-blue", "occasion": "office"},
            ]
        },
        "female": {
            "preferences": [
                {"type": "suit", "color": "black", "occasion": "formal"},
                {"type": "top", "color": "blue", "occasion": "beach"},
                {"type": "shirt", "color": "navy-blue", "occasion": "office"},
                {"type": "floral-skirt", "color": "black", "occasion": "date"},
            ]
        },
    }
    return jsonify(default_preferences)


@preferencesbp.route("/preferences", methods=["GET"])
def get_preferences():
    """
    response :

    {
        "
    }

    """
    preferences = {
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
    print(preferences)

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
    # query the preferences table and check if preferences have been saved or not
    userid = session[contracts.SessionParameters.USERID]
    preferencesObj = models.Preference.query.filter_by(userid=int(userid)).first()
    if not preferencesObj:
        return (
            jsonify(
                {
                    "error_code": contracts.ErrorCodes.OBJECT_NOT_SAVED,
                    "error": "preferences not saved",
                }
            ),
            400,
        )

    userpreferences = preferencesObj.preferences
    response = json.loads(userpreferences)
    return jsonify(response), 200


def build_json(formData):
    newDict = {}
    for key in formData:
        newDict[key.replace("'", "")] = formData[key].replace("'", "")
    jsonData = {"preferences": str(newDict).replace("'", '"')}
    return jsonData


@preferencesbp.route("/preferences", methods=["POST"])
@login_required
def post_preferences():
    if request.content_type == "application/x-www-form-urlencoded":
        req = build_json(request.form.to_dict())
    else:
        req = request.json
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

    userid = session["userid"]
    user_preferences = "{}"

    if contracts.PreferenceContractRequest.PREFERENCES in req:
        user_preferences = req[contracts.PreferenceContractRequest.PREFERENCES]

    preferenceObject = models.Preference.query.filter_by(userid=int(userid)).first()
    if not preferenceObject:
        preferenceObject = models.Preference(
            userid=int(userid), preferences=json.dumps(user_preferences)
        )
        db.session.add(preferenceObject)
    else:
        preferenceObject.preferences = user_preferences
    db.session.commit()
    if request.content_type == "application/x-www-form-urlencoded":
        flash("Preferences updated!", category="success")
        return render_template("home.html", user=current_user)
    else:
        return jsonify({"status": 200}), 200
