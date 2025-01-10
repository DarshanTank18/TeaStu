from django.db import models

# Create your models here.

class signup(models.Model):
    userType = models.CharField(max_length=10)
    fnm = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    doj = models.DateField()
    compensation = models.IntegerField(null=True)
    rollNumber = models.IntegerField(null=True)
    password = models.CharField(max_length=100)

class addteacher(models.Model):
    T_name = models.CharField(max_length=100)
    T_mail = models.EmailField(unique=True)
    T_subject = models.CharField(max_length=50)
    T_number = models.BigIntegerField()

class addstudent(models.Model):
    S_name = models.CharField(max_length=100)
    S_mail = models.EmailField(unique=True)
    S_dob = models.DateField()
    S_grade = models.CharField(max_length=50)
    S_number = models.BigIntegerField()
    S_address = models.TextField(max_length=500)

class eventbl(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_location = models.CharField(max_length=200)
    event_image = models.ImageField(upload_to='image/')

class clubtbl(models.Model):
    c_title = models.CharField(max_length=100)
    pere = models.CharField(max_length=1000)

class Booktbl(models.Model):
    B_name = models.CharField(max_length=100)
    B_author = models.CharField(max_length=100)
    B_image = models.ImageField(upload_to='image/books/')