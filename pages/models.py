from django.db import models

class Email(models.Model):
	address = models.CharField(max_length=100, null=False)
<<<<<<< HEAD
	site = models.CharField(max_length=10, null=False)
=======

>>>>>>> 274ff29f07d98ae71fc2e73ba9699d9bf19bf62d
	def __unicode__(self):
		return self.address
