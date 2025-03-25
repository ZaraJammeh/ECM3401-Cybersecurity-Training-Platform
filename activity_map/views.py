from django.shortcuts import get_object_or_404, HttpResponse, render
from django.urls import reverse

from core.models import Activity, ActivityTag

def activity_map(request):
    activity_pool = Activity.objects.filter(tags__name="email")
    # query above should never lead to none because only valid tags should be selectable
    # TODO include topic "complexity" in tags (i.e. beginner/intermediate/advanced)
    activity1 = activity_pool[0]
    # TODO use activity_obj.gapfilltext to check if activity is a gap fill etc
    context = {
        "activity_link": reverse("gap-fill:activity", args=[activity1.pk])
    }
    return render (request, "activity-map/activity_map.html", context)