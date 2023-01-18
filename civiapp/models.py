from django.db import models


class Citation(models.Model):
    violation_datetime = models.DateTimeField()
    route = models.CharField(max_length=20)
    county = models.CharField(max_length=80)
    city = models.CharField(max_length=80)

    def __str__(self):
        return ''


class Gender(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Passenger(models.Model):
    oln_state = models.CharField(max_length=20)
    oln_number = models.CharField(max_length=30)
    class_oln = models.CharField(max_length=20)
    cdl = models.BooleanField(default=False)
    fullname = models.CharField(max_length=180)
    dob = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.RESTRICT)
