from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from QuerySort import forms
from QuerySort.forms import EventFilterOrderForm
from QuerySort.models import Event


# Create your views here.
def index(request):

    form = EventFilterOrderForm(request.GET or None)
    events = Event.objects.all()

    if form.is_valid():
        town = form.cleaned_data.get('town')
        type_ = form.cleaned_data.get('type')
        date_from = form.cleaned_data.get('date_from')
        date_to = form.cleaned_data.get('date_to')
        order_by = form.cleaned_data.get('order_by')

        if town:
            events = events.filter(town__icontains=town)
        if type_:
            events = events.filter(type=type_)
        if date_from:
            events = events.filter(date__gte=date_from)
        if date_to:
            events = events.filter(date__lte=date_to)

        if order_by:
            ordering = order_by.split(',')
            events = events.order_by(*ordering)
        else:
            events = events.order_by('date')
    else:
        events = events.order_by('date')

    paginator = Paginator(events, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    querydict = request.GET.copy()
    if 'page' in querydict:
        querydict.pop('page')
    querystring = querydict.urlencode()

    return render(request, 'index.html', {
        'form': form,
        'page_obj': page_obj,
        'querystring': querystring,
    })

def new_data(request):
    form = forms.EventForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, template_name='new-data.html', context={'form': form})


def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('index')