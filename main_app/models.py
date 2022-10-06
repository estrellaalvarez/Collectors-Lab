from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Skin(models.Model):

    name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    price = models.TextField(max_length=200)
    verified_artist = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
