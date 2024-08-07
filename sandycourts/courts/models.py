from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator, MaxLengthValidator


class News(models.Model):

    title = models.CharField(max_length=150, verbose_name ='Заголовок')
    content = models.TextField(blank=True, verbose_name ='Текст статьи')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    date_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None,
                              blank=True, null=True, verbose_name="Фото")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug",                           
                            validators=[
                               MinLengthValidator(5, message="Минимум 5 символов"),
                               MaxLengthValidator(100, message="Максимум 100 символов"),
                           ])
    is_published = models.BooleanField(default=True, verbose_name="Статус")
    
    def get_absolute_url(self):
        return reverse('post', kwargs = {'post_slug': self.slug})
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['-date_create']

class Tournament(models.Model):
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
        ('O', 'Смешанный'),
    )

    title = models.CharField(max_length=150, verbose_name = 'Название')
    date = models.DateField(auto_now_add=True, verbose_name = 'Дата проведения')
    comands_quantity = models.IntegerField(default=0, verbose_name = 'Кол-во команд')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name = 'Пол')
    contribution = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = 'Взнос')
    prize = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = 'Призовой фонд')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug",                           
                            validators=[
                               MinLengthValidator(5, message="Минимум 5 символов"),
                               MaxLengthValidator(100, message="Максимум 100 символов"),
                           ])
    is_active = models.BooleanField(default=True, verbose_name = 'Статус')

    def get_absolute_url(self):
        return reverse('tournament', kwargs = {'tournament_slug': self.slug})
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'
    
class Trainer(models.Model):    
    last_name = models.CharField(max_length=30, verbose_name = 'Фамилия')
    first_name = models.CharField(max_length=30, verbose_name = 'Имя')
    contribution = models.DecimalField(max_digits=7, decimal_places=2, verbose_name = 'Цена')
    location = models.ForeignKey('Location', on_delete=models.PROTECT, verbose_name = 'Расположение')

    def get_absolute_url(self):
        return reverse('trainer', kwargs = {'trainer_id': self.pk})
    
    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name}'
    
    class Meta:
        verbose_name = 'Тренер'
        verbose_name_plural = 'Тренеры'

class Location(models.Model):
    name = models.CharField(max_length=50, verbose_name ='Название')
    adress = models.CharField(max_length=100, verbose_name ='Адрес')
    phone_number = models.CharField(max_length=30, verbose_name ='Телефон')
    courts = models.IntegerField(default=0, verbose_name ='Кол-во кортов')

    def get_absolute_url(self):
        return reverse('location', kwargs = {'loc_id': self.pk})

    def __str__(self) -> str:
        return f'{self.name}'
    
    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'

class Court(models.Model):
    court_number = models.IntegerField(default=0, verbose_name ='№ корта')
    capacity = models.IntegerField(default=0, verbose_name ='Вместимость')
    location = models.ForeignKey(Location, on_delete=models.PROTECT, verbose_name ='Расположение')
    price_weekday1 = models.DecimalField(max_digits=7, decimal_places=2, verbose_name ='Цена. Будни-день')
    price_weekday2 = models.DecimalField(max_digits=7, decimal_places=2, verbose_name ='Цена. Будни-вечер')
    price_weekend = models.DecimalField(max_digits=7, decimal_places=2, verbose_name ='Цена. Выходной')

    def __str__(self) -> str:
        return f'{self.court_number}'
    
    class Meta:
        verbose_name = 'Корт'
        verbose_name_plural = 'Корты'