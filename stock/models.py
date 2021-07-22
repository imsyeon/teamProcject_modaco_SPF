from django.db import models

# Create your models here.

class KospiData(models.Model):
    kospi_date = models.CharField(max_length=50)
    conclusion = models.FloatField()
    volume = models.IntegerField()
    trade_value = models.IntegerField()

class Kosdaq(models.Model):
    kosdaq_date = models.CharField(max_length=50)
    conclusion = models.FloatField()
    volume = models.IntegerField()
    trade_value = models.IntegerField()

class Report(models.Model):
    report_stock = models.CharField(max_length=30)
    report_title = models.CharField(max_length=200)
    report_publisher = models.CharField(max_length=30)
    report_date = models.CharField(max_length=50)
    report_link = models.URLField()

    def __str__(self):
            return f'[{self.pk}]{self.report_title}'

class Capitalzation(models.Model):
    stockRank = models.IntegerField()
    stockName = models.CharField(max_length=40)
    stockPrice = models.IntegerField()
    stockCap = models.IntegerField()
    stockVolume = models.IntegerField()

    def __str__(self):
            return f'[{self.stockRank}]{self.stockName}'

class Kospicap(models.Model):
    stockRank = models.IntegerField()
    stockName = models.CharField(max_length=40)
    stockPrice = models.IntegerField()
    stockCap = models.IntegerField()
    stockVolume = models.IntegerField()

    def __str__(self):
            return f'[{self.stockRank}]{self.stockName}'

