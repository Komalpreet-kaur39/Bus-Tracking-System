from django.contrib import admin
from .models import AdminUser,Student,Driver,Route,Bus,BusLocation
# Register your models here.
admin.site.register(AdminUser)
admin.site.register(Student)
admin.site.register(Driver)
admin.site.register(Route)
admin.site.register(Bus)
admin.site.register(BusLocation)