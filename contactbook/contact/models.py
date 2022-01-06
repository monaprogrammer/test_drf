from django.db import models


class ContactDetail(models.Model):

       first_name = models.CharField(max_length=300)
       last_name = models.CharField(max_length=300)
       email = models.EmailField(null=True)
       phone_number = models.CharField(max_length=20)


       def __str__(self):
           return f'{self.first_name} {self.last_name}'
