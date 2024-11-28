from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.CharField(max_length=1000000000000000000000000000000000000000, default="none")

    def __str__(self):
        return self.title