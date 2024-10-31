from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
)

from flask_login import login_required, current_user
from . import models
import json

views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route("/procResult", methods=["POST"])
@login_required
def procResult():
    if request.method == "POST":
        linksData = request.json["resultLinks"]["links"]
        strLinks = ""
        for links in linksData:
            strLinks += links + " || "
        linksData = strLinks
        return redirect(url_for("views.results", user=current_user, data=linksData))
    
@views.route('/results')
@login_required
def results():
    image_paths = request.args.get('images', '').split(',')
    return render_template('results.html', ldata=image_paths, user=current_user, enumerate=enumerate)



# @views.route("/results", methods=["POST", "GET"])
# @login_required
# def results():
#     linksData = str(request.args.to_dict())[2:-2].split(" || ")
#     return render_template(
#         "results.html", user=current_user, ldata=linksData, enumerate=enumerate
#     )


@views.route("/profile", methods=["POST", "GET"])
@login_required
def profile():
    preferenceObject = models.Preference.query.filter_by(
        userid=int(current_user.id)
    ).first()
    if preferenceObject:
        prefData = json.loads(preferenceObject.preferences)
    else:
        preferenceObject = models.Preference(
            userid=int(current_user.id), preferences=""
        )
        prefData = {}

    return render_template("profile.html", user=current_user, prefData=prefData)
