from pyexpat import model
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UnicornUser, Community, Comment, Discussion, GriefStage, DirectMessage, Resource, UserProfile


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
    list_display = ('email', 'is_staff', 'is_active', 'user_type')
    list_filter = ('email', 'is_staff', 'is_active', 'user_type')
    readonly_fields = ('date_joined',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Profile', {'fields': ('username', 'user_type', 'email_verified')}),
        ('Activity History', {'fields': ('date_joined', 'last_login')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    inlines = [UserProfileInline]

    search_fields = ('email', 'first_name', 'last_name', 'user_type')
    ordering = ('email',)


admin.site.register(UnicornUser, UnicornUserAdmin)
admin.site.register(GriefStage)
admin.site.register(Comment)
admin.site.register(Community)
admin.site.register(Discussion)
admin.site.register(DirectMessage)
admin.site.register(Resource)
