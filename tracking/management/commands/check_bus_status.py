from django.core.management.base import BaseCommand
from django.utils import timezone
from tracking.models import Student, Route
from tracking.utils import send_notification_email  # your email sending function

# class Command(BaseCommand):
#     help = 'Check bus distance and send notifications to students'

#     def handle(self, *args, **kwargs):
#         now = timezone.now()
        
#         # Dummy example: Loop through students
#         students = Student.objects.all()

#         for student in students:
#             route = student.route
#             if not route:
#                 continue  # No route, skip

#             # Here you should calculate bus distance for the student's stop
#             # (Replace this dummy distance with your real distance logic)
#             distance_km = 1.5  # <-- Assume you fetch distance from ESP32 update

#             # Example logic:
#             if distance_km <= 2:  # Around 10 minutes away
#                 send_notification_email(
#                     subject="Bus Arriving Soon 🚍",
#                     message=f"Hello {student.name}, your bus is about 10 minutes away from your stop {student.stop_name}.",
#                     recipient_email=student.email
#                 )
#             elif distance_km > 5:  # Assume bus is delayed
#                 send_notification_email(
#                     subject="Bus Delayed ⌛",
#                     message=f"Hello {student.name}, your bus seems delayed. Please stay updated.",
#                     recipient_email=student.email
#                 )

#         self.stdout.write(self.style.SUCCESS('Checked bus status and sent notifications.'))


from django.core.management.base import BaseCommand
from django.utils import timezone
from geopy.distance import geodesic  # You can use geopy for distance calculations
from tracking.models import Student  # Make sure this is the correct import for your Student model
from tracking.utils import send_notification_email  # Your email function

class Command(BaseCommand):
    help = 'Check bus distance and send notifications to students'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        
        # Loop through all students
        students = Student.objects.all()

        for student in students:
            route = student.route
            if not route:
                continue  # Skip if the student doesn't have a route assigned

            # Get the student's stop location (latitude and longitude)
            student_stop_location = (student.stop_latitude, student.stop_longitude)

            # Here, fetch the bus's current location (from your GPS data)
            # Example: Fetch the most recent GPS data from the bus (e.g., from the database or API)
            # For demonstration, let's assume bus_latitude and bus_longitude are fetched from somewhere
            bus_location = (route.bus_latitude, route.bus_longitude)  # You should have a method to get bus's current location

            # Calculate the distance between the bus and the student's stop using geopy's geodesic method
            distance_km = geodesic(student_stop_location, bus_location).kilometers

            # Example logic for notifications based on distance
            if distance_km <= 2:  # Around 10 minutes away
                send_notification_email(
                    subject="Bus Arriving Soon 🚍",
                    message=f"Hello {student.name}, your bus is about 10 minutes away from your stop {student.stop_name}.",
                    recipient_email=student.email
                )
            elif distance_km > 5:  # Assume bus is delayed
                send_notification_email(
                    subject="Bus Delayed ⌛",
                    message=f"Hello {student.name}, your bus seems delayed. Please stay updated.",
                    recipient_email=student.email
                )

        self.stdout.write(self.style.SUCCESS('Checked bus status and sent notifications.'))

# class Command(BaseCommand):
#     help = 'Check bus distance and send notifications to students'

#     def handle(self, *args, **kwargs):
#         now = timezone.now()
        
#         # Simulating a student with manually set location
#         students = [
#             {
#                 "name": "Komalpreet Kaur",
#                 "email": "komalpreet9113@gmail.com",
#                 "stop_latitude": 77.00000,  # Example: latitude for student's stop
#                 "stop_longitude": 70.00000,  # Example: longitude for student's stop
#                 "route": "3",  # You can link this to a route in your database
#             }
#         ]

#         for student in students:
#             route = student.get('route')  # Get the student's route
#             if not route:
#                 continue  # Skip if no route is assigned

#             # Get the student's stop location (latitude and longitude)
#             student_stop_location = (student["stop_latitude"], student["stop_longitude"])

#             # For simulation: hardcoding bus location
#             bus_location = (70.0000, 77.0150)  # Simulate bus at a specific location (e.g., in Delhi)

#             # Calculate the distance between the bus and the student's stop using geopy's geodesic method
#             distance_km = geodesic(student_stop_location, bus_location).kilometers

#             # Example logic for notifications based on distance
#             if distance_km <= 2:  # Around 10 minutes away
#                 print(f"Bus Arriving Soon: {student['name']} - {distance_km} km away.")
#                 # Replace print with the send_notification_email() function for real emails
#             elif distance_km > 5:  # Assume bus is delayed
#                 print(f"Bus Delayed: {student['name']} - {distance_km} km away.")
#                 # Replace print with the send_notification_email() function for real emails

#         self.stdout.write(self.style.SUCCESS('Checked bus status and sent notifications.'))
