from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name