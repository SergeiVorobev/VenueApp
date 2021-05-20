from django.urls import path
from . import views

urlpatterns =[
     path('register/', views.registration, name="registration"),
     path('login/', views.loginPage, name="login"),
     path('logout/', views.logoutUser, name="logout"),
     path('', views.home, name="home"),
     path('<int:year>/<str:month>/', views.home, name="home"),
     path('events/', views.all_events, name="list-events"),
     path('venues/', views.all_venues, name="list-venues"),
     path('show_venue/<venue_id> ', views.show_venue, name='show-venue'),
     path('venues/add_venue/', views.add_venue, name='add-venue'),
     path('search_venues/', views.search_venues, name='search-venues'),
     path('show_event/<event_id> ', views.show_event, name='show-event'),
     path('events/add_event/', views.add_event, name='add-event'),
     path('search_events/', views.search_events, name='search-events'),
     path('edit_event/<event_id>', views.edit_event, name="edit-event"),
     path('edit_venue/<venue_id>', views.edit_venue, name="edit-venue"),
     path('del_event/<event_id>', views.del_event, name="del-event"),
     path('del_venue/<venue_id>', views.del_venue, name="del-venue"),
]