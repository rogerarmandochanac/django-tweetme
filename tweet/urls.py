from django.urls import path, include
from .views import home, tweet_detail_view, tweet_list_view, TweetDetailView, TweetListView

urlpatterns = [
    path('', home, name="home"),
    path('detail/<pk>', TweetDetailView.as_view(), name='detail'),
    path('list/', TweetListView.as_view(), name='list'),
]