from django import forms
from django.forms import ModelForm
from .models import Venue, Event, EventUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = (
            'name', 'address', 'post_code', 'phone', 'web', 'email', 'booking_rates', 'from_hour',
            'to_hour', 'flour_size', 'ven_description')

        labels = {
            'name': 'Name', 'address': 'Address', 'post_code': 'Post Code', 'phone': 'Phone number', 'web': 'WebSite', 'email': 'Email', 'ven_description': 'Description',
            'booking_rates': 'Ranking', 'from_hour': 'Open Time',
            'to_hour': 'Close Time', 'flour_size': 'Area size (m^2)',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'post_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Code'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number'}),
            'web': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Website (http://...)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', ' placeholder': 'Email'}),
            'ven_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'booking_rates': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ranking'}),
            'from_hour': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Open time'}),
            'to_hour': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Close time'}),
            'flour_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Square size (m^2)'})}

   # Create a event form
class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = (
            'name', 'event_date', 'start_time', 'end_time', 'manager', 'man_phone', 'venue',
            'attendees','eve_description')

        labels = {
            'name': 'Name', 'event_date': 'Date', 'start_time': 'Start Time', 'end_time': 'End Time', 'manager': 'Manager', 'man_phone': 'Contact Phone',
            'eve_description': 'Description', 'venue': 'Venue', 'attendees': 'Attendees',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event name'}),
            'venue': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Venue'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date'}),
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Start time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'End time'}),
            'manager': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Manager'}),
            'man_phone': forms.TextInput(attrs={'class': 'form-control', ' placeholder': 'Manager phone'}),
            'eve_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Atendees'}),
        }



class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
