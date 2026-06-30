from django.http import JsonResponse
from tracking.models import Student, Route
from django.utils import timezone
from geopy.distance import geodesic

def bus_data_api(request):
    buses_data = []
    routes = Route.objects.all()

    for route in routes:
        # You need a logic to get bus_latitude and bus_longitude for each route
        # Let's assume you store them somewhere in the Route model or related model
        
        # For example, assume bus current location near the first stop
        if route.stops_latitudes and route.stops_longitudes:
            lat = route.stops_latitudes[0]
            lng = route.stops_longitudes[0]
        else:
            lat, lng = None, None

        bus_info = {
            "bus_number": f"{route.id}",  # or any bus number
            "route_name": route.name,
            "status": "on-time",  # you can dynamically calculate status if you want
            "current_stop": route.stops[0] if route.stops else "",
            "eta_minutes": 8,  # Calculate based on distance if you want
            "capacity": "45/60",  # You can make a Bus model if you want real-time
            "lat": lat,
            "lng": lng,
        }
        buses_data.append(bus_info)

    return JsonResponse(buses_data, safe=False)

# def notifications_api(request):
#     # Dummy notifications for now
#     notifications = [
#         {
#             "message": "Bus #205 is delayed by 5 minutes",
#             "details": "Due to traffic on Main Street",
#             "time": "10 min ago"
#         },
#         {
#             "message": "Bus #101 is on time",
#             "details": "Currently at University Station",
#             "time": "30 min ago"
#         },
#         {
#             "message": "Bus #408 canceled today",
#             "details": "Technical issues",
#             "time": "1 hour ago"
#         },
#     ]
#     return JsonResponse(notifications, safe=False)

# ef bus_data_api(request):
#     buses_data = []
#     routes = Route.objects.all()

#     for route in routes:
#         # Simulate bus location with hardcoded lat/lng
#         lat = 70.0000  # Latitude of Delhi (for example)
#         lng = 77.0150  # Longitude of Delhi (for example)

#         bus_info = {
#             "bus_number": f"{route.id}",
#             "route_name": route_name,
#             "status": "on-time",  # You can dynamically calculate status if you want
#             "current_stop": route.stops[0] if route.stops else "",
#             "eta_minutes": 8,  # Calculate based on distance if you want
#             "capacity": "45/60",  # You can make a Bus model if you want real-time
#             "lat": lat,
#             "lng": lng,
#         }
#         buses_data.append(bus_info)

#     return JsonResponse(buses_data, safe=False)

# def notifications_api(request):
#     # Dummy notifications for now
#     notifications = [
#         {
#             "message": "Bus #205 is delayed by 5 minutes",
#             "details": "Due to traffic on Main Street",
#             "time": "10 min ago"
#         },
#         {
#             "message": "Bus #101 is on time",
#             "details": "Currently at University Station",
#             "time": "30 min ago"
#         },
#         {
#             "message": "Bus #408 canceled today",
#             "details": "Technical issues",
#             "time": "1 hour ago"
#         },
#     ]
#     return JsonResponse(notifications, safe=False)
