# Generated by Django 3.1.5 on 2021-01-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210119_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Название'),
        ),
    ]
