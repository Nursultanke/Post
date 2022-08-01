from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    date = models.DateField()

