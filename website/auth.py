from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from . import contracts

auth = Blueprint("auth", __name__)


# Login authentication module that takes user email and password as input and validates against the database before giving authorization to the page
@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                session[contracts.SessionParameters.USERID] = user.get_id()
                login_user(user, remember=True)
                return render_template("home.html", user=user)
            else:
                flash("ERRORIncorrect password, try again.", category="error")
        else:
            flash("ERROR Email does not exist.", category="error")
    
    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    session.pop(contracts.SessionParameters.USERID, None)
    return redirect(url_for("auth.login"))


# get and post both come to the same aciton. When we hit the sign up end point on the URL, a get request is generated.
# This generates the view. Submitting the form hits the same action. We run the logic for post now.
@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    # For the post request.
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        last_name = request.form.get("lastName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        gender = request.form.get("gender")
        phone_number = request.form.get("phoneNumber")
        city = request.form.get("city")
        age = request.form.get("age")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("ERROR Email already exists.", category="error")
        elif len(email) < 4:
            flash("ERROR Email must be greater than 3 characters.", category="error")
        elif len(first_name) < 2:
            flash("ERROR First name must be greater than 1 character.", category="error")
        elif password1 != password2:
            flash("ERROR Passwords don't match.", category="error")
        elif len(password1) < 7:
            flash("ERROR Password must be at least 7 characters.", category="error")
        elif int(age) < 18 or int(age) > 90:
            flash("ERROR Please enter a valid age", category="error")
        else:
            new_user = User(
                email=email,
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                city=city,
                age=age,
                phone_number=phone_number,
                password=generate_password_hash(password1),
            )
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created!", category="success")
            return render_template("home.html", user=new_user)

    # For get request.
    return render_template("sign_up.html", user=current_user)


# Profile Update function that takes phone number, city, age, user_id as input from the form data and submits a POST request to update the input values to the database.
@auth.route("/profile-update", methods=["GET", "POST"])
def profile_update():
    # For the post request.
    if request.method == "POST":
        phone_number = request.form.get("phoneNumber")
        city = request.form.get("city")
        age = request.form.get("age")
        userid = request.form.get("userid")

        user = User.query.filter_by(id=int(userid)).first()

        if int(age) < 18 or int(age) > 90:
            flash("ERROR Please enter a valid age", category="error")
        else:
            user.age = age
            user.city = city
            user.phone_number = phone_number
            db.session.commit()
            flash("Account updated!", category="success")
            return render_template("home.html", user=user)

    # For get request.
    return render_template("profile.html", user=current_user)
