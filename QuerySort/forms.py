from django import forms
from QuerySort.models import Event


class EventForm(forms.ModelForm):
    lectors = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': 'text-field'
        }),
        label='Лектори'
    )

    class Meta:
        model = Event
        fields = '__all__'

        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'flatpickr',
                'placeholder': 'Избери дата',
                'type': 'date'
            }),
            'type': forms.Select(attrs={
                'class': 'select-field'
            }),
        }

        labels = {
            'name': 'Име на събитието',
            'town': 'Място на събитието',
            'date': 'Дата',
            'type': 'Тип на събитието',
        }

        def clean_lectors(self):
            data = self.cleaned_data.get('lectors')
            if not data or data.strip() == '':
                return 'Няма лектори.'
            return data

from django import forms

class EventFilterOrderForm(forms.Form):
    ORDER_CHOICES = [
        ('date', 'Дата'),
        ('name', 'Име'),
        ('town', 'Град'),
        ('type', 'Тип'),
        ('name,date', 'Име, Дата'),
        ('date,name', 'Дата, Име'),
        ('town,name', 'Град, Име'),
        ('name,town', 'Име, Град'),
        ('date,town', 'Дата, Град'),
        ('town,date', 'Град, Дата'),
        ('type,name', 'Тип, Име'),
        ('name,type', 'Име, Тип'),
        ('type,date', 'Тип, Дата'),
        ('date,type', 'Дата, Тип'),
        ('type,town', 'Тип, Град'),
        ('town,type', 'Град, Тип'),
    ]

    order_by = forms.ChoiceField(
        choices=ORDER_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'order-select'}),
        label='Подреди по:'
    )
    town = forms.CharField(required=False, label='Място')
    type = forms.ChoiceField(
        choices=[('', 'Всички')] + [(t, t) for t in ['Конференция', 'Семинар', 'Уъркшоп', 'Друго']],
        required=False,
        label='Тип'
    )
    date_from = forms.DateField(required=False, label='От дата', widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(required=False, label='До дата', widget=forms.DateInput(attrs={'type': 'date'}))
