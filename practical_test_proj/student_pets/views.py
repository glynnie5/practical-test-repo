from django.shortcuts import render
from django.http import HttpResponse
from student_pets.models import Student, Cat


# Create your views here.
def index(request):

    student_list = Student.objects.order_by('surname')

    context_dict = {}
    context_dict['students'] = student_list

    return render(request, 'student_pets/index.html', context=context_dict)


def about(request):

    cat_list = Cat.objects.order_by('name')

    context_dict = {}
    context_dict['cats'] = cat_list

    return render(request, 'student_pets/about.html', context=context_dict)
