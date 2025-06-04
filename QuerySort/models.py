from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from datetime import date, timedelta


# Create your models here.

def validate_event_date(value):
    today = date.today()
    max_date = today + timedelta(days=365)
    if value < today:
        raise ValidationError('Date cannot be in the past.')
    if value > max_date:
        raise ValidationError('Date cannot be more than one year from today.')


class Event(models.Model):
    # The RegEx  '^[A-Za-zА-Яа-яЁё0-9 _\-\'&]+$' allows Latin and Cyrillic letters, digits, spaces, special characters and more
    name = models.CharField(max_length=255,
                            null=False,
                            blank=False,
                            validators=[
                                MinLengthValidator(1, message='The event name must be at least 1 characters long.'),
                                RegexValidator('^[A-Za-zА-Яа-яЁё0-9 _\-\'&]+$')
                            ])

    town = models.CharField(max_length=255,
                            null=False,
                            blank=False,
                            validators=[
                                MinLengthValidator(1, message='The town name must be at least 1 characters long.'),
                                RegexValidator('^[A-Za-zА-Яа-яЁё0-9 _\-\'&]+$')
                            ])

    date = models.DateField(
        null=False,
        blank=False,
        validators=[
           validate_event_date
        ]
    )

    type = models.CharField(max_length=255,
                            null=False,
                            blank=False,
                            validators=[
                                MinLengthValidator(5, message='The event type must be at least 5 characters long.'),
                                RegexValidator('^[A-Za-zА-Яа-яЁё0-9 _\-\'&]+$')
                            ],
                            choices=(('Конференция', 'Конференция'), ('Уъркшоп', 'Уъркшоп') , ('Семинар', 'Семинар'), ('Други', 'Други')))

    lectors = models.CharField(max_length=255,
                               default='Няма лектори.')