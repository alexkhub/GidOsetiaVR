from django.db import models
from sortedm2m.fields import SortedManyToManyField
from autoslug import AutoSlugField

class Event(models.Model):
    name = models.CharField(max_length=100 , verbose_name='Название',)
    date_time = models.DateTimeField(verbose_name='Время и дата')
    description = models.TextField(verbose_name='Описание', )
    imgs = SortedManyToManyField('expeditions.Img', verbose_name='Фотографии')
    slug = AutoSlugField(populate_from='name', unique=True, db_index=True, verbose_name='URL', )

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.name

class HotelType(models.Model):
    name = models.CharField(max_length=100 , verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    slug = AutoSlugField(populate_from='name', unique=True, db_index=True, verbose_name='URL', )
    class Meta:
        verbose_name = 'Тип объекта'
        verbose_name_plural = 'Типы объектов'

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100 , verbose_name='Название')
    email = models.EmailField(max_length=120, verbose_name='Почта', blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name='Номер телефона', blank=True, null=True)
    redirect_url = models.SlugField(verbose_name='URL заведения', )
    hotel_type = models.ForeignKey(HotelType , on_delete=models.SET_NULL, verbose_name='Тип объектов', null=True, blank=True)
    imgs = SortedManyToManyField('expeditions.Img', verbose_name='Фотографии')
    comments = SortedManyToManyField('expeditions.Comment', verbose_name='Комментарии')
    rating = models.FloatField(verbose_name='Средний рейтинг')
    description = models.TextField(verbose_name='Описание')
    slug = AutoSlugField(populate_from='name', unique=True, db_index=True, verbose_name='URL', )

    class Meta:
        verbose_name = 'Место отдыха'
        verbose_name_plural = 'Места отдыха'

    def __str__(self):
        return self.name
