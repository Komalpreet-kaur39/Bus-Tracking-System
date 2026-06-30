# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from tracking.models import Bus, BusLocation
# import json

# @csrf_exempt
# def save_location(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)  # Parse JSON data from the request body
#             bus_id = data.get('bus_id')
#             latitude = data.get('latitude')
#             longitude = data.get('longitude')

#             # Ensure that we have all required fields
#             if not all([bus_id, latitude, longitude]):
#                 return JsonResponse({'status': 'Error', 'message': 'Missing required parameters'}, status=400)

#             # Get the bus and save location
#             bus = Bus.objects.get(id=bus_id)
#             location = BusLocation(bus=bus, latitude=latitude, longitude=longitude)
#             location.save()

#             return JsonResponse({'status': 'Location saved!'})
#         except Exception as e:
#             return JsonResponse({'status': 'Error', 'message': str(e)}, status=400)
#     return JsonResponse({'status': 'Invalid request method'}, status=405)


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from tracking.models import Bus, BusLocation
import json

@csrf_exempt
def save_location(request):
    print(">>> save_location view called with", request.method)
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            bus_id = data.get('bus_id')
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            if not all([bus_id, latitude, longitude]):
                return JsonResponse({'status': 'Error', 'message': 'Missing required parameters'}, status=400)

            bus = Bus.objects.get(id=bus_id)
            location = BusLocation(bus=bus, latitude=latitude, longitude=longitude)
            location.save()

            return JsonResponse({'status': 'Location saved!'})
        except Exception as e:
            return JsonResponse({'status': 'Error', 'message': str(e)}, status=400)

    elif request.method == "GET":
        # Fetch latest location for bus 1
        try:
            bus = Bus.objects.get(id=3)
            latest = BusLocation.objects.filter(bus=bus).latest('timestamp')
            return JsonResponse({
                'latitude': latest.latitude,
                'longitude': latest.longitude,
                'timestamp': latest.timestamp
            })
        except BusLocation.DoesNotExist:
            return JsonResponse({'status': 'Error', 'message': 'No location found'}, status=404)

    return JsonResponse({'status': 'Invalid request method'}, status=405)


