from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from travel_admin.models import PackageType, PlanManagement, Destination, Role_Master
from .forms import PackageTypeForm, PlanManagementForm, DestinationForm, Role_MasterForm
from .models import PackageType, PlanManagement, Destination, UserDetails, InquiryDetails, Role_Master
from pymongo import MongoClient
from bson.objectid import ObjectId
from .decorators import admin_required
from django.contrib import messages

@admin_required
def admin_dashboard_view(request):

    if "admin_id" not in request.session:
        return redirect("travel_admin:admin_login") 


    client = MongoClient("mongodb://localhost:27017/")
    db = client["travel_db"]

    users_collection = db["bookings"]
    inquiry_collection = db["contactus"]
    admin_collection = db["admin"]

    total_users = users_collection.count_documents({})
    customer_count = users_collection.count_documents({"role": "customer"})
    admin_count = admin_collection.count_documents({"role": "admin"})
    inquiry_count = inquiry_collection.count_documents({})

    destination_count = Destination.objects.count()
    plan_count = PlanManagement.objects.count()
    package_count = PackageType.objects.count()

    # Count records from the Admin Role page
    role_count = Role_Master.objects.count()

    context = {
        "total_users": total_users,
        "customer_count": customer_count,
        "admin_count": admin_count,
        "destination_count": destination_count,
        "plan_count": plan_count,
        "package_count": package_count,
        "inquiry_count": inquiry_count,
        "role_count": role_count,
    }

    return render(request, "travel_admin/dashboard.html", context)

@admin_required
def package_type_view(request):

    action = request.GET.get('action','data')

    form = PackageTypeForm()

    package_list = PackageType.objects.all()


    if request.method == "POST":

        form = PackageTypeForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect('travel_admin:package_type')

    return render(request,"travel_admin/packagetype.html",
    {
        "form":form,
        "package_list":package_list,
        "action":action
    })
    
@admin_required    
def delete_package_type(request, id):
    package = get_object_or_404(PackageType, id=id)
    package.delete()
    return redirect("travel_admin:package_type")

@admin_required
def edit_package_type(request,id):

    package = get_object_or_404(PackageType,id=id)


    if request.method=="POST":

        package.destination=request.POST.get("destination")
        package.package_type=request.POST.get("package_type")
        package.plan_management=request.POST.get("plan_management")

        package.save()


        return redirect('/travel-admin/package-type/?action=data')



    return render(request,"travel_admin/packagetype.html",
                  {
                      "package":package,
                      "action":"edit"
                  })

@admin_required
def plan_management_view(request):
    action = request.GET.get('action')

    form = PlanManagementForm()
    plan_list = None

    if request.method == "POST":
        form = PlanManagementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('travel_admin:plan_management')

    if action == "data":
        plan_list = PlanManagement.objects.all()


    return render(request, "travel_admin/planmanagement.html", {
        "form": form,
        "plan_list": plan_list,
        "action": action
    })

@admin_required
def delete_plan_management(request, id):
    plan = get_object_or_404(PlanManagement, id=id)
    plan.delete()
    return redirect('travel_admin:plan_management')

@admin_required
def edit_plan_management(request, id):

    plan = get_object_or_404(PlanManagement, id=id)

    if request.method == "POST":

        plan.plan_name = request.POST.get("plan_name")
        plan.duration = request.POST.get("duration")
        plan.nights_days = request.POST.get("nights_days")
        plan.status = request.POST.get("status")

        plan.save()

        return redirect('/travel-admin/plan-management/?action=data')


    return render(request, "travel_admin/planmanagement.html", {
        "plan": plan,
        "action": "edit"
    })
    
@admin_required
def destination_view(request):
    action = request.GET.get("action")

    if request.method == "POST":
        form = DestinationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/travel-admin/destination/?action=data")
    else:
        form = DestinationForm()

    destination_list = Destination.objects.all() if action == "data" else []

    return render(request, "travel_admin/destination.html", {
        "form": form,
        "destination_list": destination_list,
        "action": action,
    })

@admin_required
def delete_destination(request, id):
    destination = get_object_or_404(Destination, id=id)
    destination.delete()
    return redirect('travel_admin:destination')

@admin_required
def edit_destination(request, id):
    destination = get_object_or_404(Destination, id=id)

    if request.method == "POST":
        form = DestinationForm(request.POST, request.FILES, instance=destination)

        if form.is_valid():
            form.save()
            return redirect('travel_admin:destination')

    else:
        form = DestinationForm(instance=destination)

    destination_list = Destination.objects.all()

    return render(request, "travel_admin/destination.html", {
        "form": form,
        "destination_list": destination_list,
        "action": "edit",
        "destination": destination,
    })
