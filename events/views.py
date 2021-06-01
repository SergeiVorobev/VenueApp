from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm, CreateUser
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
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

@login_required(login_url='login')
def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/list_event.html', {
                      "event_list": event_list,
                  })

@login_required(login_url='login')
def all_venues(request):
    venues_list = Venue.objects.all()
    return render(request, 'events/list_venue.html', {
                      "venue_list": venues_list,
                  })

@login_required(login_url='login')
def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/venue_show.html', {
                      "venue": venue,
                  })

@login_required(login_url='login')
def show_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'events/event_show.html', {
                      "event": event,
                  })

@login_required(login_url='login')
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

    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted, })

@login_required(login_url='login')
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

@login_required(login_url='login')
def search_venues(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venues.html', {'searched': searched, 'venues': venues})
    else:
        return render(request, 'events/search_venues.html', {})

@login_required(login_url='login')
def search_events(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        events = Event.objects.filter(name__contains=searched)
        return render(request, 'events/search_events.html', {'searched': searched, 'events': events})
    else:
        return render(request, 'events/search_events.html', {})

@login_required(login_url='login')
def edit_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('show-venue', venue_id)

    return render(request, 'events/edit_venue.html', {'venue': venue,'form': form})

@login_required(login_url='login')
def edit_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('show-event', event_id)

    return render(request, 'events/edit_event.html', {'event': event,'form': form})

@login_required(login_url='login')
def del_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')

@login_required(login_url='login')
def del_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')

def registration(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUser()

        if request.method=='POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'events/registration.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, password=password, username=username)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is not correct')

        context = {}
        return render(request, 'events/login.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def venue_to_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'

    # Designate the Model
    venues =  Venue.objects.all()
    lines = []
    for venue in venues:
        lines.append(f'Name: {venue.name}\nAddress: {venue.address}\nPost Code: {venue.post_code}\nContact phone: {venue.phone}\n'
                     f'WebSite: {venue.web}\nEmail: {venue.email}\nDescription: {venue.ven_description}\nRating: {venue.booking_rates}\n'
                     f'Open hours: {venue.from_hour} - {venue.to_hour}\nSquare(m^2): {venue.flour_size}\n\n')

    # Write to text file
    response.writelines(lines)
    return response

@login_required(login_url='login')
def events_to_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=events.txt'

    # Designate the Model
    events =  Event.objects.all()
    lines = []
    for event in events:
        lines.append(f'Name: {event.name}\nDate: {event.event_date}\nStart Time: {event.start_time}\nEnd Time: {event.end_time}\n'
                     f'Manager: {event.manager}\nContact Phone: {event.man_phone}\nDescription: {event.eve_description}\n'
                     f'Venue: {event.venue}\nAtendees: {event.attendees}\n\n')

    # Write to text file
    response.writelines(lines)
    return response

