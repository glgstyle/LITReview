from django.contrib import admin
from review.models import Ticket
from review.models import Review

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display: ('id')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display: ('id')

