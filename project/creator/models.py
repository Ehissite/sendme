from django.db import models
# reference to the users
from django.contrib.auth.models import User

# Create your models here.
class Creators(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='upload/creators')
    user = models.OneToOneField(User, related_name='creator', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    