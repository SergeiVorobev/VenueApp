from django import forms
from django.forms import ModelForm
from .models import Venue

# Create a venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'post_code', 'phone', 'web', 'email', 'ven_description', 'booking_rates', 'from_hour', 'to_hour', 'flour_size')

        labels = {
            'name': '', 'address': '', 'post_code': '', 'phone': '', 'web': '', 'email': '', 'ven_description': '', 'booking_rates': 'Ranking', 'from_hour': '',
            'to_hour': '', 'flour_size': 'Area size (m^2)',
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
