# Generated by Django 4.0.3 on 2022-03-10 19:43

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('date_of_appointment', models.DateTimeField()),
                ('date_of_set_appointment', models.DateTimeField()),
                ('age', models.PositiveIntegerField()),
                ('scolarship', models.BooleanField()),
                ('hipertension', models.BooleanField()),
                ('diabetes', models.BooleanField()),
                ('alcoholism', models.BooleanField()),
                ('sms_received', models.BooleanField()),
                ('handicap', models.IntegerField(choices=[(0, 'first'), (1, 'second'), (2, 'third'), (3, 'fourth'), (4, 'fifth')], default=0)),
                ('num_app_missed', models.DecimalField(decimal_places=0, max_digits=3, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))])),
            ],
        ),
    ]