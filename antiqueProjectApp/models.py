from django.db import models

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
    title = models.CharField(max_length=200)

    creator = models.ForeignKey('Creator', on_delete=models.SET_NULL, null=True)
    
    summary = models.TextField(max_length=1000, help_text='Enter a description of the antique')
        
    AntiqueType = models.ManyToManyField(AntiqueType, help_text='Select a type for this antique')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('antique-detail', args=[str(self.id)])

class Creator(models.Model):
    """Model representing the creator/brand"""
    creator_name = models.CharField(max_length=120)
    date_of_creation = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['creator_name']

    def get_absolute_url(self):
        return reverse('creator-detail', args=[str(self.id)])

    def __str__(self):
        return self.creator_name