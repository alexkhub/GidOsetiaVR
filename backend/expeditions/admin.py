from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'phone', 'is_staff', 'subscribe_to_the_newsletter')
    list_display_links = ('id', 'username')
    search_fields = ('email', 'phone', 'username')
    list_filter = ('is_staff', 'subscribe_to_the_newsletter')


class ImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_image')
    prepopulated_fields = {"slug": ("name",)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="90" height="90"')

    get_image.short_description = "Изображение"


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'rating', 'date',)
    list_display_links = ('id', 'title')
    list_filter = ('date', 'rating')
    search_fields = ('user__username',)


class TourOperatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo', 'email', 'phone', 'rating')
    list_display_links = ('id', 'name')
    list_filter = ('rating',)
    search_fields = ('name', 'email', 'phone')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.logo.url} width="60" height="40"')

    get_image.short_description = "Изображение"


class AttractionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


class ExpeditionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'tour_operator', 'start_date_time', 'end_date_time', 'price')
    list_display_links = ('name', 'tour_operator')
    search_fields = ('name', 'tour_operator__name',)
    list_filter = ('tour_operator__name', 'price')
    list_editable = ('start_date_time', 'end_date_time')


admin.site.register(User, UserAdmin)
admin.site.register(Img, ImgAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(TourOperator, TourOperatorAdmin)
admin.site.register(Attractions, AttractionsAdmin)
admin.site.register(Expeditions, ExpeditionsAdmin)
