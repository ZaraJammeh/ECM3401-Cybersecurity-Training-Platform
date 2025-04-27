from django.db import models

from core.models import Activity

class SortingSet(Activity):
    UI_type = models.TextField()

class SortingItem(models.Model):
    sorting_parent = models.ForeignKey(Activity, on_delete=models.CASCADE)
    phishing = models.BooleanField("Is this a phishing example?")

class SortingEmail(SortingItem):
    sender = models.CharField(max_length=40)
    subject = models.CharField(max_length=80)
    body_text = models.TextField()
    link_ranges = models.JSONField() # Stores ranges of characters that are part of a link

# TODO use inheritance to define different types of scam email
# e.g. security alert, refund/charge, special offer, share link, postage, password reset request
# create building blocks that can be put together to create specific examples for each of these types
# optionally include multiple layout options to increase variety? -> inject + populate html templates
# create a demo mode to show off features during the presentation

class SortingSMS(SortingItem):
    sender_num = models.CharField(max_length=16)
    subject = models.CharField(max_length=80)
    messages_json = models.JSONField()

class hyperlink(models.Model):
    display_type = None
    display_text = models.CharField(max_length=256)
    full_text = models.TextField()