from django.db import models
import json
# Admin Model
class AdminUser(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @staticmethod
    def emailExists(email):
        return AdminUser.objects.filter(email=email).exists()

# # Student Model
# class Student(models.Model):
#     name = models.CharField(max_length=50, default="")
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     profile_pic = models.ImageField(upload_to="upload/students", blank=True)
#     route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True)
#     stop_name = models.CharField(max_length=100, blank=True)  # Match with Route.stops

#     def __str__(self):
#         return self.name

#     @staticmethod
#     def emailExists(email):
#         return Student.objects.filter(email=email).exists()

class Route(models.Model):
    name = models.CharField(max_length=100)
    stops = models.JSONField(default=list)  # ✅ Correct
    timings = models.JSONField(default=list)  # ✅ Correct
    # latitude = models.FloatField(null=True, blank=True)  # Added latitude
    # longitude = models.FloatField(null=True, blank=True)  # Added longitude
    stops_latitudes = models.JSONField(default=list)  # A list of latitudes
    stops_longitudes = models.JSONField(default=list)  # A list of longitudes

    def get_stops_with_timings(self):
        """Pairs stops and timings correctly"""
        stops = self.stops if isinstance(self.stops, list) else json.loads(self.stops)
        timings = self.timings if isinstance(self.timings, list) else json.loads(self.timings)
        latitudes = self.stops_latitudes if isinstance(self.stops_latitudes, list) else json.loads(self.stops_latitudes)
        longitudes = self.stops_longitudes if isinstance(self.stops_longitudes, list) else json.loads(self.stops_longitudes)

        if isinstance(stops, list) and isinstance(timings, list) and isinstance(latitudes, list) and isinstance(longitudes, list):
            return list(zip(stops, timings, latitudes, longitudes))
        return []
        #  if isinstance(stops, list) and isinstance(timings, list):
        #      return list(zip(stops, timings))
        #  return []

# Student Model
class Student(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    # profile_pic = models.ImageField(upload_to="upload/students", blank=True)
    route = models.ForeignKey(Route, on_delete=models.SET_NULL, null=True, blank=True)
    stop_name = models.CharField(max_length=100, blank=True)  # Match with Route.stops

    def __str__(self):
        return self.name

    @staticmethod
    def emailExists(email):
        return Student.objects.filter(email=email).exists()
 
class Driver(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Bus(models.Model):
    bus_number = models.CharField(max_length=10, unique=True)
    capacity = models.IntegerField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.bus_number
        
class BusLocation(models.Model):
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bus.bus_number} - {self.latitude}, {self.longitude}"
