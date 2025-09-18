from .views import TweetListView, TweetDetailView, TweetCreateView, TweetUpdateView, TweetDeleteView
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('list/', TweetListView.as_view(), name="tweet_list"),
    path('detail/<pk>', TweetDetailView.as_view(), name="tweet_detail"),
    path('create/', TweetCreateView.as_view(), name="tweet_create"),
    path('update/<pk>', TweetUpdateView.as_view(), name="tweet_update"),
    path('delete/<pk>', TweetDeleteView.as_view(), name="tweet_delete"),
]