from django.db import models

# Create your models here

class Place(models.Model):
    pl_name=models.CharField(max_length=30)
    pl_email=models.EmailField(max_length=100)
    pl_phone=models.IntegerField()
    pl_image=models.ImageField()

    def __str__(self):
        return self.pl_name
    

