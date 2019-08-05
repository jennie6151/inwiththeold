from django.db import models

# Create your models here.
class antiqueType(models.Model):
    """Model representing an antique type ie pottery/glass."""
    name = models.CharField(max_length=200, help_text='Enter an antique or collectable type (e.g. Pottery vase)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

from django.urls import reverse

class Antique(models.Model):
    title = models.CharField(max_length=200)

    creator = models.ForeignKey('Creator', on_delete=models.SET_NULL, null=True)
    
    summary = models.TextField(max_length=1000, help_text='Enter a description of the antique')
        
    antiqueType = models.ManyToManyField(antiqueType, help_text='Select a type for this antique')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('antique-detail', args=[str(self.id)])