from django.db import models

class ImagePic(models.Model):
    content = models.ImageField(upload_to='')
    style = models.ImageField(upload_to='')
    result = models.ImageField(upload_to='', default="None")