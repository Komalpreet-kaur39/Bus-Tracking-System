from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from tracking.models import Student,Route
import json
# from tracking.views.admin_dashboard import manage_route

class StudentSignup(View):
    def get(self, request):
        routes = Route.objects.all()
        # stops = Stop.objects.all()
        # return render(request, "student_signup.html", {"routes": routes})
        # all_stops = set()
    
        # for route in routes:
        #     stops = route.stops if isinstance(route.stops, list) else []
        #     all_stops.update(stops)

        # return render(request, "student_signup.html", {'routes': routes, 'stops': sorted(all_stops)})
        # return render(request, "student_signup.html")
        route_stop_map = {
                route.id: route.stops if isinstance(route.stops, list) else []
                for route in routes
        }
    
        return render(request, "student_signup.html", {
            'routes': routes,
            'route_stop_map': json.dumps(route_stop_map)  # Pass to JS
        }) 
    def post(self, request):
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        route_id = request.POST.get("route")
        stop_name = request.POST.get("stop_name")

        # Ensure routes and mapping are available when re-rendering on errors
        routes = Route.objects.all()
        route_stop_map = {
            route.id: route.stops if isinstance(route.stops, list) else []
            for route in routes
        }
        # Validation
        if not name or not email or not password or not route_id or not stop_name:
            messages.error(request, "All fields are required!")
            return render(request, "student_signup.html", {
                'routes': routes,
                'route_stop_map': json.dumps(route_stop_map)
            })

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, "student_signup.html", {
                'routes': routes,
                'route_stop_map': json.dumps(route_stop_map)
            })

        if Student.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered!")
            return render(request, "student_signup.html", {
                'routes': routes,
                'route_stop_map': json.dumps(route_stop_map)
            })
        
        # Get route and stop
        # try:
        route = Route.objects.get(id=route_id)
        # except Route.DoesNotExist:
            # messages.error(request, "Selected route is invalid!")
            # return render(request, "student_signup.html")

        # Save student
        student = Student(name=name, email=email, password=make_password(password),route=route,
        stop_name=stop_name)
        student.save()
        messages.success(request, "Signup successful! Please login.")
        return redirect("student_login")


class StudentLogin(View):
    def get(self, request):
        return render(request, "student_login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")

        student = Student.objects.filter(email=email).first()
        if student:
            if check_password(password, student.password):
                request.session["student_id"] = student.id
                return redirect("student_dashboard")
            else:
                messages.error(request, "Invalid password!")
        else:
            messages.error(request, "Student account does not exist!")

        return render(request, "student_login.html")


def student_logout(request):
    request.session.flush()
    return redirect("student_login")
