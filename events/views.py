from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm, CreateUser
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    # name = "John"
    month = month.capitalize()
    # Convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # create a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)
    # Get current year
    now = datetime.now()
    current_year = now.year
    # Get current time
    time = now.strftime('%I:%M:%S %p')
    return render(request, 'events/home.html', {
                      # "name": name,
                      "year": year,
                      "month": month,
                      "month_number": month_number,
                      "cal": cal,
                      "current_year": current_year,
                      "time": time,
                  })

def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html', {
                      "event_list": event_list,
                  })

def all_venues(request):
    venues_list = Venue.objects.all()
    return render(request, 'events/venue_list.html', {
                      "venue_list": venues_list,
                  })

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html', {
                      "venue": venue,
                  })

def show_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'events/show_event.html', {
                      "event": event,
                  })

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/venues/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})

def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/events/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {'form': form, 'submitted': submitted})

def search_venues(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venues.html', {'searched': searched, 'venues': venues})
    else:
        return render(request, 'events/search_venues.html', {})

def search_events(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        events = Event.objects.filter(name__contains=searched)
        return render(request, 'events/search_events.html', {'searched': searched, 'events': events})
    else:
        return render(request, 'events/search_events.html', {})

def edit_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('show-venue', venue_id)

    return render(request, 'events/edit_venue.html', {'venue': venue,'form': form})

def edit_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('show-event', event_id)

    return render(request, 'events/edit_event.html', {'event': event,'form': form})

def del_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')

def del_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')

def registration(request):
    form = CreateUser()

    if request.method=='POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'events/registration.html', context)

def login(request):
    context = {}
    return render(request, 'events/login.html', context)
