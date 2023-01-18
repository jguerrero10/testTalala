from django.contrib.auth.models import User
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

    def __str__(self):
        return f'Officer: {self.user.first_name} {self.user.last_name}'


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
    gender = models.ForeignKey(Gender, on_delete=models.RESTRICT, null=True, blank=True)
    hair = models.CharField(max_length=25, blank=True)
    eyes = models.CharField(max_length=25, blank=True)
    height = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=180, blank=True)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return self.fullname


class VehicleType(models.Model):
    vin = models.CharField(max_length=12)
    color = models.CharField(max_length=30)
    make = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()
    model_vehicle = models.CharField(max_length=180)

    def __str__(self):
        return f'Vin: {self.vin}'


class Citation(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.RESTRICT)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.RESTRICT)
    violation_datetime = models.DateTimeField()
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
        return f'{self.id} - Citation | {self.passenger}'


class Violation(models.Model):
    citation = models.ForeignKey(Citation, on_delete=models.RESTRICT, related_name='citation_violation')
    description = models.CharField(max_length=185)

    def __str__(self):
        return f'Citation - {self.description}'
