from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    upload_img = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=(self.id,))
