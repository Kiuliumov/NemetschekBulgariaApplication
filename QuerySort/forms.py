from django import forms
from QuerySort.models import Event


class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = '__all__'

        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'flatpickr',
                'placeholder': 'Избери дата',
                'type': 'date'
            }),
        }

        labels = {
            'name': 'Име на събитието',
            'town': 'Място на събитието',
            'date': 'Дата',
            'type': 'Тип на събитието',
            'lectors': 'Лектори',
        }