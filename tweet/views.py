from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from .models import Tweet
from .forms import TweetModelForm


# Create your views here.
def home(request):
    return render(request, 'index.html', {})

class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = 'tweet/create_view.html'
    success_url = reverse_lazy("tweet_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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