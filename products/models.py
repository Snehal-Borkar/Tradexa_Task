from django.db import models

# Create your models here.
 
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=70)
    weight=models.FloatField()
    price=models.FloatField()
    created_at=models.DateTimeField(default=None,null=True)
    updated_at=models.DateTimeField(default=None,null=True)

    def __str__(self):
        return self.name
