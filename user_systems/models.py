from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone

from core.models import Subtopic, KnowledgePoint, Activity

# Code for custom users heavily based on:
# https://testdriven.io/blog/django-custom-user-model/

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        # create and save user
        if not email:
            raise ValueError("The Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        # create and save superuser
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)


# define custom user model that uses email as unique identifier
# to remove need for username
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField("email", unique=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Course(models.Model):
    estim_duration = models.DurationField()
    length = models.IntegerField()
    next_activity = models.IntegerField(default=1)

class CourseData(models.Model):
    parent_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    activity_id = models.ForeignKey(Activity, on_delete=models.CASCADE)
    index = models.IntegerField()
    
class CurrentCourse(models.Model):
    # links user and course (*:1) externally from user model
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

class SubtopicCoverage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE)
    last_covered_on = models.DateField()

class Ratings(models.IntegerChoices):
        # enum for rating user knowledge of each kp
        UNSEEN = 0
        SEEN = 1
        PRACTISED = 2
        APPLIED = 3
        MASTERED = 4

class UserKnowledgeData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    kp = models.ForeignKey(KnowledgePoint, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Ratings)
    updated_on = models.DateField()

    def set_rating(self, new_rating):
        self.rating = new_rating
    
class UserKnowledgeUpdate(models.Model):
    # used to store pending knowledge updates
    # submitted to UserKnowledgeData via POST when an Activity is completed
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    kp = models.ForeignKey(KnowledgePoint, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=Ratings)
    # store ID of posting Activity to prevent cheated scores through memorising + reattempting
    anticheat_id = models.ForeignKey(Activity, on_delete=models.CASCADE)