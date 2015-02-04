from django.db import models

class Email(models.Model):
	address = models.CharField(max_length=100, null=False)
	site = models.CharField(max_length=10, null=False)
	def __unicode__(self):
		return self.address
