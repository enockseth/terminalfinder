from django.contrib.gis import admin
from .models import Operator, Station

admin.site.register(Operator)
admin.site.register(Station, admin.OSMGeoAdmin)