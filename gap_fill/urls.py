from django.urls import path

from . import views

urlpatterns = [
    path("<int:gap_fill_id>/", views.active, name="active"),
]