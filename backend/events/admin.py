from django.contrib import admin
from .models import *


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_time', 'description')
    list_display_links = ('id', 'name')
    list_editable = ('date_time',)
    search_fields = ('name', 'description',)


class CommentEventAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'rating', 'date',)
    list_display_links = ('id', 'text')
    list_filter = ('date', 'rating')
    search_fields = ('user__username',)


class HotelTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')


class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'redirect_url', 'hotel_type', 'rating')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')
    list_filter = ('hotel_type', 'rating')


admin.site.register(Event, EventAdmin)
admin.site.register(HotelType, HotelTypeAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(CommentEvent, CommentEventAdmin)