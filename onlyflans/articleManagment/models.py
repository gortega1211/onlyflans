from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    price = models.FloatField()
    category = models.CharField(max_length=30)

    def clean(self):
        if not self.name:
            raise ValidationError("the name is required.")
        if self.price <= 0.0:
            raise ValidationError("The price should be greater than 0.")
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)