from django.db import models
from django.urls import reverse


class Image(models.Model):
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="pics")

    def get_absolute_url(self):
        return reverse("pictures")
