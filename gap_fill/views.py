from django.shortcuts import get_object_or_404, render

import re

from .models import GapFillText, GapFillOption

def active(request, gap_fill_id):
    gap_fill_obj = get_object_or_404(GapFillText, pk=gap_fill_id)
    context = {
        "gap_fill_obj": gap_fill_obj,
        "text_list": re.split(r"\[.*?\]", gap_fill_obj.text)
    }
    return render(request, "gap_fill/active.html", context)
