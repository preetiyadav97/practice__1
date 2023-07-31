from django.db import models
# from phone_field import phone

# Create your models here.C\
# class User(models.Model):
#     firstname=models.CharField(max_length=20)
#     seondname=models.CharField(max_length=20)
#     # phone=models.PhoneField(max_length=10)
#     email=models.EmailField(max_length=29)
#     salary=models.FloatField(max_length=23)


#     def __str__(self):
#         return self.firstname
    


class detail(models.Model):
    firstname=models.CharField(max_length=20)
    seondname=models.CharField(max_length=20)
    # phone=models.PhoneField(max_length=10)
    email=models.EmailField(max_length=29)
    salary=models.FloatField(max_length=23)


    def __str__(self):
        return self.firstname