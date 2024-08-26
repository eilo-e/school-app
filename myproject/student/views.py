from django.shortcuts import render
from student.models import Student,Homework,Jozve
# Create your views here.

def StudentListView(request):
    students = Student.objects.all()
    context = {
        'studentlist' : students

    }
    return render(request,"student/studentlist.html",context=context)


def HomeworkListView(request):
    homeworks = Homework.objects.all()
    context = {
        "homeworklist":homeworks

    }
    return render(request,"student/homeworklist.html",context)


def JozveListView(request):
    jozveha = Jozve.objects.all()
    context = {
        "jozvelist":jozveha

    }
    return render(request,"student/jozvelist.html",context=context)

