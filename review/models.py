from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models


class Ticket(models.Model):
    # Your Ticket model definition goes here
    title = models.fields.CharField(max_length=128)
    author = models.fields.CharField(max_length=128, blank=True)
    description = models.fields.TextField(max_length=2048, blank=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    @property
    def is_reviewed(self):
        review = Review.objects.filter(ticket=self)
        if review.count() >= 1:
            return True
        else:
            return False


class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(
        # max_length=1024,
        # validates that rating must be between 0 and 5
        validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.CharField(max_length=8192, blank=True)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
