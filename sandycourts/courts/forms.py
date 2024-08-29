from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible
from datetime import datetime
from .models import Reserve, Court, Trainer

class AddReserveForm(forms.ModelForm):
    court_id = forms.ModelChoiceField(queryset=Court.objects.all(), empty_label="Корт не выбран", label="Корт")
    trainer_id = forms.ModelChoiceField(queryset=Trainer.objects.all(), required=False, empty_label="Без тренера", label="Тренер")


    class Meta:
        model = Reserve
        fields = ['date_reserve', 'time_reserve', 'court_id', 'quantity', 'trainer_id']
        widgets = {
            'date_reserve': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("Длина превышает 50 символов")
        return title
    
    def clean_date(self):
        dt = self.cleaned_data['date_reserve']
        if dt < datetime.now:
            raise ValidationError("Дата должна быть больше текущей")

        return dt

    