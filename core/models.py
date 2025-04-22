from django.db import models

class ActivityTag(models.Model):
    name = models.CharField(max_length=40, primary_key=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    estim_min_duration = models.DurationField("Estimated MIN activity duration")
    estim_max_duration = models.DurationField("Estimated MAX activity duration")
    tags = models.ManyToManyField(ActivityTag, blank=True)