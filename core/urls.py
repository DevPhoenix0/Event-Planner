from django.urls import path
from . import views

urlpatterns=[
    path("", views.homepage, name="Homepage"),
    path("about/", views.about, name="About")
]