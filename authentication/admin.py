from django.contrib import admin
from review.models import Ticket
from review.models import Review


admin.site.register(Ticket)
admin.site.register(Review)

# Register your models here.

# if is authenticated: direction path flow