from flask import Flask, g
import json
from website.auth import auth
from website.auth import db
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import sys

sys.path.append("..")


def test_login_get(app):
    client = app.test_client()
    url = "/login"

    response = client.get(url)
    print(response.get_data())
    assert response.status_code == 200


def test_login_post(app):
    client = app.test_client()
    mimetype = "application/x-www-form-urlencoded"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    # This user is not present in the db
    data = {"email": "testxyz@gmail.com",
            "password": "password123"}
    url = "/login"

    response = client.post(url, data=data, headers=headers)
    assert response.status_code == 200
    assert "ERROR" in response.data.decode('utf-8')


def test_signup_get(app):
    client = app.test_client()
    url = "/sign-up"
    response = client.get(url)
    assert response.status_code, 200


def test_signup_post(app):
    client = app.test_client()
    url = "/sign-up"
    mimetype = "application/x-www-form-urlencoded"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    # This user is not present in the db
    data = {
        "email": "test@gmail.com",
        "firstName": "test_user",
        "lastName": "test_end_name",
        "gender": "unknown",
        "phoneNumber": 9874561230,
        "password1": "password123",
        "password2": "password123",
        "age": 25,
        "city": "Raleigh",
    }

    response = client.post(url, data=data, headers=headers)
    assert response.status_code, 200
    assert "ERROR" in response.data.decode('utf-8')


def test_login_check_positive_case(app):
    client = app.test_client()
    url = "/login"
    mimetype = "application/x-www-form-urlencoded"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    data = {
        "email": "test@gmail.com",
        "password": "password123",
    }

    response = client.post(url, data=data, headers=headers)
    assert response.status_code, 200
    assert "ERROR" not in response.data.decode('utf-8')

def test_signup_email_already_exists(app):
    client = app.test_client()
    url = "/sign-up"
    mimetype = "application/x-www-form-urlencoded"
    headers = {"Content-Type": mimetype, "Accept": mimetype}

    # Step 1: Sign up the user for the first time
    data = {
        "email": "test2@gmail.com",
        "firstName": "test_user2",
        "lastName": "test_end_name2",
        "gender": "Male",
        "phoneNumber": "5467891239",
        "password1": "password123",
        "password2": "password123",
        "age": 25,
        "city": "Raleigh",
    }

    response = client.post(url, data=data, headers=headers)
    assert response.status_code == 200  # Successful sign-up
    assert "ERROR" in response.data.decode('utf-8')

    # Step 2: Attempt to sign up with the same email again
    response = client.post(url, data=data, headers=headers)
    assert response.status_code == 200  # Check if still valid response
    # Now check for the flash message
    response_data = response.data.decode('utf-8')
    assert "Email already exists." in response.data.decode('utf-8')
    assert "ERROR" in response.data.decode('utf-8')

def test_login_fail_user_not_exist(app):
    client = app.test_client()
    response = client.post('/login', data={
            'email': 'nonexistent@example.com',
            'password': 'password123'
    })
    assert response.status_code == 200  # Check if still valid response
    # Now check for the flash message
    response_data = response.data.decode('utf-8')
    assert "Email does not exist." in response.data.decode('utf-8')
    assert "ERROR" in response.data.decode('utf-8')

def test_login_fail_incorrect_password(app):
    client = app.test_client()
    data = {
        "email": "test3@gmail.com",
        "firstName": "test_user2",
        "lastName": "test_end_name2",
        "gender": "Male",
        "phoneNumber": "84561793217",
        "password1": "password123",
        "password2": "password123",
        "age": 25,
        "city": "Raleigh",
    }
    mimetype = "application/x-www-form-urlencoded"
    headers = {"Content-Type": mimetype, "Accept": mimetype}
    response = client.post("/sign-up", data=data, headers=headers)
    assert response.status_code == 200  # Successful sign-up
    response = client.post('/login', data={
            'email': 'test3@gmail.com',
            'password': '1122334455'
    })
    assert response.status_code == 200  # Check if still valid response
    # Now check for the flash message
    assert "Incorrect password, try again." in response.data.decode('utf-8')
    assert "ERROR" in response.data.decode('utf-8')

def test_signup_short_email(app):
    client = app.test_client()
    url = "/sign-up"
    data = {
        "email": "ab",
        "firstName": "First",
        "lastName": "Last",
        "gender": "Male",
        "phoneNumber": "1234567890",
        "password1": "password123",
        "password2": "password123",
        "age": 25,
        "city": "Raleigh",
    }
    response = client.post(url, data=data)
    assert response.status_code == 200
    withresponse_data = response.data.decode('utf-8')
    assert "Email must be greater than 3 characters." in response.data.decode('utf-8')
    assert "ERROR" in response.data.decode('utf-8')
    
def test_signup_short_first_name(app):
    client = app.test_client()
    url = "/sign-up"
    data = {
        "email": "test4@gmail.com",
        "firstName": "A",
        "lastName": "Last",
        "gender": "Male",
        "phoneNumber": "8976251654",
        "password1": "password123",
        "password2": "password123",
        "age": 25,
        "city": "Raleigh",
    }
    response = client.post(url, data=data)
    assert response.status_code == 200
    response_data = response.data.decode('utf-8')
    assert "First name must be greater than 1 character." in response.data.decode('utf-8')
    assert "ERROR" in response.data.decode('utf-8')

def test_signup_short_password(app):
    client = app.test_client()
    url = "/sign-up"
    data = {
        "email": "test5@gmail.com",
        "firstName": "First",
        "lastName": "Last",
        "gender": "Male",
        "phoneNumber": "5677189794",
        "password1": "short",
        "password2": "short",
        "age": 25,
        "city": "Raleigh",
    }
    response = client.post(url, data=data)
    assert response.status_code == 200
    response_data = response.data.decode('utf-8')
    assert "Password must be at least 7 characters." in response.data.decode('utf-8')
    assert "ERROR" in response.data.decode('utf-8')

def test_signup_invalid_age_below_18(app):

    client = app.test_client()
    url = "/sign-up"
    data = {
        "email": "test6@gmail.com",
        "firstName": "First",
        "lastName": "Last",
        "gender": "Male",
        "phoneNumber": "87777888777",
        "password1": "password123",
        "password2": "password123",
        "age": 15,  # Invalid age
        "city": "Raleigh",
    }
    response = client.post(url, data=data)
    assert response.status_code == 200
    response_data = response.data.decode('utf-8')
    assert "Please enter a valid age" in response.data.decode('utf-8')
    assert "ERROR" in response.data.decode('utf-8')

def test_signup_invalid_age_above_90(app):

    client = app.test_client()
    url = "/sign-up"
    data = {
        "email": "test7asaas@gmail.com",
        "firstName": "First21",
        "lastName": "Last21",
        "gender": "Female",
        "phoneNumber": "95778268777",
        "password1": "pasword123",
        "password2": "pasword123",
        "age": 99,  # Invalid age
        "city": "Raleigh",
    }
    response = client.post(url, data=data)
    assert response.status_code == 200
    response_data = response.data.decode('utf-8')
    assert "Please enter a valid age" in response.data.decode('utf-8')
    assert "ERROR" in response.data.decode('utf-8')