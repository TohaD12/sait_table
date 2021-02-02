from django.db import models



class Task(models.Model):
    class Meta:
        verbose_name = "Данные полуфабриката"
        verbose_name_plural = "Данные полуфабриката"
        ordering = [
            '-release_date']

    details_name = models.CharField("Дельта", max_length=100, blank=True)
    code = models.CharField("Код детали", max_length=50, blank=True)
    color_code = models.CharField("Код цвета", max_length=50, blank=True)
    quantity_actual = models.CharField("Фактический остаток", max_length=50, blank=True)
    quantity_1c = models.CharField("Остаток 1с", max_length=50, blank=True)
    delta = models.CharField("Дельта", max_length=50, blank=True)
    adjustments = models.CharField("Корректировка", max_length=50, blank=True)
    adjustments_marriage = models.CharField("Списание в брак", max_length=50, blank=True)
    actual_registration = models.CharField("Постановка на учет", max_length=50, blank=True)
    after_adjustment_quantity_actual = models.CharField("Фактический остаток после корректировки",
                                                        max_length=50, blank=True)
    after_adjustment_quantity_1c = models.CharField("Остаток 1с после корректировки", max_length=50, blank=True)
    after_adjustment_delta = models.CharField("Дельта после корректировки", max_length=50, blank=True)
    release_date = models.DateField("Дата пересчета")

    def __str__(self):
        return self.details_name


class Accessories(models.Model):
    class Meta:
        verbose_name = "Данные комплектующих"
        verbose_name_plural = "Данные комплектующих"
        ordering = [
            '-release_date']

    details_name = models.CharField("Дельта", max_length=100, blank=True)
    code = models.CharField("Код детали", max_length=50, blank=True)
    quantity_actual = models.CharField("Фактический остаток", max_length=50, blank=True)
    quantity_1c = models.CharField("Остаток 1с", max_length=50, blank=True)
    delta = models.CharField("Дельта", max_length=50, blank=True)
    adjustments = models.CharField("Корректировка", max_length=50, blank=True)
    adjustments_marriage = models.CharField("Списание в брак", max_length=50, blank=True)
    actual_registration = models.CharField("Постановка на учет", max_length=50, blank=True)
    after_adjustment_quantity_actual = models.CharField("Фактический остаток после корректировки",
                                                        max_length=50, blank=True)
    after_adjustment_quantity_1c = models.CharField("Остаток 1с после корректировки", max_length=50, blank=True)
    after_adjustment_delta = models.CharField("Дельта после корректировки", max_length=50, blank=True)
    release_date = models.DateField("Дата пересчета")

    def __str__(self):
        return self.details_name


