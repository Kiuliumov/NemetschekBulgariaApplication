from django.http import HttpResponse
from django.shortcuts import render, redirect
from forms import EventForm

# Create your views here.
def index(request):
    return redirect('new-data')
def new_data(request):
    form = EventForm(request.POST or None)
    return render(request, template_name='new-data.html', context={'form': form})