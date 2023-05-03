from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Voivodeship(models.Model):
    name = models.CharField(max_length=40)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Voivodeships'
    def __str__(self):
        return self.name
class Address(models.Model):
    first_name = models.CharField(max_length=40)
    middle_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40)
    voivodeship = models.ForeignKey(Voivodeship, related_name='Addresses', on_delete=models.CASCADE)
    nationality = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=40)
    house_number = models.IntegerField()
    zip_code = models.CharField(max_length=15)
    E_mail = models.CharField(max_length=50)
    Phone_number = models.BigIntegerField()
    created_by = models.ForeignKey(User, related_name='Addresses', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Addresses'
    def __str__(self):
        stringg = self.first_name +" "+ self.last_name
        return stringg