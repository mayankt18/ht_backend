from django.contrib import admin
from .models import Prescription, HealthScore

admin.site.register(Prescription)
admin.site.register(HealthScore)
