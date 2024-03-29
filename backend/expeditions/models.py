from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import F, Sum, Count
from sortedm2m.fields import SortedManyToManyField
from autoslug import AutoSlugField
from django.contrib.auth.hashers import make_password


class User(AbstractUser):
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)
    slug = AutoSlugField(populate_from='username', unique=True, db_index=True, verbose_name='URL', )
    user_photo = models.ImageField(upload_to='user_img/%Y/%m/%d/', verbose_name='Аватарка', blank=True, null=True)
    subscribe_to_the_newsletter = models.BooleanField(verbose_name='Подписка на рассылку', default=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.username}"

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2')):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)


class Img(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    img = models.ImageField(upload_to='img/%Y/%m/%d/', verbose_name='Картинка')
    first_img = models.BooleanField(default=False, verbose_name='Главная картинка')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.first_img:
            self.name = f'{self.name}-main'
            self.slug = f'{self.slug}-main'
        super(Img, self).save(*args, **kwargs)


class TourOperator(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название турагенства ')
    logo = models.ImageField(upload_to='tour_logo/%Y/%m/%d/', verbose_name='Логотип', blank=True, null=True)
    email = models.EmailField(max_length=120, verbose_name='Почта', blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name='Номер телефона', blank=True, null=True)
    description = models.TextField(verbose_name='О турагентсве', blank=True, null=True)
    rating = models.FloatField(verbose_name='Средний рейтинг')
    slug = AutoSlugField(populate_from='name', unique=True, db_index=True, verbose_name='URL', )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Туроператор'
        verbose_name_plural = 'Туроператоры'


class CommentTourOperator(models.Model):
    rating = models.PositiveIntegerField(verbose_name='Оценка', default=1)
    date = models.DateField(verbose_name='Дата', auto_now_add=True)
    user = models.ForeignKey('expeditions.User', verbose_name='Пользователь', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий', blank=True, null=True)
    tour_operator = models.ForeignKey('TourOperator', on_delete=models.CASCADE, verbose_name='Туроператор')

    class Meta:
        verbose_name = 'Комментарии туроператор'
        verbose_name_plural = 'Комментарии туроператор'

    def __str__(self):
        return f'{self.user}-{self.text[:15]}...'


class Attractions(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    imgs = SortedManyToManyField(Img, verbose_name='Картинки')
    description = models.TextField(verbose_name='О турагентсве', blank=True, null=True)
    address = models.CharField(max_length=80, verbose_name='Адрес', null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, db_index=True, verbose_name='URL', )

    class Meta:
        verbose_name = 'Достопримечательность'
        verbose_name_plural = 'Достопримечательности'

    def __str__(self):
        return self.name


class Expeditions(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    tour_operator = models.ForeignKey(TourOperator, on_delete=models.CASCADE, verbose_name='Туроператор')
    start_date_time = models.DateTimeField(verbose_name='Начало экспедиции')
    end_date_time = models.DateTimeField(verbose_name='Конец экспедиции')
    attractions = SortedManyToManyField(Attractions, verbose_name='Достопримечательности')
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
    email = models.EmailField(max_length=120, verbose_name='Почта', blank=True, null=True)
    phone = models.CharField(max_length=15, verbose_name='Номер телефона', blank=True, null=True)

    class Meta:
        verbose_name = 'Экспедиция'
        verbose_name_plural = 'Экспедиции'

    def __str__(self):
        return self.name
