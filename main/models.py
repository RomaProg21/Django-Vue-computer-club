from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class  Equipment(models.Model):
    number = models.IntegerField('Номер')
    type = models.IntegerField('Тип')
    name = models.CharField('Название',max_length=100)
    status = models.IntegerField('Статус')
    vip = models.BooleanField('Вип')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудования'



class  Periphery(models.Model):

    type = models.IntegerField('Тип')
    name = models.CharField('Название',max_length=100)

    def __str__(self):
        if self.type == 0:
            tipe = 'мышь'
        elif self.type == 1:
            tipe = 'наушники'
        elif self.type == 2:
            tipe = 'коврик'
        elif self.type == 3:
            tipe = 'клавиатура'
        elif self.type == 4:
            tipe = 'Стандарт'

        return f'{self.name} {tipe}'

    class Meta:
        verbose_name = 'Периферия'
        verbose_name_plural = 'Периферии'


class Reservation(models.Model):
    equipment = models.ForeignKey('Equipment', on_delete=models.PROTECT)
    time_start = models.DateTimeField('Начало')
    end_date = models.DateTimeField('Конец')
    comment = models.TextField('Комментарий',max_length=255)
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    periphery = models.ManyToManyField('Periphery', blank=True)
    def __str__(self):
        return  self.comment
    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

class UsernameTelegram(models.Model):
     userTg = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     nameTg = models.CharField('Имя телеграм',max_length=255)
     def __str__(self):
        return  self.nameTg
     class Meta:
        verbose_name = 'Имя телеграмм'
        verbose_name_plural = 'Имена телеграммов'

class GameTur(models.Model):
    nameGame = models.CharField('Название игры',max_length=100)
    photo = models.ImageField(upload_to='images/', null=True)
    def __str__(self):
        return  self.nameGame
    class Meta:
        verbose_name = 'Игра для турниров'
        verbose_name_plural = 'Игры для турниров'

class Tournament(models.Model):
    nameTournament = models.CharField('Название турнира',max_length=100)
    gameTour = models.ForeignKey('GameTur', on_delete=models.PROTECT)
    dateStartTour = models.DateTimeField('Дата Начала турнира')
    comment = models.TextField('Комментарий к турниру', max_length=999)
    def __str__(self):
        return  self.nameTournament
    class Meta:
        verbose_name = 'Турнир'
        verbose_name_plural = 'Турниры'

class PeopleTournament(models.Model):
    UserIdTour = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    TournamentId = models.ForeignKey('Tournament', on_delete=models.PROTECT)
    date_register = models.DateTimeField('Дата регистрации пользователя на турнир')
    comment = models.CharField('Комментарий',max_length=255)
    def __str__(self):
        return  self.comment
    class Meta:
        verbose_name = 'Бронь на турнир'
        verbose_name_plural = 'Бронь на турниры'


class Phone(models.Model):
     userPhone = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     phoneNumber = models.CharField('Телефон пользователя',max_length=19)
     def __str__(self):
        return  self.phoneNumber
     class Meta:
        verbose_name = 'Телефон пользователя'
        verbose_name_plural = 'Телефоны пользователей'