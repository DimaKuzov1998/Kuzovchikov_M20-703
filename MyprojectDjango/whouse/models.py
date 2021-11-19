from django.db import models

class Pr(models.Model):
    height = models.CharField(max_length=15, verbose_name='Высота, см')
    width = models.CharField(max_length=15, verbose_name='Ширина, см')
    length = models.CharField(max_length=15, verbose_name='Длина, см')
    weight = models.CharField(max_length=15, verbose_name='Масса, кг')
    recdate = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата поступления')
    nofcon = models.CharField(max_length=20, verbose_name='Номер договора')
    client = models.ForeignKey('Client', null=True, on_delete=models.PROTECT, verbose_name='Клиент')
    content = models.TextField(null=True, blank=True, verbose_name='Указание')
    expdate = models.CharField(max_length=12, verbose_name='Дата окончания')
    rack = models.ForeignKey('Rack', null=True, on_delete=models.PROTECT, verbose_name='Стеллаж')
    numofpos = models.CharField(max_length=10, verbose_name='Номер позиции')
    def __str__(self):
        return self.content
    
    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['-recdate']

class Client(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название юр. лица')
    requisites = models.TextField(verbose_name='Банковские реквизиты')
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = 'Клиенты'
        verbose_name = 'Клиент'
        ordering = ['-name']

class Rack(models.Model):
    number = models.CharField(max_length=20, db_index=True, verbose_name='Номер')
    room = models.ForeignKey('Room', null=True, on_delete=models.PROTECT, verbose_name='Помещение')
    seats = models.CharField(max_length=20, db_index=True, verbose_name='Количество мест')
    H = models.CharField(max_length=20, db_index=True, verbose_name='Высота места, см')
    W = models.CharField(max_length=20, db_index=True, verbose_name='ширина места, см')
    L = models.CharField(max_length=20, db_index=True, verbose_name='Длина места, см')
    load = models.CharField(max_length=20, db_index=True, verbose_name='Максимальная нагрузка, кг')
    def __str__(self):
        return 'Стеллаж №' + self.number
        
    class Meta:
        verbose_name_plural = 'Стеллажи'
        verbose_name = 'Стеллаж'
        ordering = ['-number']

class Room(models.Model):
    namer = models.CharField(max_length=20, db_index=True, verbose_name='Название')
    V = models.CharField(max_length=20, db_index=True, verbose_name='Полезный объем, м^3')
    def __str__(self):
        return self.namer
        
    class Meta:
        verbose_name_plural = 'Помещения'
        verbose_name = 'Помещение'
        ordering = ['-namer']