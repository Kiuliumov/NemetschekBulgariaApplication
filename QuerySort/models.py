from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

# Create your models here.

class Event(models.Model):
    # The RegEx allows Latin and Cyrillic letters, digits, spaces, special characters and more
    name = models.CharField(max_length=255,
                            null=False,
                            blank=False,
                            validators=[
                                MinLengthValidator(6, message='The event name must be at least 6 charracers long.'),
                                RegexValidator('^[A-Za-zА-Яа-яЁё0-9 _\-\'&]+$')
                            ])

