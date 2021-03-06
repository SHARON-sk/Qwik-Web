from django.urls import path
from .views import home, user_profile, team, events, event_registration

urlpatterns = [
    path('', home, name='home'),
    path('user-profile/', user_profile, name='user-profile'),
    path('team/', team, name='team'),
    path('events/', events, name='events'),
    path('event-registration/', event_registration, name='event-registration')
]