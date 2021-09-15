from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Prescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prescription_image = CloudinaryField('image')
    date_of_upload = models.DateTimeField(auto_now_add=True)


GENDER_CHOICES = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('OTHERS', 'OTHERS')
)


class HealthScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=7)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
