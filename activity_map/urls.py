from django.urls import path

from . import views

app_name = "activity_map"
urlpatterns = [
    path("", views.activity_map, name="activity_map"),
]