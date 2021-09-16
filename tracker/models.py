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
    creatinine = models.IntegerField(choices=TRACKER, default=TRACKER[0][0])
    bloodsugar = models.IntegerField(choices=TRACKER, default=TRACKER[0][0])
    cholesterol = models.IntegerField(choices=TRACKER, default=TRACKER[0][0])
    sysbp = models.IntegerField(choices=TRACKER, default=TRACKER[0][0])
    diabp = models.IntegerField(choices=TRACKER, default=TRACKER[0][0])
    total = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username
