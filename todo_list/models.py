from django.db import models

# Create your models here.
class List(models.Model):
	item=models.CharField(max_length=50)
	done=models.BooleanField(default=False)

	def __str__(self):
		return self.item
