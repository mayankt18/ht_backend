from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

# Create your views here.
@api_view(['GET', 'POST'])
def healthScore_detail(request):
    # try:
    # healthScore = HealthScore.objects.get(pk=pk)
    # except HealthScore.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        healthScore = HealthScore.objects.all()
        serializer = ScoreSerializer(healthScore, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ScoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

