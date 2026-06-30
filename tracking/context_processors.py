from django.conf import settings


def site_settings(request):
    return {
        "GOOGLE_MAPS_API_KEY": getattr(settings, "GOOGLE_MAPS_API_KEY", ""),
        "SAVE_LOCATION_URL": getattr(settings, "SAVE_LOCATION_URL", "/save_location/"),
    }
