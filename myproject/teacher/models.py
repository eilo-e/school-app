from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Teacher (models.Model):
    name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, validators=[RegexValidator(regex=r'\d{10,14}', message='Enter a valid phone number')],default="09123456789")
    national_code = models.CharField(max_length=10)
    father_name = models.CharField(max_length=30)
    personnel_code = models.CharField(max_length=8)
    id_number = models.CharField(max_length=4)  #شماره شناسه
    birth_place = models.CharField(max_length=35)
    birth_date = models.DateField()
    study_field = models.CharField(max_length=30)

    diploma = 1
    bachelors = 2
    masters = 3
    certificate = (
    (diploma , "دیپلم"),
    (bachelors , "لیسانس"),
    (masters , "فوق لیسانس")
    )
    status = models.IntegerField(choices=certificate)

    taminejtemaee = 1
    niroohayemosalah = 2
    farhangian = 3
    salamat = 4
    none = 5
    insurance_type = (
    (taminejtemaee , "تامین اجتماعی"),
    (niroohayemosalah , "نیروهای مسلح"),
    (farhangian , "فرهنگیان"),
    (salamat , "سلامت"),
    (none , "هیچکدام"),
    )
    status = models.IntegerField(choices=insurance_type,default=5)

class Homework(models.Model):
    home_work = models.TextField( max_length= 500 )
    image = models.ImageField(null=True,blank=True)

class Amoozesh(models.Model):
    subject = models.CharField(max_length = 30)
    video =  models.FileField()
    caption = models.TextField(max_length=1000)    

class Marks(models.Model):
    science = 1
    math = 2
    religious = 3
    social_studies = 4
    literature = 5
    english = 6
    chemistry = 7
    physics = 8
    exam_subject = (
    (science , "علوم" ),
    (math , " ریاضی" ),
    (religious , "دین و زندگی"),
    (social_studies , "مطالعات اجتماعی"),
    (literature , "ادبیات"),
    (english , "زبان انگلیسی"),
    (chemistry , "شیمی"),
    (physics , "قیزیک"), 
    )
    status = models.IntegerField(choices=exam_subject)
    
    exam_title = models.CharField(max_length=100)
    exam_date = models.DateField()
    mark = models.FloatField()
    feedback = models.TextField(max_length=1000)
    






    