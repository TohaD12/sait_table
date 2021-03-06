# Generated by Django 3.1.5 on 2021-01-18 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210118_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='color',
            field=models.TextField(max_length=10, verbose_name='Код цвета'),
        ),
        migrations.AlterField(
            model_name='task',
            name='details',
            field=models.TextField(blank=True, max_length=10, verbose_name='Количество штук'),
        ),
        migrations.AlterField(
            model_name='task',
            name='quantity',
            field=models.CharField(blank=True, max_length=10, verbose_name='Количество коробок'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.CharField(max_length=10, verbose_name='Код'),
        ),
    ]
