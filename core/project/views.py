import random
from pymongo import MongoClient
from .mongo import users_collection, booking_collection, contact_collection
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required

client = MongoClient("mongodb://localhost:27017/")
db = client["travel_db"]
signup_collection = db["signup"]

def index(request):
    name = request.session.get('user_name')
    return render(request, "project/index.html", {"name": name})

def destination(request):
    return render(request, 'project/destination.html')

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        pin_code = request.POST.get("pin_code")
        mobile_no = request.POST.get("mobile_no")

        users_collection.insert_one({
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "address": address,
            "pin_code": pin_code,
            "mobile_no": mobile_no
        })

        return redirect("login")

    return render(request, "project/signup.html")


    
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = users_collection.find_one({
            "email": email,
            "password": password
        })

        if user:
            request.session["user_email"] = user["email"]
            request.session["user_name"] = user["first_name"]

            return redirect("index")

        else:
            return render(request, "project/login.html", {
                "error": "Login unsuccessful"
            })

    return render(request, "project/login.html")
def contactus(request):
    if request.method  == "POST":
        userid = request.POST.get("userid")
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile_no = request.POST.get("mobile_no")
        message = request.POST.get("message")

        contact_collection.insert_one({
            "userid":userid,
            "name":name,
            "email":email,
            "mobile_no":mobile_no,
            "message":message
        })

    return render(request, 'project/contactus.html')
    
def package(request):
    return render(request, 'project/package.html')

def bookmytrip(request):
    if request.method == "POST":
            data = {
                "userid": request.POST.get('userid'),
                "role": request.POST.get('role'),
                "first_name": request.POST.get("travelNameFirst"),
                "last_name": request.POST.get("travelNameLast"),
                "mobile": request.POST.get("telephone"),
                "city": request.POST.get("city"),
                "state": request.POST.get("state"),
                "zip": request.POST.get("zip"),
                "country": request.POST.get("country"),
                "email": request.POST.get("quoteEmail"),
                "people": request.POST.get("travelers"),
                "from_city": request.POST.get("travelFromCity"),
                "from_state": request.POST.get("travelFromState"),
                "from_country": request.POST.get("travelFromCountry"),
                "to_city": request.POST.get("travelPlaceCity"),
                "to_state": request.POST.get("travelPlaceState"),
                "to_country": request.POST.get("travelPlaceCountry"),
                "start_date": request.POST.get("startdate"),
                "end_date": request.POST.get("enddate"),
                }
                
            booking_collection.insert_one(data)

            return redirect("booked")

    return render(request, "project/bookmytrip.html")


def booked(request):
    return render(request, 'project/booked.html')

def forgotpassword(request):
    if request.method == "POST":
        email = request.POST.get("email")

        user = signup_collection.find_one({"email": email})

        if user:
            # Store email for the next page
            request.session["reset_email"] = email
            return redirect("changepassword")
        else:
            messages.error(request, "Email not registered.")

    return render(request, "project/forgotpassword.html")

def tipsfortravel(request):
    return render(request, "project/tipsfortravel.html")

def changepassword(request):
    email = request.session.get("reset_email")

    if not email:
        return redirect("forgotpassword")

    if request.method == "POST":
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("new_password_retype")

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
        else:
            signup_collection.update_one(
                {"email": email},
                {"$set": {"password": new_password}}
            )

            messages.success(request, "Password changed successfully.")
            request.session.pop("reset_email", None)
            return redirect("login")

    return render(request, "project/changepassword.html")