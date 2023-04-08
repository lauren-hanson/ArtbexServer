from django.db import models
# from django.contrib.auth.models import User


class Creator(models.Model):

    firstName = models.CharField(max_length=55)
    lastName = models.CharField(max_length=55)
    email = models.CharField(max_length=55)

    @property
    def full_name(self): 
        return f'{self.user.first_name} {self.user.last_name}'