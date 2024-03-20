from django.db import models


# Create your models here.
class Student(models.Model):
    forename = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    catNum = models.IntegerField(default=0)

    def __str__(self):
        return self.forename


class Cat(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
