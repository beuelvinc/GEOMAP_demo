from django.db import models
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Person(models.Model):
	name=models.CharField(max_length=50)
	lng=models.CharField(max_length=50)
	lat=models.CharField(max_length=50)
	country = CountryField()
	image=models.ImageField(upload_to="images/", default='default.png', blank=True, null=True)
	def __str__(self):
		return self.name
	def getImage(self):
		if not self.image:
			return 'static/media_root/images/default.png'


