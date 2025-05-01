from django.db import models

# Define curriculum structuring classes
class Topic(models.Model):
    name = models.CharField(max_length=80, primary_key=True)
    topic_num = models.IntegerField("Topic No.")
    desc = models.TextField("Description", blank=True)
    def __str__(self):
        return self.name
    
class Subtopic(models.Model):
    name = models.CharField(max_length=80)
    parent_topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subtopic_num = models.IntegerField("Subtopic No.")
    info = models.TextField("Text for this subtopic, separate pages with \page")
    def __str__(self):
        return str(self.parent_topic.topic_num) + "." + str(self.subtopic_num)

class KnowledgePoint(models.Model):
    # AKA kp
    parent_subtopics = models.ManyToManyField(Subtopic, blank=True, through="SubtopicPoints")
    brief_desc = models.CharField(max_length=40, blank=True)
    kp_text = models.TextField("Text for this knowledge point")
    kp_question = models.TextField("Question to assess this knowledge point")
    # backup mcq answers
    def __str__(self):
        return str(self.pk) + " " + self.brief_desc

class SubtopicPoints(models.Model):
    # many-to-many resolver for Subtopic and Knowledge Points
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)
    kp = models.ForeignKey(KnowledgePoint, on_delete=models.CASCADE)

# Define parent models for Activities
class ActivityTag(models.Model):
    name = models.CharField(max_length=40, primary_key=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    estim_min_duration = models.DurationField("Estimated MIN activity duration")
    estim_max_duration = models.DurationField("Estimated MAX activity duration")
    subtopics = models.ManyToManyField(Subtopic, blank=True, through="ActivitySubtopics")
    kps = models.ManyToManyField(KnowledgePoint, blank=True, through="ActivityKps")
    tags = models.ManyToManyField(ActivityTag, blank=True, through="ActivityTags")

class ActivitySubtopics(models.Model):
    # many-to-many resolver for Activity and Subtopic
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)

class ActivityKps(models.Model):
    # many-to-many resolver for Activity and KnowledgePoint
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    kp = models.ForeignKey(KnowledgePoint, on_delete=models.CASCADE)

class ActivityTags(models.Model):
    # many-to-many resolver for Activity and ActivityTag
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    tag = models.ForeignKey(ActivityTag, on_delete=models.CASCADE)
