from django.db import models
from django.conf import settings
from .validators import validate_content

class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=140, blank=False, validators=[validate_content])
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content[0:10])
