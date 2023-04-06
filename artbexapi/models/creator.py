from django.db import models
from django.contrib.auth.models import User


class Creator(models.Model):

    firstName = models.DateField(max_length=55)
    lastName = models.DateField(max_length=55)
    email = models.DateField(max_length=55)

    @property
    def full_name(self): 
        return f'{self.user.first_name} {self.user.last_name}'