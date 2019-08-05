from django.db import models

# Create your models here.
class antiqueType(models.Model):
    """Model representing an antique type ie pottery/glass."""
    name = models.CharField(max_length=200, help_text='Enter an antique or collectable type (e.g. Pottery vase)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name

