from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('destination/', views.destination, name='destination'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('contactus/', views.contactus, name='contactus'),
    path('package/', views.package, name='package'),
    path('bookmytrip/', views.bookmytrip, name='bookmytrip'),
    path('booked/', views.booked, name='booked'),
    path('forgot-password/', views.forgotpassword, name='forgotpassword'),
    path("tips-for-travel/", views.tipsfortravel, name="tipsfortravel"),
    path("change-password/", views.changepassword,name="changepassword"),
]