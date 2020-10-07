from django.db import models

# Create your models here.
class Movie(models.Model):
	moviename=models.CharField(max_length=50)
	heroname=models.CharField(max_length=50)
	heroineame=models.CharField(max_length=50)
	poster=models.ImageField(upload_to='poster/',null='True')
	directorname=models.CharField(max_length=50)
	releasedate=models.DateField(null=True)