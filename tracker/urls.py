from django.urls import path, include
from . import views

urlpatterns = [
    path('detail/', views.healthScore_detail),
]