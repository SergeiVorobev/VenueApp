from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=255)
    address = models.CharField('Address', max_length=255)
    post_code = models.CharField('Post Code', max_length=10)
    phone = models.CharField('Contact Phone', max_length=15, blank=True)
    web = models.URLField('Website Address', blank=True)
    email = models.EmailField('Email', blank=True)
    ven_description = models.TextField(blank=True)
    booking_rates = models.FloatField(verbose_name='Ranking (up to 9.0)', default=1.0, blank=True)
    from_hour = models.TimeField(blank=True)
    to_hour = models.TimeField(blank=True)
    flour_size = models.FloatField(verbose_name='Square (mxm)', default=1.0, blank=True)
    # type = models.CharField('Type of Venue', max_length=255)
    def __str__(self):
        return self.name

class EventUser(models.Model):
    f_name = models.CharField('First Name', max_length=50)
    l_name = models.CharField('Last Name', max_length=50)
    email = models.EmailField('Email', blank=True)
    phone = models.CharField('Phone Number', max_length=15, blank=True)

    def __str__(self):
        return self.f_name + ' ' + self.l_name

class Event(models.Model):
    name = models.CharField('Event Name', max_length=100)
    event_date = models.DateField('Event Date')
    start_time = models.TimeField()
    end_time = models.TimeField()
    # manager = models.CharField('Manager', max_length=60)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    man_phone = models.CharField('Manager Phone', max_length=15)
    eve_description = models.TextField('Description', blank=True)
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(EventUser, blank=True)

    def __str__(self):
        return self.name

