from django.db import models

# Create your models here.
class features(models.Model):
    GENDER = [
        ('male','male'),
        ('female','female'),
    ]
    sex = models.CharField(
        max_length=6,
        choices=GENDER,
    )
    Age = models.IntegerField()
    bmi = models.FloatField(max_length=100)
    children = models.IntegerField()
    SMOKER = [
        ('yes','yes'),
        ('no','no'),
    ]
    smoker = models.CharField(
        max_length=3,
        choices=SMOKER,
    )
    REGION = [
        ('southwest','southwest'),
        ('southeast','southeast'),
        ('northwest','northwest'),
        ('northeast','northeast'),
    ]
    region = models.CharField(
        max_length=9,
        choices=REGION,
    )

class MedicalData(models.Model):
    GENDER = [('male','male'),('female','female')]
    REGION = [('southwest','southwest'),('southeast','southeast'),('northwest','northwest'),('northeast','northeast'),]
    SMOKER = [('yes','yes'),('no','no')]
    
    age = models.IntegerField()
    bmi = models.FloatField()
    children = models.IntegerField()
    gender = models.CharField(choices=GENDER,max_length=10)
    smoker = models.CharField(choices=SMOKER,max_length=5)
    region = models.CharField(choices=REGION,max_length=20)

class LifeData(models.Model):
    CHOISE = [('yes','1'),('no','0')]
    age = models.IntegerField()
    diabetes = models.IntegerField()
    bloodpressure = models.IntegerField()
    transplant = models.IntegerField()
    chronicdisease = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    allergies = models.IntegerField()
    cancer = models.IntegerField()
    surgeries = models.IntegerField()

class CarData(models.Model):
    Year  = models.IntegerField()
    Present_Price = models.FloatField()
    Kms_Driven = models.IntegerField()
    Fuel_Type = models.IntegerField()
    Seller_Type = models.IntegerField()
    Transmission = models.IntegerField()
    Owner = models.IntegerField()