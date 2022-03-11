from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
import uuid
import datetime


def truncated_uuid4(uuid):
    return str(uuid)[:5]

# Create your models here.
class Handicapchoices(models.IntegerChoices):
    FIRST = 0, 'first'
    SECOND = 1, 'second'
    THIRD = 2, 'third'
    FOURTH = 3, 'fourth'
    FIFTH = 4, 'fifth'
    
class Gender(models.IntegerChoices):
    MAN = 1, 'man'
    WOMAN = 0, 'woman'

class Person(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gender = models.IntegerField(default=Gender.WOMAN, choices=Gender.choices)
    created_at =  models.DateTimeField(auto_now=True)
    date_of_appointment = models.DateTimeField()
    date_of_set_appointment = models.DateTimeField()
    age = models.PositiveIntegerField(validators=[MaxValueValidator(Decimal('102.0'))])
    scolarship = models.BooleanField()
    hipertension = models.BooleanField()
    diabetes = models.BooleanField()
    alcoholism = models.BooleanField()
    sms_received = models.BooleanField()
    handicap = models.IntegerField(default=Handicapchoices.FIRST, choices=Handicapchoices.choices)
    num_app_missed = models.DecimalField(max_digits=3, decimal_places=0, validators=[MinValueValidator(Decimal('-0.01'))])


    def __str__(self) -> str:
        return f"Osoba o skróconym id: {truncated_uuid4(self.id)}, utworzona: {(self.created_at)}"
