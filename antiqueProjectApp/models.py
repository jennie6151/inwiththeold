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
    Antique = models.CharField(max_length=200)

    Creator = models.ForeignKey('Creator', on_delete=models.SET_NULL, null=True)
    
    Summary = models.TextField(max_length=1000, help_text='Enter a description of the antique')
        
    AntiqueType = models.ManyToManyField(AntiqueType, help_text='Select a type for this antique')

    DateOfCreation = models.IntegerField(null=True, blank=True)

    Price= models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.Title
    
    def get_absolute_url(self):
        return reverse('antique-detail', args=[str(self.id)])

    def display_AntiqueType(self):
        return ', '.join(AntiqueType.name for AntiqueType in self.AntiqueType.all()[:3])
    
    display_AntiqueType.short_description = 'AntiqueType'

class Creator(models.Model):
    """Model representing the creator/brand"""
    CreatorName = models.CharField(max_length=120)

    class Meta:
        ordering = ['CreatorName']

    def get_absolute_url(self):
        return reverse('creator-detail', args=[str(self.id)])

    def __str__(self):
        return self.CreatorName