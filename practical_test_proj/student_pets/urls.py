from django.urls import path
from student_pets import views

app_name = 'student_pets'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]