def getElementById(request):
    return render(request, 'travel_admin/destination.html')

@admin_required
def userdetails_view(request):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["travel_db"]
    collection = db["bookings"]

    details_list = list(collection.find())

    # Convert MongoDB _id to string for URL
    for user in details_list:
        user["id"] = str(user["_id"])

    return render(request, "travel_admin/userdetails.html", {
        "details_list": details_list
    })

@admin_required
def edit_userdetails(request, id):

    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client["travel_db"]
    collection = db["bookings"]

    # Get one user by id
    details = collection.find_one({"_id": ObjectId(id)})

    # Update user
    if request.method == "POST":

        collection.update_one(
            {"_id": ObjectId(id)},
            {
                "$set": {
                    "role": request.POST.get("role"),
                    "first_name": request.POST.get("first_name"),
                    "last_name": request.POST.get("last_name"),
                    "mobile": request.POST.get("mobile"),
                    "city": request.POST.get("city"),
                    "state": request.POST.get("state"),
                    "zip": request.POST.get("zip"),
                    "country": request.POST.get("country"),
                    "email": request.POST.get("email"),
                    "people": request.POST.get("people"),
                    "from_city": request.POST.get("from_city"),
                    "from_state": request.POST.get("from_state"),
                    "from_country": request.POST.get("from_country"),
                    "to_city": request.POST.get("to_city"),
                    "to_state": request.POST.get("to_state"),
                    "to_country": request.POST.get("to_country"),
                    "start_date": request.POST.get("start_date"),
                    "end_date": request.POST.get("end_date"),
                }
            }
        )

        return redirect("travel_admin:userdetails")

    # Convert MongoDB ObjectId to string
    details["id"] = str(details["_id"])

    # Show edit form
    return render(
        request,"travel_admin/userdetails.html",
        {
            "details": details,
            "action": "edit",
        }
    )

@admin_required
def delete_userdetails(request, id):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["travel_db"]
    collection = db["bookings"]

    collection.delete_one({"_id": ObjectId(id)}) 

    return redirect('travel_admin:userdetails')

@admin_required
def inquirydetails_view(request):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["travel_db"]
    collection = db["contactus"]  

    details_list = list(collection.find())

    for item in details_list:
        item['id'] = str(item['_id'])
        del item['_id']

    return render(request, "travel_admin/inquirydetails.html", {
        "details_list": details_list
    })

@admin_required
def edit_inquirydetails(request, id):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["travel_db"]
    collection = db["contactus"]

    details = collection.find_one({"_id": ObjectId(id)})

    if details:
        details['id'] = str(details['_id'])
        del details['_id']

    return render(request, "travel_admin/inquirydetails.html", {"details": details})

@admin_required
def delete_inquirydetails(request, id):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["travel_db"]
    collection = db["contactus"]

    collection.delete_one({"_id": ObjectId(id)}) 

    return redirect('travel_admin:inquirydetails')

@admin_required
def role_master_view(request):
    action = request.GET.get('action')

    form = Role_MasterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('travel_admin:role_master')

    role_list = Role_Master.objects.all() if action == "data" else []

    return render(request, "travel_admin/role_master.html", {
        "form": form,
        "role_list": role_list,
        "action": action
    })

@admin_required
def edit_role_master(request, id):
    role = get_object_or_404(Role_Master, id=id)

    form = Role_MasterForm(request.POST or None, instance=role)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('travel_admin:role_master')

    return render(request, 'travel_admin/role_master.html', {
        'form': form,
        'action': 'new'
    })
    
@admin_required
def delete_role_master(request, id):
    role = get_object_or_404(Role_Master, id=id)

    role.delete()
    return redirect('travel_admin:role_master')


def admin_login(request):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["travel_db"]
    admin_collection = db["admin"]

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        admin = admin_collection.find_one({
            "email": email,
            "role": "admin"
        })

        if admin and password == admin["password"]:
            request.session["admin_id"] = str(admin["_id"])
            request.session["admin_name"] = admin["name"]
            return redirect("travel_admin:admin_dashboard")

        messages.error(request, "Invalid Email or Password")

    return render(request, "travel_admin/admin_login.html")
def admin_logout(request):
    request.session.flush()
    return redirect("index")
