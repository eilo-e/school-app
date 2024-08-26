from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Student(models.Model):
    
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11,validators=[RegexValidator(regex=r'\d{10,14}', message='Enter a valid phone number')],default="09123456789")
    student_code = models.CharField(max_length=10)
    national_code = models.CharField(max_length=10)
    address = models.TextField(max_length=300)
    fathers_name = models.CharField(max_length=30)
    mothers_name = models.CharField(max_length=30)
    fathers_phone = models.CharField(max_length=11,validators=[RegexValidator(regex=r'\d{10,14}', message='Enter a valid phone number')],default="09123456789")
    mothers_phone = models.CharField(max_length=11,validators=[RegexValidator(regex=r'\d{10,14}', message='Enter a valid phone number')],default="09123456789")
    birth_place = models.CharField(max_length=30)
    birth_date = models.DateField()
    irani = 1
    atba = 2
    nationality = (
    (irani , "ایرانی"),
    (atba , "اتباع"), 
    )
    status = models.IntegerField(choices=nationality)

    def __str__(self):
        return "name:{}-------last name:{}-------phone number:{}-------address:{}-------fathers name:{}-------student code:{}".format(self.name,self.last_name,self.phone_number,self.address,self.fathers_name,self.student_code)

class Homework(models.Model):
    name = models.ForeignKey(Student,on_delete=models.CASCADE,max_length=30)
    image = models.ImageField()
    text = models.TextField(max_length=500)

class Jozve(models.Model):
    name = models.ForeignKey(Student,on_delete=models.CASCADE,max_length=30)
    image = models.ImageField()
    text = models.TextField(max_length=500)

