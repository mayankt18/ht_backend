from django.contrib import admin
from .models import Prescription, HealthScore

admin.autodiscover()
admin.site.enable_nav_sidebar = False

admin.site.register(Prescription)
admin.site.register(HealthScore)
