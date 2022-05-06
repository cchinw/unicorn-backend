from email import message
from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.TextField(
        default='https://img.freepik.com/free-vector/silhouette-unicorn-hologram-gradient-background_1048-12923.jpg?w=2000', null=True)

    def __str__(self):
        return self.username


class GriefStage(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.TextField()
    help = models.TextField()

    def __str__(self):
        return self.title


class GriefImage(models.Model):
    stage = models.ForeignKey(
        GriefStage, on_delete=models.CASCADE, related_name='stage')
    image = models.TextField()

    def __str__(self):
        return self.image


class Community(models.Model):
    category = models.CharField(max_length=500)
    image = models.TextField()
    description = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='users')
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='creator', default=True)
    grief_stage = models.ForeignKey(
        GriefStage, on_delete=models.CASCADE, related_name='community_grief_stage')
    image = models.TextField(
        null=True, default='https://www.komar.de/en/media/catalog/product/cache/5/image/9df78eab33525d08d6e5fb8d27136e95/S/H/SHX8-133_1568286487.jpg')

    def __str__(self):
        return self.category


class Discussion(models.Model):
    topic = models.TextField(max_length=2000)
    content = models.TextField()
    upvotes = models.PositiveIntegerField()
    comments = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='discussion_creator')
    community = models.ForeignKey(
        Community, on_delete=models.CASCADE, related_name='community')

    def __str__(self):
        return self.topic


class Comment(models.Model):
    comment = models.TextField()
    upvotes = models.PositiveIntegerField()
    discussion = models.ForeignKey(
        Discussion, on_delete=models.CASCADE, related_name='discussion')
    commenter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='commenter')

    def __str__(self):
        return self.topic


class DirectMessage(models.Model):
    sent_to = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_to')
    sent_from = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sent_from')
    message = models.TextField()


class Resources(models.Model):
    grief_stage = models.ForeignKey(
        GriefStage, on_delete=models.CASCADE, related_name='grief_stage')
    resource = models.TextField()
