from django.urls import path
from django.shortcuts import render
from tracking.views.home import home1
from tracking.views.tracking import save_location
from tracking.views.admin_view import AdminLogin, admin_logout
# from tracking.views.admin_view import admin_login, admin_logout
# from tracking.views.admin_dashboard import AdminDashboard
from tracking.views.admin_dashboard import admin_dashboard, manage_buses,manage_routes,manage_drivers,view_bus_list
from tracking.views.student_view import StudentSignup, StudentLogin, student_logout
from tracking.views.search_bus import search_stop_results
from tracking.views.student_dashboard import haversine_distance,student_dashboard
# from tracking.views.api_bus import bus_data_api,notifications_api

urlpatterns = [
    path('', home1, name='home'),
    # Admin URLs
    path("custom-admin/login/", AdminLogin.as_view(), name="admin_login"),
    path("custom-admin/logout/", admin_logout, name="admin_logout"),
    # path("custom-admin/dashboard/", AdminDashboard.as_view(), name="admin_dashboard"),
    
    # path("admin/dashboard/", lambda request: render(request, "admin_dashboard.html"), name="admin_dashboard"),
    path('custom-admin/dashboard/', admin_dashboard, name='admin_dashboard'),
    # path("admin/dashboard/", AdminDashboard.as_view(), name="admin_dashboard"),
    # path('custom-admin/add-bus/', add_bus, name='add_bus'),
    path('custom-admin/buses/', manage_buses, name='manage_buses'),
    path('custom-admin/routes/',manage_routes, name='manage_routes'),
    path('custom-admin/drivers/', manage_drivers, name='manage_drivers'),
    path('custom-admin/buses/bus-list', view_bus_list, name='view_buses'),
    # path('custom-admin/assign-driver/', assign_driver, name='assign_driver'),
    # path('custom-admin/add-route/', add_route, name='add_route'),
    # path('custom-admin/track-buses/', track_buses, name='track_buses'),
    path('save_location/', save_location, name='save_location'),
    # path('student/dashboard/search_bus/', search_stops,name='search_bus'),
    # path('api/buses/', bus_data_api, name='bus_data_api'),
    # path('api/notifications/', notifications_api, name='notifications_api'),
    path('student/dashboard/', student_dashboard, name='student_dashboard'),
    path('student/dashboard/search/', search_stop_results, name='search_stop_results'),


    # Student URLs
    path("student/signup/", StudentSignup.as_view(), name="student_signup"),
    path("student/login/", StudentLogin.as_view(), name="student_login"),
    path("student/logout/", student_logout, name="student_logout"),
    path("student/dashboard/", lambda request: render(request, "student_dashboard.html"), name="student_dashboard"),
]
