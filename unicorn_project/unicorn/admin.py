from pyexpat import model
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UnicornUser, Community, Comment, Discussion, GriefStage, DirectMessage, Resources, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    fk_name = 'user'
    verbose_name = 'Unicorn User Profile'
    verbose_name_plural = 'Unicorn User Profiles'


class UnicornUserAdmin(UserAdmin):
    model = UnicornUser
    can_delete = False
    fk_name = 'user'
    verbose_name = 'Unicorn User'
    verbose_name_plural = 'Unicorn Users'
    inlines = [UserProfileInline]


admin.site.register(UnicornUser, UnicornUserAdmin)
admin.site.register(GriefStage)
admin.site.register(Comment)
admin.site.register(Community)
admin.site.register(Discussion)
admin.site.register(DirectMessage)
admin.site.register(Resources)
