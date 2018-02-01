from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Operator(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    email = models.EmailField('E-Mail', blank=True)
    website = models.URLField(blank=True)
    phone = PhoneNumberField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    class Meta:
        verbose_name = "Operator"
        verbose_name_plural = "Operators"

    def __str__(self):
        return self.name


class Station(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.PROTECT)
    town = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    phone = PhoneNumberField(blank=True)
    phone2 = PhoneNumberField('Phone 2', blank=True)
    region = models.CharField(max_length=2)
    lon = models.FloatField()
    lat = models.FloatField()
    pnt = models.PointField()

    class Meta:
        verbose_name = "Station"
        verbose_name_plural = "Stations"

    def __str__(self):
        return "%s - %s" % (self.operator, self.town)
