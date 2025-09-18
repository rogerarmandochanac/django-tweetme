from rest_framework import viewsets
from .serializers import TweetSerializer
from ..models import Tweet

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


