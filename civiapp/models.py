from datetime import date

from django.contrib.auth.models import User, Group
from django.db import models


class Agency(models.Model):
    name = models.CharField(max_length=180)
    agency_number = models.CharField(max_length=100)
    address = models.CharField(max_length=180)

    def __str__(self):
        return f'{self.name} | {self.agency_number}'


class Officer(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    badge = models.PositiveSmallIntegerField()
    agency = models.ForeignKey(Agency, on_delete=models.RESTRICT)
    rol = models.ForeignKey(Group, on_delete=models.RESTRICT, default=1)

    def __str__(self):
        return f'Officer: {self.user.first_name} {self.user.last_name}'


class Clerk(models.Model):
    user = models.ForeignKey(User, on_delete=models.RESTRICT)
    agency = models.ForeignKey(Agency, on_delete=models.RESTRICT, related_name='clrek_agency')
    rol = models.ForeignKey(Group, on_delete=models.RESTRICT, default=2)

    def __str__(self):
        return f'Clerk: {self.user.first_name} {self.user.last_name}'


class Gender(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Citation(models.Model):
    oln_state_passenger = models.CharField(max_length=20)
    oln_number_passenger = models.CharField(max_length=30)
    class_oln_passenger = models.CharField(max_length=20)
    cdl_passenger = models.BooleanField(default=False)
    fullname_passenger = models.CharField(max_length=180)
    dob_passenger = models.DateField()
    gender_passenger = models.ForeignKey(Gender, on_delete=models.RESTRICT, null=True, blank=True)
    hair_passenger = models.CharField(max_length=25, blank=True)
    eyes_passenger = models.CharField(max_length=25, blank=True)
    height_passenger = models.CharField(max_length=10, blank=True)
    address_passenger = models.CharField(max_length=180, blank=True)
    city_passenger = models.CharField(max_length=30)
    state_passenger = models.CharField(max_length=25)
    phone_passenger = models.CharField(max_length=25)
    email_passenger = models.EmailField()
    vin = models.CharField(max_length=12)
    color = models.CharField(max_length=30)
    make = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    model_vehicle = models.CharField(max_length=180)
    violation_date = models.DateField(default=date.today)
    violation_time = models.TimeField(default='00:00')
    route = models.CharField(max_length=20)
    county = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    factor_crash = models.BooleanField()
    factor_passenger = models.BooleanField()
    factor_spanish_speaker = models.BooleanField()
    factor_in_car_video = models.BooleanField()
    factor_construction_zone = models.BooleanField()
    factor_body_camera = models.BooleanField()
    factor_school_zone = models.BooleanField()
    factor_workers_present = models.BooleanField()
    officer = models.ForeignKey(Officer, on_delete=models.RESTRICT)
    officer_notes = models.TextField()

    def __str__(self):
        return f'{self.id} - Citation | {self.fullname_passenger}'


class Violation(models.Model):
    citation = models.ForeignKey(Citation, on_delete=models.RESTRICT, related_name='citation_violation')
    description = models.CharField(max_length=185)

    def __str__(self):
        return f'Citation - {self.description}'
