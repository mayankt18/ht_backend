from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import cloudinary


class Prescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prescription_image = CloudinaryField('image')
    date_of_upload = models.DateTimeField(auto_now_add=True)


GENDER_CHOICES = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
    ('OTHERS', 'OTHERS')
)

VLOW = 1
LOW = 2
NORMAL = 3
HIGH = 2
VHIGH = 1
TRACKER = (
    (VLOW, 'Very Low'),
    (LOW, 'Low'),
    (NORMAL, 'Medium'),
    (HIGH, 'High'),
    (VHIGH, 'Very High')
)


class HealthScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=0)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=7)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    bmi = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    bmitext = models.CharField(max_length=50, blank=True, null=True)
    creatinine = models.DecimalField(max_digits=10, decimal_places=2)
    creatininetext = models.CharField(max_length=50, blank=True, null=True)
    bloodsugar = models.DecimalField(max_digits=10, decimal_places=2)
    bloodsugartext = models.CharField(max_length=50, blank=True, null=True)
    cholesterol = models.DecimalField(max_digits=10, decimal_places=2)
    cholesteroltext = models.CharField(max_length=50, blank=True, null=True)
    sysbp = models.DecimalField(max_digits=10, decimal_places=2)
    diabp = models.DecimalField(max_digits=10, decimal_places=2)
    bptext = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    expired = models.DateTimeField(auto_now_add=False, null=True)

    def __str__(self):
        return self.user.username
