from django.db import models
from django.contrib.auth.models import *
# Create your models here.
class sign_up_add(models.Model):
    first_name= models.CharField(max_length=20)
    last_name= models.CharField(max_length=20)
    username= models.CharField(max_length=20,primary_key=True)
    password= models.CharField(max_length=20)
    confirm_password= models.CharField(max_length=20)
    email= models.EmailField()
    mobile_number= models.CharField(max_length=20)

    # def __str__(self):
    #     return self.first_name
    # def __str__(self):
    #     return self.last_name

    # def __str__(self):
    #     return self.confirm_password
    # def __str__(self):
    #     return self.password
    # def __str__(self):
    #     return self.email

    def __str__(self):
        return self.username #+" "+self.first_name+" "+self.last_name+" "+self.email+" "+self.mobile_number
