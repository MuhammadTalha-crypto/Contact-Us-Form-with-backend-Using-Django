from django.db import models

# Create your models here.
#data is the model name.
class data(models.Model):

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    desc = models.TextField()
    #To store data in database against "name" entered in the Contact us form
    def __str__(self):
        return self.name
    
