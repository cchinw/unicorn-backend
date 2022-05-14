from email import message
from operator import truediv
import resource
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


class UnicornUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'UnicornAdmin'),
        (2, 'Griever'),
    )
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    user_type = models.PositiveSmallIntegerField(
        choices=USER_TYPE_CHOICES, null=True)

    def __str__(self):
        return self.email


class GriefStage(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(
        upload_to='uploads/images/grief', blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title


class Resources(models.Model):
    title = models.CharField(
        max_length=500, default='Grief Handling Resource')
    resource = models.TextField()
    image = models.ImageField(
        upload_to='uploads/resources', blank=True, null=True)

    def __str__(self):
        return self.title


class Community(models.Model):
    name = models.CharField(max_length=500)
    banner = models.ImageField(blank=True, null=True)
    description = models.TextField()
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='members', blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='creator', default=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField()
    avatar = models.ImageField(
        upload_to='uploads/avatar', blank=True, null=True)
    grief_stage = models.ForeignKey(
        GriefStage, on_delete=models.CASCADE, related_name='user_grief_stage', blank=True, null=True)

    def __str__(self):
        return self.user.username


class Discussion(models.Model):
    topic = models.TextField(max_length=2000)
    content = models.TextField()
    upvotes = models.PositiveIntegerField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='discussion_creator')
    community = models.ForeignKey(
        Community, on_delete=models.CASCADE, related_name='community')

    def __str__(self):
        return self.topic


class Comment(models.Model):
    text = models.TextField()
    upvotes = models.PositiveIntegerField()
    discussion = models.ForeignKey(
        Discussion, on_delete=models.CASCADE, related_name='discussion')
    commenter = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='commenter')

    def __str__(self):
        return self.text


class DirectMessage(models.Model):
    sent_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_to')
    sent_from = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_from')
    message = models.TextField()

    def __str__(self):
        return self.sent_from
