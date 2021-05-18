from django.test import TestCase
from events.models import *


# Create your tests here.
class VenueTest(TestCase):
    def setUp(self):
        Venue.objects.create(name="test venue",
                             address="test address",
                             post_code="test post code",
                             phone="000 000 000",
                             web="website.com",
                             email="email@address.com",
                             ven_description="a sample description",
                             booking_rates=1000,
                             from_hour="07:00",
                             to_hour="15:00",
                             flour_size="100")

        EventUser.objects.create(f_name="First",
                                 l_name="Name",
                                 email="first.name@email.com",
                                 phone="111 111 111")

    def test_objects_created_successfully(self):
        venue = Venue.objects.get(name="test venue")
        self.assertEqual(venue.ven_description, "a sample description")

        eventUser = EventUser.objects.get(email="first.name@email.com")
        self.assertEqual(eventUser.f_name, "First")
        self.assertEqual(eventUser.l_name, "Name")
