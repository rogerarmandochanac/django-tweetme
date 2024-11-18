from django.db import models

class Tweet(models.Model):
    description = models.CharField(max_length=30)
    create_att = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description[0:10]
