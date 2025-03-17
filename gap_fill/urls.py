from django.urls import path

from . import views

app_name = "gap-fill"
urlpatterns = [
    path("<int:gap_fill_id>/", views.activity, name="activity"),
    path("check/", views.check, name="check"),
]