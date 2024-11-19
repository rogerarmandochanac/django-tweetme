from django.urls import path, include
from .views import home, TweetDetailView, TweetListView, TweetCreateView

urlpatterns = [
    path('', home, name="home"),
    path('detail/<pk>', TweetDetailView.as_view(), name='detail'),
    path('list/', TweetListView.as_view(), name='tweet_list'),
    path('create/', TweetCreateView.as_view(), name="tweet_create"),
]