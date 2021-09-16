from rest_framework import serializers
from .models import *

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthScore
        fields = ('user', 'age', 'gender', 'height', 'weight', 'creatinine','bloodsugar','cholesterol','sysbp','diabp')