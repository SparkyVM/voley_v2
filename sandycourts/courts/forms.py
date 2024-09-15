from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible
from datetime import date
from .models import Reserve, Court, Trainer, News

from django.db.models import Sum


    # Форма добавления Новости
class AddNewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'content', 'photo', 'slug', 'is_published']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 150:
            raise ValidationError("Длина превышает 150 символов")
        return title
    
    
    # Форма добавления Брони
class AddReserveForm(forms.ModelForm):

    date_reserve = forms.DateField(initial=date.today(), label='Дата брони', widget=forms.DateInput(format="%Y-%m-%d", attrs={'type': 'date'} ) )
    #time_reserve = forms.ChoiceField(widget=forms.RadioSelect(choices=model.Time_choices), label='Время брони')
    quantity = forms.IntegerField(initial=1, label='Кол-во человек')
    court_id = forms.ModelChoiceField(queryset=Court.objects.all(), empty_label="Корт не выбран", label="Корт")
    trainer_id = forms.ModelChoiceField(queryset=Trainer.objects.all(), required=False, empty_label="Без тренера", label="Тренер")

    class Meta:
        model = Reserve
        fields = ['court_id', 'date_reserve', 'time_reserve', 'quantity', 'trainer_id']

        widgets = {
            'time_reserve' : forms.RadioSelect(choices=model.Time_choices)
        }
    
    def clean_date_reserve(self):
        form_date_reserve = self.cleaned_data['date_reserve']
        if form_date_reserve < date.today():
            raise ValidationError("Дата должна быть больше или равна текущей")
        return form_date_reserve
    
    def clean_time_reserve(self):                   # !!!!!! Доделать. Должно быть не доступно Без времени
        form_time_reserve = self.cleaned_data['time_reserve']
        if not form_time_reserve:
            raise ValidationError("Выберите время")
        return form_time_reserve
        
    def clean_court_id(self):
        form_court_id = self.cleaned_data['court_id']
        if not form_court_id:
            raise ValidationError("Выберите корт")
        return form_court_id

    def clean_quantity(self):
        form_quantity = self.cleaned_data['quantity']
        q_reserve = Reserve.objects.filter(date_reserve = self.cleaned_data['date_reserve'], 
                                           time_reserve = self.cleaned_data['time_reserve'], 
                                           court_id = self.cleaned_data['court_id'])
        q_court = Court.objects.get(pk = self.cleaned_data['court_id'].pk)
        if q_reserve.count() != 0:
            reserved_item = q_reserve.aggregate(Sum('quantity'))['quantity__sum']
            free_item = q_court.capacity - reserved_item
        else:
            reserved_item = 0
            free_item = q_court.capacity
        if free_item - form_quantity < 0:              # Проверка на свободные места
            if free_item == 0:
                raise ValidationError(f'На {self.cleaned_data['time_reserve']}:00 мест не осталось. Выберите другое время')
            else:
                raise ValidationError(f'Недостаточно свободных мест! Осталось {free_item} мест')
        return form_quantity
    
    def clean_trainer_id(self):
        form_trainer = self.cleaned_data['trainer_id']
        q_reserve = Reserve.objects.filter(date_reserve = self.cleaned_data['date_reserve'], 
                                           time_reserve = self.cleaned_data['time_reserve'], 
                                           trainer_id = self.cleaned_data['trainer_id'])
        # Проверка - тренер доступен на местоположении
        q_court = Court.objects.get(pk = self.cleaned_data['court_id'].pk)
        if form_trainer.location != q_court.location:
        #if q_trainer.location != q_trainer.location:
            raise ValidationError(f'Тренер {form_trainer} не доступен на {q_court}')
        else:
            # Проверка - занят тренер
            if q_reserve.count() != 0:
                raise ValidationError(f'В {self.cleaned_data['time_reserve']}:00 {form_trainer} уже занят')
        return form_trainer

    
'''
class AddReserveForm(forms.ModelForm):
    court_id = forms.ModelChoiceField(queryset=Court.objects.all(), empty_label="Корт не выбран", label="Корт")
    trainer_id = forms.ModelChoiceField(queryset=Trainer.objects.all(), required=False, empty_label="Без тренера", label="Тренер")

    class Meta:
        model = Reserve
        fields = ['date_reserve', 'time_reserve', 'quantity', 'trainer_id','court_id']
        
        widgets = {
            'date_reserve': forms.DateInput(attrs={'type': 'date'}),        #, 'value': date.today().strftime("%d-%m-%Y")
            'time_reserve' : forms.RadioSelect(choices=model.Time_choices)
        }
    
    def clean_date_reserve(self):
        dt = self.cleaned_data['date_reserve']
        if dt < date.today():
            raise ValidationError("Дата должна быть больше или равна текущей")
        return dt
'''
