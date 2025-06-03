from django.http import HttpResponse
from django.shortcuts import render, redirect
from QuerySort import forms

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def new_data(request):
    form = forms.EventForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, template_name='new-data.html', context={'form': form})