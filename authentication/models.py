from django.conf import settings
from django.db import models


class UserFollows(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='following')
    followed_user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.CASCADE,
                                      related_name='followed_by')

    def get_followed_users(request):
        followed_users = UserFollows.objects.filter(user=request.user)
        return followed_users

    def get_followed_by(request):
        followed_by = UserFollows.objects.filter(followed_user=request.user)
        return followed_by

    class Meta:
        # ensures we don't get multiple UserFollows instances
        # for unique user-user_followed pairs
        unique_together = ('user', 'followed_user', )
