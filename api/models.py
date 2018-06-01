from django.db import models

# Create your models here.

class Blog(models.Model):
	title=models.CharField(max_length=200)
	body=models.CharField(max_length=200)
	def __unicode__(self):
		return self.title

class Login(models.Model):
	username=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	def __unicode__(self):
		return self.username

		