   
from django.shortcuts import render, redirect, get_object_or_404
from tracking.models import Bus, Route,Driver
from tracking.forms import BusForm,RouteForm,DriverForm
import json
from django.views.decorators.csrf import csrf_exempt

def admin_dashboard(request):
    # return render(request, 'admin_dashboard.html')
    drivers = Driver.objects.all()
    routes = Route.objects.all()
    buses = Bus.objects.select_related('driver', 'route').all()
    # Check if the search query is provided
    # search_query = request.GET.get('search', '').lower()  # Get the search term
    
    # if search_query:
    #     # Filter buses based on bus_number or driver name or the route's stops
    #     buses = buses.filter(
    #         bus_number__icontains=search_query) | buses.filter(
    #         driver__name__icontains=search_query)

    #     # Filter buses based on the route's stops (JSON field)
    #     buses = buses.filter(route__stops__icontains=search_query)
    # if search_query:
    #     # Filter buses based on the search query in the stop list of each route
    #     buses = buses.filter(route__stops__icontains=search_query)
    
    return render(request, 'admin_dashboard.html', {
        'buses': buses,  
        'drivers': drivers,
        'routes': routes,
        })

@csrf_exempt  # Only for testing; remove in production
def manage_buses(request):
    buses = Bus.objects.select_related('driver', 'route').all()
    drivers = Driver.objects.all()
    routes = Route.objects.all()
    bus = None  # Used when editing an existing bus

    # ✅ Handle Delete Request
    if request.GET.get("delete"):
        bus = get_object_or_404(Bus, id=request.GET.get("delete"))
        bus.delete()
        return redirect("manage_buses")

    if request.method == "POST":
        bus_id = request.POST.get("bus_id")
        bus_number = request.POST.get("bus_number")
        capacity = request.POST.get("capacity")
        driver_id = request.POST.get("driver")
        route_id = request.POST.get("route")

        if not (bus_number and capacity and driver_id and route_id):
            return render(request, 'bus.html', {
                'buses': buses,
                'drivers': drivers,
                'routes': routes,
                'error': "All fields are required!"
            })

        driver = get_object_or_404(Driver, id=driver_id)
        route = get_object_or_404(Route, id=route_id)

        if bus_id:  # Edit existing bus
            bus = get_object_or_404(Bus, id=bus_id)
            bus.bus_number = bus_number
            bus.capacity = capacity
            bus.driver = driver
            bus.route = route
            bus.save()
        else:  # Create new bus
            Bus.objects.create(bus_number=bus_number, capacity=capacity, driver=driver, route=route)

        return redirect('manage_buses')

    return render(request, "bus.html", {
        "buses": buses,
        "drivers": drivers,
        "routes": routes,
    })
def view_bus_list(request):
    buses = Bus.objects.all()
    context = {'buses': buses}
    return render(request, 'view_bus.html', context)

def manage_routes(request):
    routes = Route.objects.all()
    route = None

    # Handle delete in GET request
    if request.GET.get('delete'):
        route = get_object_or_404(Route, id=request.GET.get('delete'))
        route.delete()
        return redirect('manage_routes')

    # Handle edit request
    if request.GET.get('edit'):
        route = get_object_or_404(Route, id=request.GET.get('edit'))

    if request.method == 'POST':
        route_id = request.POST.get('route_id')
        stops = request.POST.getlist('stops')
        timings = request.POST.getlist('timings')
        name = request.POST.get('name')
        latitudes = request.POST.getlist('latitudes')  # Get latitudes from form
        longitudes = request.POST.getlist('longitudes')  # Get longitudes from form

        # Clean and validate data
        stops = [s.strip() for s in stops if s.strip()]
        timings = [t.strip() for t in timings if t.strip()]
        latitudes = [float(lat) for lat in latitudes if lat.strip()]
        longitudes = [float(lon) for lon in longitudes if lon.strip()]

        # Validate that stops, timings, latitudes, and longitudes have the same length
        if len(stops) == len(timings) == len(latitudes) == len(longitudes):
            if route_id:  # Update existing route
                route = get_object_or_404(Route, id=route_id)
                route.name = name
                route.stops = stops
                route.timings = timings
                route.stops_latitudes = latitudes
                route.stops_longitudes = longitudes
                route.save()
            else:  # Create new route
                Route.objects.create(
                    name=name,
                    stops=stops,
                    timings=timings,
                    stops_latitudes=latitudes,
                    stops_longitudes=longitudes,
                )

        return redirect('manage_routes')

    return render(request, 'route.html', {
        'routes': routes,
        'route': route,
    })
def manage_drivers(request):
    drivers = Driver.objects.all()
    driver = None

    # If editing an existing driver
    if request.GET.get('edit'):
        driver = get_object_or_404(Driver, id=request.GET.get('edit'))

    if request.method == 'POST':
        driver_id = request.POST.get('driver_id')
        name = request.POST.get('name')
        contact_number = request.POST.get('contact_number')

        if driver_id:  # Update existing driver
            driver = get_object_or_404(Driver, id=driver_id)
            driver.name = name
            driver.contact_number = contact_number
            driver.save()
        else:  # Create new driver
            Driver.objects.create(name=name, contact_number=contact_number)

        return redirect('manage_drivers')

    # Handle delete request
    if request.GET.get('delete'):
        driver = get_object_or_404(Driver, id=request.GET.get('delete'))
        driver.delete()
        return redirect('manage_drivers')

    return render(request, 'driver.html', {
        'drivers': drivers,
        'driver': driver
    })
