from django.db import models
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField('Производитель', max_length=100, unique=True)
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'



class Phone(models.Model):
    name = models.CharField('Название телефона', max_length=100, unique=True)
    description = models.TextField('Описание', null=True)
    poster = models.ImageField('Постер телефона', upload_to='phones/', null=True)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name='Производитель', on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField('Цена', default=0)
    number_of_sim_cards = models.PositiveIntegerField('Количество сим-карт', default=2)
    screen_size = models.FloatField('Диагональ экрана')
    screen_refresh_rate = models.PositiveIntegerField('Частота обновления экрана', default=60)
    screen_resolution = models.CharField('Разрешение экрана', max_length=100)
    main_camera_resolution = models.PositiveIntegerField('Разрешение основной камеры', default=0)
    front_camera_resolution = models.PositiveIntegerField('Разрешение фронтальной камеры', default=0)
    number_of_main_cameras = models.PositiveIntegerField('Каличество основных камер', default=0)
    built_in_memory = models.PositiveIntegerField('Обьем встроенной памяти', default=0)
    ram = models.PositiveIntegerField('Оперативная память', default=0)
    battery_capacity = models.PositiveIntegerField('Емкость аккумулятора', default=0)
    phone_release_date = models.DateField('Дата выхода телефона')
    operating_system = models.ForeignKey('OperatingSystem', verbose_name='Операционная система', on_delete=models.SET_NULL, null=True)
    wireless_interfaces = models.ManyToManyField('WirelessInterfaces', verbose_name='Безпроводной интерфейс')
    communication_standards = models.ManyToManyField('CommunicationStandards', verbose_name='Стандарт связи')
    processor_model = models.ForeignKey('ProcessorModel', verbose_name='Модель процессора', on_delete=models.SET_NULL, null=True)
    screen_type = models.ForeignKey('ScreenType', verbose_name='Тип экрана', on_delete=models.SET_NULL, null=True)
    headphone_jack = models.ForeignKey('HeadphoneJack', verbose_name='Разьем для наушников', on_delete=models.SET_NULL, null=True)
    charging_connector_type = models.ForeignKey('ChargingConnectorType', verbose_name='Тип разъема для зарядки', on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey('Color', verbose_name='Цвет', on_delete=models.SET_NULL, null=True)
    draft = models.BooleanField('Черновик', default=False)
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Смартфон'
        verbose_name_plural = 'Смартфоны'



class OperatingSystem(models.Model):
    name = models.CharField('Операционная система', unique=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Операционная система'
        verbose_name_plural = 'Операционные системы'



class WirelessInterfaces(models.Model):
    name = models.CharField('Безпроводной интерфейс', unique=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Безпроводной интерфейс'
        verbose_name_plural = 'Безпроводные интерфейсы'



class CommunicationStandards(models.Model):
    name = models.CharField('Стандарт связи', unique=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стандарт связи'
        verbose_name_plural = 'Стандарты связи'



class ProcessorModel(models.Model):
    name = models.CharField('Модель процессора', unique=True, max_length=100)
    number_of_processor_cores = models.PositiveIntegerField('Каличество ядер процессора', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Модель процессора'
        verbose_name_plural = 'Модели процессоров'



class ScreenType(models.Model):
    name = models.CharField('Тип экрана', unique=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип экрана'
        verbose_name_plural = 'Типы экрана'



class HeadphoneJack(models.Model):
    name = models.CharField('Разьем для наушников', unique=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Разъем для наушников'
        verbose_name_plural = 'Разъемы для наушников'

class ChargingConnectorType(models.Model):
    name = models.CharField('Тип разъема для зарядки', unique=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Разъем для зарядки'
        verbose_name_plural = 'Разъемы для зарядки'



class Color(models.Model):
    name = models.CharField('Цвет', unique=True, max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'



class PhoneShots(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение телефона', upload_to='phone_shots/')
    phone = models.ForeignKey(Phone, verbose_name='Телефон', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Фотография телефона'
        verbose_name_plural = 'Фотографии телефонов'



class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField('Значение', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'



class Rating(models.Model):
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='Звезда')
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, verbose_name='Телефон')

    def __str__(self):
        return f'{self.star} - {self.phone}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'



class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Сообщение', max_length=6000)
    phone = models.ForeignKey(Phone, verbose_name='Телефон', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
