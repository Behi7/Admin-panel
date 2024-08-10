from django.db import models

class Employees(models.Model):
    l_name = models.CharField(max_length=255)
    f_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    age = models.IntegerField()
    work = models.CharField(max_length=255)


class Attendance(models.Model):
    visit_time = models.DateTimeField(auto_now_add=True)
    employ = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True)


class Imageuser(models.Model):
    img = models.ImageField(blank=True, null=True)