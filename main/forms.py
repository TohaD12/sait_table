from .models import Task, Accessories
from django.forms import ModelForm, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["details_name", "code", "color_code", "quantity_actual", "quantity_1c", "delta", "adjustments",
                  "after_adjustment_quantity_actual", "after_adjustment_quantity_1c", "after_adjustment_delta",
                  "adjustments_marriage"]
        widgets = {
            'details_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название детали'
            }),
            'code': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код детали'
            }),
            'color_code': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код цвета'
            }),
            'quantity_actual': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фактический остаток'
            }),
            'quantity_1c': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Остаток 1с'
            }),
            'delta': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дельта'
            }),
            'adjustments': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Корректировка'
            }),
            'adjustments_marriage': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Списание в брак'
            }),
            'after_adjustment_quantity_actual': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фактический остаток после карректировки'
            }),
            'after_adjustment_quantity_1c': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Остаток 1с после корректировки'
            }),
            'after_adjustment_delta': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дельта после корректировки'
            }),

        }


class AccessoriesForm(ModelForm):
    class Meta:
        model = Accessories
        fields = ["details_name", "code", "quantity_actual", "quantity_1c", "delta", "adjustments",
                  "after_adjustment_quantity_actual", "after_adjustment_quantity_1c", "after_adjustment_delta",
                  "adjustments_marriage"]
        widgets = {
            'details_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название детали'
            }),
            'code': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Код детали'
            }),
            'quantity_actual': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фактический остаток'
            }),
            'quantity_1c': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Остаток 1с'
            }),
            'delta': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дельта'
            }),
            'adjustments': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Корректировка'
            }),
            'adjustments_marriage': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Списание в брак'
            }),
            'after_adjustment_quantity_actual': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фактический остаток после карректировки'
            }),
            'after_adjustment_quantity_1c': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Остаток 1с после корректировки'
            }),
            'after_adjustment_delta': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дельта после корректировки'
            }),

        }
