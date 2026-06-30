# from django.shortcuts import render
# from tracking.models import Bus, Driver, Route

# def search_stops(request):
#     search_query = request.GET.get('search', '').lower()  # Get search query

#     # Query buses based on the stop names
#     buses = Bus.objects.select_related('driver', 'route').all()

#     if search_query:
#         # Filter buses based on the stop names in the route's stops
#         buses = buses.filter(route__stops__icontains=search_query)

#     return render(request, 'search_results.html', {
#         'buses': buses,
#         'search_query': search_query
#     })


# from django.shortcuts import render
# from tracking.models import Bus, Driver, Route

# def search_stops(request):
#     print("Search function called")  #
#     search_query = request.GET.get('search', '').lower()  # Get search query

#     # Query buses based on the stop names
#     buses = Bus.objects.select_related('driver', 'route').all()

#     if search_query:
#         buses = buses.filter(route__stops__icontains=search_query)

#     # Debugging: print out stops and timings to check if they are being paired correctly
#     for bus in buses:
#         print(f"Bus: {bus.bus_number}")
#     # Check the raw data for stops and timings in the route
#         print(f"Route stops: {bus.route.stops}")
#         print(f"Route timings: {bus.route.timings}")
#         print(f"Route stops latitudes: {bus.route.stops_latitudes}")
#         print(f"Route stops longitudes: {bus.route.stops_longitudes}")
    
#         for stop, timing, lat, lng in bus.route.get_stops_with_timings():
#             print(f"Stop: {stop}, Timing: {timing}, Latitude: {lat}, Longitude: {lng}")
#             print(f"Route stops: {bus.route.stops}")
#             print(f"Route timings: {bus.route.timings}")
 
#     return render(request, 'search_results.html', {
#         'buses': buses,
#         'search_query': search_query
#     })


# from django.shortcuts import render
# from tracking.models import Bus, Route, BusLocation

# def search_stop_results(request):
#     stop_name = request.GET.get('stop_name')
#     results = []

#     if stop_name:
#         # Find all buses whose route contains this stop
#         buses = Bus.objects.filter(route__stops__icontains=stop_name).select_related('route', 'driver')

#         for bus in buses:
#             route = bus.route
#             stops = route.stops  # assuming this is a list or comma-separated string
#             # find index of stop
#             stops_list = [s.strip() for s in stops.split(',')] if isinstance(stops, str) else stops

#             if stop_name in stops_list:
#                 index = stops_list.index(stop_name)
#                 # You can calculate ETA here based on bus location if needed
#                 # For now, just add basic info

#                 results.append({
#                     'bus_number': bus.bus_number,
#                     'route_name': route.name if hasattr(route, 'name') else f'Route {route.id}',
#                     'stop_name': stop_name,
#                     # ETA/time can be calculated or left blank here for now
#                 })

#     context = {
#         'results': results,
#         'query': stop_name,
#     }
#     return render(request, 'student_search_results.html', context)



# from django.shortcuts import render
# from tracking.models import Bus

# def search_stop_results(request):
#     stop_name = request.GET.get('stop_name', '').strip()
#     results = []

#     if stop_name:
#         buses = Bus.objects.filter(route__stops__icontains=stop_name).select_related('route', 'driver')

#         for bus in buses:
#             route = bus.route
#             stops_with_info = route.get_stops_with_timings()  # [(stop, time, lat, lon), ...]

#             for stop, timing, lat, lon in stops_with_info:
#                 if stop.lower() == stop_name.lower():
#                     results.append({
#                         'bus_number': bus.bus_number,
#                         'route_name': route.name,
#                         'stop_name': stop,
#                         'scheduled_time': timing,
#                     })
#                     break  # since we found the stop in this route, no need to look further

#     context = {
#         'results': results,
#         'query': stop_name,
#     }
#     return render(request, 'student_search_results.html', context)
from django.shortcuts import render
from tracking.models import Bus

def search_stop_results(request):
    stop_name = request.GET.get('stop_name', '').strip()
    results = []

    if stop_name:
        buses = Bus.objects.filter(route__stops__icontains=stop_name).select_related('route', 'driver')

        for bus in buses:
            route = bus.route
            stops_with_info = route.get_stops_with_timings()

            for stop, timing, lat, lon in stops_with_info:
                print(f"Checking stop: {stop} vs {stop_name}")  # Debug
                if stop.lower() == stop_name.lower():
                    print(f"Matched! Stop: {stop}, Time: {timing}")  # Debug
                    results.append({
                        'bus_number': bus.bus_number,
                        'route_name': route.name,
                        'stop_name': stop,
                        'scheduled_time': timing,
                    })
                    break

    context = {
        'results': results,
        'query': stop_name,
    }
    return render(request, 'student_search_results.html', context)
