from django.db import models 
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text=models.CharField(max_length=70)
    created_at=models.DateTimeField(default=None,null=True)
    updated_at=models.DateTimeField(default=None,null=True)

    def __str__(self):
        return self.text