from django.shortcuts import get_object_or_404, HttpResponse, render
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

import json
import random
import re

from .models import GapFillText, GapFillOption

def get_valid_option_pos_list(option_obj):
    # extract list of valid gap positions from GapFillOption object
    valid_pos_str = option_obj.valid_positions_str
    return valid_pos_str.split(",")

@login_required
def activity(request, gap_fill_id):
    gap_fill_obj = get_object_or_404(GapFillText, pk=gap_fill_id)
    options_list = list(GapFillOption.objects.filter(gap_fill_parent=gap_fill_id))
    # randomise options' order of appearance
    random.shuffle(options_list)
    context = {
        "text_list": re.split(r"\[.*?\]", gap_fill_obj.text),
        "options_list": options_list,
    }
    return render(request, "gap_fill/activity.html", context)

# @require_POST()
def check(request):
    request_json = json.load(request)
    rsp_json = {}
    for option_id in request_json.keys():
        # for each option, value = True if its current slot is valid or False if not
        option_obj = get_object_or_404(GapFillOption, pk=option_id)
        # add SLOT number, True/False pair to response
        # enables frontend to easily process correct/incorrect input in slot order
        rsp_json[request_json[option_id]] = request_json[option_id] in option_obj.valid_positions_str.split(",")
    print(rsp_json)
    return HttpResponse(json.dumps(rsp_json), content_type='application/json')
