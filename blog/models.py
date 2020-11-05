from django.db import models

# Create your models here.
class Post(models.Model):
	image = models.ImageField(upload_to ='evenr_images/')
	title = models.CharField(max_length=300)
	date = models.DateTimeField()
	text = models.TextField()

	def get_summary(self):
		return self.text[:100]


	def __str__(self):
		return self.title