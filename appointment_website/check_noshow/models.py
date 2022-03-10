from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

# Create your models here.
class Handicapchoices(models.IntegerChoices):
    FIRST = 0, 'first'
    SECOND = 1, 'second'
    THIRD = 2, 'third'
    FOURTH = 3, 'fourth'
    FIFTH = 4, 'fifth'
class Person(models.Model):
    created_at =  models.DateTimeField(auto_now=True)
    date_of_appointment = models.DateTimeField()
    date_of_set_appointment = models.DateTimeField()
    age = models.PositiveIntegerField()
    scolarship = models.BooleanField()
    hipertension = models.BooleanField()
    diabetes = models.BooleanField()
    alcoholism = models.BooleanField()
    sms_received = models.BooleanField()
    handicap = models.IntegerField(default=Handicapchoices.FIRST, choices=Handicapchoices.choices)
    num_app_missed = models.DecimalField(max_digits=3, decimal_places=0, validators=[MinValueValidator(Decimal('0.01'))])

    def __str__(self) -> str:
        return f"{self.created_at}"