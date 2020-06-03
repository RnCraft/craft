from django.db import models

class donat(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta():
        verbose_name = 'Донат'
        verbose_name_plural = 'Донаты'

class keysi(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta():
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'

class MM(models.Model):
    number = models.IntegerField()
    player = models.IntegerField()
    victories = models.IntegerField()
    kills = models.CharField(max_length=100)
    games = models.IntegerField()
    def __str__(self):
        return self.number
    class Meta():
        verbose_name = 'MurderMystery'
        verbose_name_plural = 'MurderMystery'

class BW(models.Model):
    number = models.IntegerField()
    player = models.IntegerField()
    victories = models.IntegerField()
    beds = models.IntegerField()
    kills = models.CharField(max_length=100)
    games = models.IntegerField()
    def __str__(self):
        return self.number
    class Meta():
        verbose_name = 'BedWars'
        verbose_name_plural = 'BedWars'

