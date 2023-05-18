from django.db import models
from django.contrib.auth.models import User
import requests
from math import ceil
# Create your models here.
class Voivodeship(models.Model):
    def ApiVoivodeships():
        start=0
        baseurl = 'https://bdl.stat.gov.pl/api/v1/units?level=2&page=' + str(start)
        print(baseurl)
        r = requests.get(baseurl)
        data = r.json()

        TotalRecords = data['totalRecords']
        PageSize = data['pageSize']
        NumberOfPages=ceil(TotalRecords/PageSize)
        Voivodeship=[]
        while start!=NumberOfPages:
            for x in data['results']:
                Voivodeship.append(x['name'])
            start+=1
            baseurl = 'https://bdl.stat.gov.pl/api/v1/units?level=2&page=' + str(start)
            r = requests.get(baseurl)
            data = r.json()
        Voivodeship.append("FOREIGNER/CUDZOZIEMIEC")
        return Voivodeship
    stackVoivo = ApiVoivodeships()
    VOIVODESHIP_CHOICES = [(str(x), str(x)) for x in stackVoivo]
    name = models.CharField(max_length=40, choices=VOIVODESHIP_CHOICES)
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
    nationality = models.CharField(max_length=50)
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=40, blank=True)
    house_number = models.IntegerField()
    zip_code = models.CharField(max_length=15)
    E_mail = models.CharField(max_length=50, blank=True)
    Phone_number = models.BigIntegerField()
    created_by = models.ForeignKey(User, related_name='Addresses', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Addresses'
    def __str__(self):
        stringg = self.first_name +" "+ self.last_name
        return stringg