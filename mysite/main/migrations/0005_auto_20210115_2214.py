# Generated by Django 3.1.5 on 2021-01-15 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210115_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='quantity',
            field=models.CharField(blank=True, max_length=30, verbose_name='Количество коробок'),
        ),
        migrations.AlterField(
            model_name='task',
            name='release_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]