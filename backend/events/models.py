from django.db import models
from sortedm2m.fields import SortedManyToManyField
from autoslug import AutoSlugField


class Event(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', )
    date_time = models.DateTimeField(verbose_name='Время и дата')
    description = models.TextField(verbose_name='Описание', blank=True)
    imgs = SortedManyToManyField('expeditions.Img', verbose_name='Фотографии', blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, db_index=True, verbose_name='URL', )

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.name


class CommentEvent(models.Model):
    rating = models.PositiveIntegerField(verbose_name='Оценка', default=1)
    date = models.DateField(verbose_name='Дата', auto_now_add=True)
    user = models.ForeignKey('expeditions.User', verbose_name='Пользователь', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name='Мероприятие')

    class Meta:
        verbose_name = 'Комментарии эвента'
        verbose_name_plural = 'Комментарии эвентов'

    def __str__(self):
        return f'{self.user}-{self.text[:15]}...'


class HotelType(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, db_index=True, verbose_name='URL', )

    class Meta:
        verbose_name = 'Тип объекта'
        verbose_name_plural = 'Типы объектов'

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(max_length=120, verbose_name='Почта', blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name='Номер телефона', blank=True, null=True)
    redirect_url = models.SlugField(verbose_name='URL заведения', )
    hotel_type = models.ForeignKey(HotelType, on_delete=models.SET_NULL, verbose_name='Тип объектов', null=True,
                                   blank=True)
    imgs = SortedManyToManyField('expeditions.Img', verbose_name='Фотографии', blank=True)
    comments = SortedManyToManyField('expeditions.Comment', verbose_name='Комментарии', blank=True)
    rating = models.FloatField(verbose_name='Средний рейтинг')
    description = models.TextField(verbose_name='Описание')
    slug = AutoSlugField(populate_from='name', unique=True, db_index=True, verbose_name='URL', )

    class Meta:
        verbose_name = 'Место отдыха'
        verbose_name_plural = 'Места отдыха'

    def __str__(self):
        return self.name

class CommentHotel(models.Model):
    rating = models.PositiveIntegerField(verbose_name='Оценка', default=1)
    date = models.DateField(verbose_name='Дата', auto_now_add=True)
    user = models.ForeignKey('expeditions.User', verbose_name='Пользователь', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    hotel  = models.ForeignKey('Hotel' , on_delete=models.CASCADE, verbose_name='Отель')

    class Meta:
        verbose_name = 'Комментарии отели'
        verbose_name_plural = 'Комментарии отели'

    def __str__(self):
        return f'{self.user}-{self.text[:15]}...'