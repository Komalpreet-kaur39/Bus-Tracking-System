from datetime import timedelta

from django.shortcuts import render, redirect
from django.utils import timezone

from tracking.models import Student, Bus, BusLocation
from tracking.utils import haversine_distance  # if you placed it in a utils.py

def student_dashboard(request):
    print("student_dashboard view called") 
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')

    student = Student.objects.get(id=student_id)
    bus = Bus.objects.filter(route=student.route).first()
    latest_location = None
    eta = None
    next_stop = None
    show_timing_details = False
    status = "On Time"
    driver = None

    if bus:
        driver = bus.driver
        latest_location = BusLocation.objects.filter(bus=bus).order_by('-timestamp').first()

        if (
            latest_location
            and student.route
            and latest_location.timestamp >= timezone.now() - timedelta(minutes=15)
        ):
            stops = student.route.stops
            lats = student.route.stops_latitudes
            longs = student.route.stops_longitudes

            if student.stop_name in stops:
                index = stops.index(student.stop_name)
                stop_lat = lats[index]
                stop_lon = longs[index]

                distance_km = haversine_distance(
                    latest_location.latitude, latest_location.longitude,
                    stop_lat, stop_lon
                )

                avg_speed_kmh = 30
                eta_min = int((distance_km / avg_speed_kmh) * 60)
                eta = f"{max(eta_min, 1)} min"
                next_stop = student.stop_name
                show_timing_details = True

    context = {
        'student': student,
        'bus': bus,
        'route': student.route,
        'eta': eta,
        'next_stop': next_stop,
        'show_timing_details': show_timing_details,
        'status': status,
        'driver': driver,
    }
    return render(request, 'student_dashboard.html', context)
