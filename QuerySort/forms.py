from plistlib import Data
from django import forms

from QuerySort.models import Event, Lector


class EventForm(forms.ModelForm):
    new_lectors = forms.CharField(
        required=False,
        help_text="Add lecturer names separated by commas"
    )

    class Meta:
        model = Event
        fields = ['name', 'town', 'date', 'type', 'lectors']

    def save(self, commit=True):
        event = super().save(commit)
        new_lectors_names = self.cleaned_data.get('new_lectors')
        if new_lectors_names:
            names = [name.strip() for name in new_lectors_names.split(',') if name.strip()]
            for name in names:
                lector, created = Lector.objects.get_or_create(name=name)
                event.lectors.add(lector)
        return event