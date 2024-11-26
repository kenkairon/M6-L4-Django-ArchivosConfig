from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    ordering = ['-created_at']  # Orden por fecha descendente

def clean(self):
    if self.price <= 0:
        raise ValidationError('El precio debe ser mayor que cero.')

    def __str__(self):
        return self.name
