from django.urls import path
from . import views

urlpatterns=[
    path("", views.homepage, name="Homepage"),
    path("about/", views.about, name="About"),
    path("events/", views.get_all_events, name="List Events"),
    path("events/create/", views.create_event, name="Create Event"),
    path("events/<int:event_id>/update/", views.update_event, name="Update Event"),
    path("events/<int:event_id>/delete/", views.delete_event, name="Delete Event"),
    path("events/<int:event_id>/", views.get_event, name="Get Event"),
]