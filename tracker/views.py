from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.utils.timezone import utc   
import datetime

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
        a=3 
        b=100
        tdelta=datetime.timedelta(days=45)
        # data['expired'] = data['created'] + tdelta
        # print(data['created'])
        # print(data['expired'])
        print(tdelta)
        bmi = float(str(round(float(data['weight']) / (float(data['height'])/100)**2,2)))
        data['bmi'] = bmi
        if(float(data['bmi'])<18.5):
            data['bmitext'] = 'You are underweight!'
        elif(float(data['bmi'])>=18.5 and float(data['bmi'])<25):
            data['bmitext'] = 'You are in healthy weight range!'
        elif(float(data['bmi'])>=255 and float(data['bmi'])<30):
            data['bmitext'] = 'You are overweight!'
        else:
            data['bmitext'] = 'You are obese!'

        if(float(data['creatinine'])<a):
            data['creatininetext'] = 'Creatinine levels are low!'
        elif(float(data['creatinine'])>=a and float(data['creatinine'])<=b):
            data['creatininetext'] = 'Creatinine levels are okay!'
        else:
            data['creatininetext'] = 'Creatinine levels are high!'

        if(float(data['bloodsugar'])<a):
            data['bloodsugartext'] = 'Bloodsugar levels are low!'
        elif(float(data['bloodsugar'])>=a and float(data['bloodsugar'])<=b):
            data['bloodsugartext'] = 'Bloodsugar levels are okay!'
        else:
            data['bloodsugartext'] = 'Bloodsugar levels are high!'

        if(float(data['cholesterol'])<a):
            data['cholesteroltext'] = 'Cholesterol levels are low!'
        elif(float(data['cholesterol'])>=a and float(data['creatinine'])<=b):
            data['cholesteroltext'] = 'Cholesterol levels are okay!'
        else:
            data['cholesteroltext'] = 'Cholesterol levels are high!'

        if(float(data['sysbp'])<a and float(data['diabp'])<a):
            data['bptext'] = 'Blood pressure levels are low!'
        elif(float(data['sysbp'])>=a and float(data['sysbp'])<=b and float(data['diabp'])>=a and float(data['diabp'])<=b):
            data['bptext'] = 'Blood pressure levels are okay!'
        else:
            data['bptext'] = 'Blood pressure levels are high!'

        serializer = ScoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

