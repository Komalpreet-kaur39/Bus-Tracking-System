from datetime import timedelta

from django.test import TestCase
from django.test.client import RequestFactory
from django.utils import timezone

from tracking.models import Bus, BusLocation, Driver, Route, Student
from tracking.views.student_dashboard import student_dashboard


class StudentDashboardViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.route = Route.objects.create(
            name="Route A",
            stops=["Stop 1", "Stop 2"],
            timings=["8:00", "8:20"],
            stops_latitudes=[31.5, 31.6],
            stops_longitudes=[74.3, 74.4],
        )
        self.student = Student.objects.create(
            name="Alice",
            email="alice@example.com",
            password="secret",
            route=self.route,
            stop_name="Stop 1",
        )

    def test_dashboard_hides_timing_details_when_bus_info_is_unavailable(self):
        driver = Driver.objects.create(name="Sam", contact_number="12345")
        bus = Bus.objects.create(bus_number="B100", capacity=40, route=self.route, driver=driver)

        session = self.client.session
        session["student_id"] = self.student.id
        session.save()

        request = self.factory.get("/student/dashboard/")
        request.session = session

        response = student_dashboard(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bus B100")
        self.assertNotContains(response, "ETA:")
        self.assertNotContains(response, "Next Stop:")

    def test_dashboard_hides_timing_details_when_bus_has_stale_location(self):
        driver = Driver.objects.create(name="Sam", contact_number="12345")
        bus = Bus.objects.create(bus_number="B200", capacity=40, route=self.route, driver=driver)
        stale_location = BusLocation.objects.create(
            bus=bus,
            latitude=31.5,
            longitude=74.3,
        )
        stale_location.timestamp = timezone.now() - timedelta(minutes=31)
        stale_location.save(update_fields=["timestamp"])

        session = self.client.session
        session["student_id"] = self.student.id
        session.save()

        request = self.factory.get("/student/dashboard/")
        request.session = session

        response = student_dashboard(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bus B200")
        self.assertNotContains(response, "ETA:")
        self.assertNotContains(response, "Next Stop:")
