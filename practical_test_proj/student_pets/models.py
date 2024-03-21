from django.db import models


# Create your models here.
class Student(models.Model):
    forename = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    catNum = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)
        self.catNum = self.cat_set.all().count()
        super(Student, self).save(*args, **kwargs)

    @property
    def order_cats(self):
        cats = self.cat_set.all()
        cat_list = []
        for cat in cats:
            cat_list.append(cat.name)
        cat_list.sort()

        return cat_list

    def __str__(self):
        return self.forename


class Cat(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)

    def save(self, *args, **kwargs):
        super(Cat, self).save(*args, **kwargs)
        self.student.save()
        super(Cat, self).save(*args, **kwargs)

    def delete(self):
        super(Cat, self).delete()
        self.student.save()

    def __str__(self):
        return self.name
