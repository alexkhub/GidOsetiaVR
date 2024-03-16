# Generated by Django 5.0.3 on 2024-03-16 10:39

import django.db.models.deletion
import sortedm2m.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        ('expeditions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='imgs',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='expeditions.img', verbose_name='Фотографии'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='comments',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='expeditions.comment', verbose_name='Комментарии'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='imgs',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='expeditions.img', verbose_name='Фотографии'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.hoteltype', verbose_name='Тип объектов'),
        ),
    ]