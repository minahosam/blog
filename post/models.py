from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=100)
    post_time=models.TimeField(auto_now=True)
    post_date=models.DateField(auto_now=True)
    author=models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.pk)