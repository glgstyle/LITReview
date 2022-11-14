from django.contrib import admin
from .models import UserFollows


@admin.register(UserFollows)
class UserFollowsAdmin(admin.ModelAdmin):
    list_display: ('id')
