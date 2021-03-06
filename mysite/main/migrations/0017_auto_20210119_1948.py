# Generated by Django 3.1.5 on 2021-01-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210119_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='adjustments',
            field=models.CharField(blank=True, max_length=10, verbose_name='Корректировка'),
        ),
        migrations.AlterField(
            model_name='task',
            name='after_adjustment_delta',
            field=models.CharField(blank=True, max_length=10, verbose_name='Дельта после корректировки'),
        ),
        migrations.AlterField(
            model_name='task',
            name='after_adjustment_quantity_1c',
            field=models.CharField(blank=True, max_length=10, verbose_name='Остаток 1с после корректировки'),
        ),
        migrations.AlterField(
            model_name='task',
            name='after_adjustment_quantity_actual',
            field=models.CharField(blank=True, max_length=10, verbose_name='Фактический остаток после корректировки'),
        ),
        migrations.AlterField(
            model_name='task',
            name='color_code',
            field=models.CharField(blank=True, max_length=10, verbose_name='Код цвета'),
        ),
        migrations.AlterField(
            model_name='task',
            name='quantity_1c',
            field=models.CharField(blank=True, max_length=10, verbose_name='Остаток 1с'),
        ),
        migrations.AlterField(
            model_name='task',
            name='quantity_actual',
            field=models.CharField(blank=True, max_length=10, verbose_name='Фактический остаток'),
        ),
    ]
