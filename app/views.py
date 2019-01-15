from django.shortcuts import render


# Create your views here.

def backend(request):
    return render(request, "base.html")


def student(req):
    student_list = ["小明", "小红", "陈杰", "小五"]

    return render(req, "student.html", locals())
