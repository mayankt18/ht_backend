from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from datetime import datetime, timedelta
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def healthScore_detail(request):
    if request.method == 'GET':
        prescription = Prescription.objects.all()
        serializer = PrescriptionSerializer(prescription, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PrescriptionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', 'POST'])
def healthScore_detail(request):

    if request.method == 'GET':
        healthScore = HealthScore.objects.all()
        serializer = ScoreSerializer(healthScore, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        tdelta = timedelta(days=45)
        data['expired'] = (datetime.now()+tdelta)

        bmi = float(
            str(round(float(data['weight']) / (float(data['height'])/100)**2, 2)))
        data['bmi'] = bmi
        data['bmitext'] = bmicalculator(bmi)
        data['creatininetext'] = creatinine_cal(float(data['creatinine']))
        data['bloodsugartext'] = bloodsugar_cal(float(data['bloodsugar']))
        data['cholesteroltext'] = bloodsugar_cal(float(data['cholesterol']))
        data['bptext'] = bloodsugar_cal(float(data['diabp']),float(data['sysbp']))


        # SENDING A DUMMY EMAIL
        subject = "Hello world"
        message = "this the message of the email"
        email_from = settings.EMAIL_HOST_USER
        recepient_list = ['mayank9903261034@gmail.com']
        send_mail(subject, message, email_from, recepient_list)
        # print("mail sent")

        serializer = ScoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def bmicalculator(bmi):
    if(float(bmi) < 18.5):
        return 'You are underweight!'
    elif(float(bmi) >= 18.5 and float(bmi) < 25):
        return 'You are in healthy weight range!'
    elif(float(bmi) >= 255 and float(bmi) < 30):
        return 'You are overweight!'
    else:
        return 'You are obese!'

def creatinine_cal(cr):
    if(cr < 5):
            return 'Creatinine levels are low!'
    elif(cr >= 5 and cr <= 10):
        return 'Creatinine levels are okay!'
    else:
        return 'Creatinine levels are high!'

def bloodsugar_cal(bs):
    if(bs < 5):
        return 'Bloodsugar levels are low!'
    elif(bs >= 5 and bs <= 10):
        return 'Bloodsugar levels are okay!'
    else:
        return 'Bloodsugar levels are high!'

def cholesterol_cal(cl):
    if(cl < 5):
        return 'Cholesterol levels are low!'
    elif(cl >= 5 and cl <= 10):
        return 'Cholesterol levels are okay!'
    else:
        return 'Cholesterol levels are high!'
        
def bp_cal(sysbp,diabp):
    if(sysbp < 5 and diabp < 5):
        return 'Blood pressure levels are low!'
    elif(sysbp >= 5 and sysbp <= 10 and diabp >= 5 and diabp <= 10):
        return 'Blood pressure levels are okay!'
    else:
        return 'Blood pressure levels are high!'


