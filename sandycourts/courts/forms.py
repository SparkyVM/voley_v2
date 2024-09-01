from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible
from datetime import date
from .models import Reserve, Court, Trainer, News


    # Форма добавления Брони
class AddReserveForm(forms.ModelForm):
    court_id = forms.ModelChoiceField(queryset=Court.objects.all(), empty_label="Корт не выбран", label="Корт")
    trainer_id = forms.ModelChoiceField(queryset=Trainer.objects.all(), required=False, empty_label="Без тренера", label="Тренер")
    

    class Meta:
        model = Reserve
        fields = ['date_reserve', 'time_reserve', 'court_id', 'quantity', 'trainer_id']
        widgets = {
            'date_reserve': forms.DateInput(attrs={'type': 'date'}),
            'time_reserve' : forms.RadioSelect(choices=model.Time_choices)
        }
    
    def clean_date_reserve(self):
        dt = self.cleaned_data['date_reserve']
        if dt < date.today():
            raise ValidationError("Дата должна быть больше или равна текущей")
        return dt


    # Форма добавления Новости
class AddNewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'content', 'slug', 'photo', 'is_published']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 150:
            raise ValidationError("Длина превышает 150 символов")
        return title