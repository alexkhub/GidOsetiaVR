# Generated by Django 5.0.3 on 2024-03-16 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expeditions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='touroperator',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='tour_logo/%Y/%m/%d/', verbose_name='Логотип'),
        ),
    ]
