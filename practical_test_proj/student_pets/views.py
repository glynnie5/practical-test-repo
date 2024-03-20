from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):

    context_dict = {"boldmessage": 'This is bold'}

    return render(request, 'student_pets/index.html', context=context_dict)


def about(request):

    context_dict = {}

    return render(request, 'student_pets/about.html', context=context_dict)
