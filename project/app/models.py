from django.db import models
class project(models.Model):
    title=models.CharField(max_length=2048)
    description=models.TextField()
    image=models.URLField()
    vedio=models.URLField()
# Create your models here.
image = models.ImageField(upload_to="project/images")

