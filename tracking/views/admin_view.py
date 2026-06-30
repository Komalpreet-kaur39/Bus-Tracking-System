from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from tracking.models import AdminUser  # Import your Admin model

class AdminLogin(View):
    def get(self, request):
        return render(request, "admin_login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        admin = AdminUser.objects.filter(email=email).first()
        if admin:
            if check_password(password, admin.password):  # Ensure password is hashed
                request.session["admin_id"] = admin.id
                return redirect("admin_dashboard")
            else:
                messages.error(request, "Invalid password!")
        else:
            messages.error(request, "Admin account does not exist!")

        return render(request, "admin_login.html")


def admin_logout(request):
    request.session.flush()
    return redirect("admin_login")