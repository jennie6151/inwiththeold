from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AntiqueType(models.Model):
    """Model representing an antique type ie pottery/glass."""
    name = models.CharField(max_length=200, help_text='Enter an antique or collectable type (e.g. Pottery vase)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

from django.urls import reverse

class Antique(models.Model):
    """Model representing an antique/collectable/artefact"""
    AntiqueName = models.CharField(max_length=200)
    AntiqueImage = models.FilePathField(path="/img", null=True, blank=True)
    Creator = models.ForeignKey('Creator', on_delete=models.SET_NULL, null=True)
    Summary = models.TextField(max_length=1000, help_text='Enter a description of the antique')
    AntiqueType = models.ManyToManyField(AntiqueType, help_text='Select a type for this antique')
    DateOfCreation = models.IntegerField(null=True, blank=True)
    Price= models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.AntiqueName
    
    def get_absolute_url(self):
        return reverse('antique-detail', args=[str(self.id)])

    def display_AntiqueType(self):
        return ', '.join(AntiqueType.name for AntiqueType in self.AntiqueType.all()[:3])
    
    display_AntiqueType.short_description = 'AntiqueType'

import uuid
from django.contrib.auth.models import User
import datetime

class AntiqueSale(models.Model):
    """Model representing a specific sale"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular antique sale')
    antiqueBuyer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    antique = models.ForeignKey('Antique', on_delete=models.SET_NULL, null=True)
    customerFirstName = models.CharField(max_length=100, null=False)
    customerLastName = models.CharField(max_length=100, null=False)
    customerAddressLine1 = models.TextField(max_length=200, null=False)
    customerAddressLine2 = models.TextField(max_length=200, null=True)
    customerAddressCity = models.TextField(max_length=200, null=False)
    customerAddressCounty = models.TextField(max_length=200, null=False)
    customerAddressPostcode = models.TextField(max_length=12, null=False)
    customerEmail = models.TextField(max_length=200, null=False)
    customerTelephone = models.TextField(max_length=20, null=False)
    saleDate = models.DateField(default=datetime.date.today)

    
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.antique.AntiqueName})'


class Creator(models.Model):
    """Model representing the creator/brand"""
    CreatorName = models.CharField(max_length=120)

    class Meta:
        ordering = ['CreatorName']

    def get_absolute_url(self):
        return reverse('creator-detail', args=[str(self.id)])

    def __str__(self):
        return self.CreatorName