from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

def validation_content(value):
    content = value
    if content == 'abc':
        raise ValidationError("No puede ser abc")
    return value

class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    content = models.CharField(max_length=140, validators=[validation_content])
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    # def clean(self):
    #     if self.content == "abc":
    #         raise ValidationError("Cannot abc")
    #     return super().clean()

    def __str__(self):
        return str(self.content)[0:15]

