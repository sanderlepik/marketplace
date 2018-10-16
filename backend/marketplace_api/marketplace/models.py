from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=400, null=False)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title