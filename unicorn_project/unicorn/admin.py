from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, GriefImage, GriefStage, Comment, Community, Discussion

admin.site.register(User)
admin.site.register(GriefStage)
admin.site.register(GriefImage)
admin.site.register(Comment)
admin.site.register(Community)
admin.site.register(Discussion)
