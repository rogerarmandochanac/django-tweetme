from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Tweet


# Create your views here.
def home(request):
    return render(request, 'index.html', {})


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = 'tweet/detail_view.html'

class TweetListView(ListView):
    queryset = Tweet.objects.all()
    template_name = 'tweet/list_view.html'


def tweet_detail_view(request, id=1):
    obj = Tweet.objects.get(id=id)
    context = {
        'object': obj
    }
    return render(request, 'detail_view.html', context)

def tweet_list_view(request):
    queryset = Tweet.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'list_view.html', context)