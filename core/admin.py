from django.contrib import admin

from .models import *

class TopicAdmin(admin.ModelAdmin):
    list_display = ["topic_num", "name"]
admin.site.register(Topic, TopicAdmin)

admin.site.register(Subtopic)
admin.site.register(KnowledgePoint)
admin.site.register(SubtopicPoints)

admin.site.register(ActivityTag)
admin.site.register(ActivitySubtopics)
admin.site.register(ActivityKps)
admin.site.register(ActivityTags)