from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=40, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    price = models.IntegerField(max_length=6, null=False, blank=False)
    upload_img = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title
