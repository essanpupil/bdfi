from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, unique=True)
    publish_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    content = models.TextField()

    def __str__(self):
        return self.title
