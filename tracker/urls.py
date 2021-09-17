from django.urls import path, include
from . import views

urlpatterns = [
    path('detail/', views.healthscore_detail),
    path('prescription/', views.prescription)
]
