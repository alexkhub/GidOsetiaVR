# Generated by Django 5.0.3 on 2024-03-16 14:43

import autoslug.fields
import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import sortedm2m.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('img', models.ImageField(upload_to='img/%Y/%m/%d/', verbose_name='Картинка')),
                ('first_img', models.BooleanField(default=False, verbose_name='Главная картинка')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Телефон')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='username', unique=True, verbose_name='URL')),
                ('user_photo', models.ImageField(blank=True, null=True, upload_to='user_img/%Y/%m/%d/', verbose_name='Аватарка')),
                ('subscribe_to_the_newsletter', models.BooleanField(default=False, verbose_name='Подписка на рассылку')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='Комментарий')),
                ('rating', models.PositiveIntegerField(default=1, verbose_name='Оценка')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Attractions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='URL')),
                ('imgs', sortedm2m.fields.SortedManyToManyField(help_text=None, to='expeditions.img', verbose_name='Картинки')),
            ],
            options={
                'verbose_name': 'Достопримечательность',
                'verbose_name_plural': 'Достопримечательности',
            },
        ),
        migrations.CreateModel(
            name='TourOperator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название турагенства ')),
                ('logo', models.ImageField(upload_to='tour_logo/%Y/%m/%d/', verbose_name='Логотип')),
                ('email', models.EmailField(blank=True, max_length=120, null=True, verbose_name='Почта')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер телефона')),
                ('description', models.TextField(blank=True, null=True, verbose_name='О турагентсве')),
                ('rating', models.FloatField(verbose_name='Средний рейтинг')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True, verbose_name='URL')),
                ('comment', sortedm2m.fields.SortedManyToManyField(help_text=None, to='expeditions.comment', verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Туроператор',
                'verbose_name_plural': 'Туроператоры',
            },
        ),
        migrations.CreateModel(
            name='Expeditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('start_date_time', models.DateTimeField(verbose_name='Начало экспедиции')),
                ('end_date_time', models.DateTimeField(verbose_name='Конец экспедиции')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('email', models.EmailField(blank=True, max_length=120, null=True, verbose_name='Почта')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Номер телефона')),
                ('attractions', sortedm2m.fields.SortedManyToManyField(help_text=None, to='expeditions.attractions', verbose_name='Достопримечательности')),
                ('tour_operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='expeditions.touroperator', verbose_name='Туроператор')),
            ],
            options={
                'verbose_name': 'Экспедиция',
                'verbose_name_plural': 'Экспедиции',
            },
        ),
    ]
