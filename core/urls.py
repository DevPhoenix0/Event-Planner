from django.urls import path
from . import views

urlpatterns=[
    path("", views.homepage, name="Homepage"),
    path("about/", views.about, name="About"),
    path("list/", views.get_all_events, name="List Events"),
    path("create/", views.create_event, name="Create Event"),
]