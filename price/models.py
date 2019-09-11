from django.db import models

# Create your models here.
class entry(models.Model):
	url=models.CharField(max_length=1000)
	email=models.CharField(max_length=50)
	price=models.IntegerField()

def __str__(self):
		return '<ID: {} , email: {} >'.format(self.id,self.email) 