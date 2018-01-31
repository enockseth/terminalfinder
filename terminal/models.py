from django.contrib.gis.db import models

class Operator(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	email = models.EmailField(blank=True)
	website = models.URLField(blank=True)
	phone = models.CharField(max_length=20)
	facebook = models.URLField(blank=True)
	twitter = models.URLField(blank=True)
	instagram = models.URLField(blank=True)

	class Meta:
		verbose_name = "Operator"
		verbose_name_plural = "Operators"

	def __str__(self):
		return self.name