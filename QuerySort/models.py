from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from datetime import date, timedelta


# Create your models here.

class Event(models.Model):
    # The RegEx  '^[A-Za-zА-Яа-яЁё0-9 _\-\'&]+$' allows Latin and Cyrillic letters, digits, spaces, special characters and more

    name = models.CharField(max_length=255,
                            null=False,
                            blank=False,
                            validators=[
                                MinLengthValidator(6, message='The event name must be at least 6 charracers long.'),
                                RegexValidator('^[A-Za-zА-Яа-яЁё0-9 _\-\'&]+$')
                            ])

    town = models.CharField(max_length=255,
                            null=False,
                            blank=False,
                            validators=[
                                MinLengthValidator(6, message='The town name must be at least 6 charracers long.'),
                                RegexValidator('^[A-Za-zА-Яа-яЁё0-9 _\-\'&]+$')
                            ])

    date = models.DateField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(limit_value=date.today),
            MaxValueValidator(limit_value=date.today() + timedelta(days=365))
        ]
    )

