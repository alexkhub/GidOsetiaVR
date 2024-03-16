# Generated by Django 5.0.3 on 2024-03-16 20:46

import sortedm2m.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_initial'),
        ('expeditions', '0002_remove_comment_title_alter_comment_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='comments',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='expeditions.comment', verbose_name='Комментарии'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='event',
            name='imgs',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='expeditions.img', verbose_name='Фотографии'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='comments',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='expeditions.comment', verbose_name='Комментарии'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='imgs',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='expeditions.img', verbose_name='Фотографии'),
        ),
        migrations.AlterField(
            model_name='hoteltype',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
