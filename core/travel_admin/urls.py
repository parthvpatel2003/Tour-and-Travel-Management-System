from django.urls import path
from . import views

app_name = "travel_admin"

urlpatterns = [
    path('', views.admin_dashboard_view, name='home'),
    path('admin-dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('package-type/', views.package_type_view, name='package_type'),
    path('edit-package-type/<int:id>/', views.edit_package_type, name='edit_package_type'),
    path('delete-package-type/<int:id>/', views.delete_package_type, name='delete_package_type'),
    path('plan-management/',views.plan_management_view, name='plan_management'),
    path('edit-plan-management/<int:id>/',views.edit_plan_management,name='edit_plan_management'),
    path('delete-plan-management/<int:id>/', views.delete_plan_management, name='delete_plan_management'),
    path('destination/',views.destination_view, name='destination'),
    path('edit-destination/<int:id>/', views.edit_destination, name='edit_destination'),
    path('delete-destination/<int:id>/', views.delete_destination, name='delete_destination'),
    path('userdetails/', views.userdetails_view, name='userdetails'),
    path('edit-userdetails/<str:id>/', views.edit_userdetails, name='edit_userdetails'),
    path('delete-userdetails/<str:id>/', views.delete_userdetails, name='delete_userdetails'),
    path('inquirydetails/', views.inquirydetails_view, name='inquirydetails'),
    path('edit-inquirydetails/<str:id>/', views.edit_inquirydetails, name='edit_inquirydetails'),
    path('delete-inquirydetails/<str:id>/', views.delete_inquirydetails, name='delete_inquirydetails'),
    path('role_master/', views.role_master_view, name='role_master'),
    path('edit-role_master/<str:id>', views.edit_role_master, name='edit_role_master'),
    path('delete-role_master/<str:id>', views.delete_role_master, name='delete_role_master'),
    path("login/", views.admin_login, name="admin_login"),
    path("logout/", views.admin_logout, name="admin_logout"),
]