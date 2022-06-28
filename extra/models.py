from distutils.command.upload import upload
from email.mime import image
from tabnanny import verbose
from django.db import models

# Create your models here.

class Carousel(models.Model):
    title = models.CharField("Nomi", max_length=255)
    image = models.ImageField("Rasm", upload_to='carousel/')

    class Meta:
        verbose_name = "Carousel"
        verbose_name_plural = "Carousel"

    def __str__(self):
        return self.title