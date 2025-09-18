from django.shortcuts import render
from .models import Tweet
from .forms import TweetModelForm
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


class TweetDeleteView(DeleteView):
    model = Tweet
    success_url = reverse_lazy("tweet_list")
    template_name = "tweet_confirm_delete.html"

class TweetUpdateView(UpdateView):
    queryset = Tweet.objects.all()
    form_class=TweetModelForm
    template_name = 'tweet_update.html'
    success_url = '/tweet/list'

class TweetCreateView(CreateView):
    form_class = TweetModelForm
    template_name = 'tweet_create.html'
    success_url = reverse_lazy('tweet_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TweetListView(ListView):
    queryset = Tweet.objects.all().order_by('updated')
    template_name = 'tweets.html'

    def get_queryset(self):
        query = Tweet.objects.all()
        qs = self.request.GET.get("q", None)
        if qs is not None:
            query = Tweet.objects.filter(content__icontains=qs)
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TweetModelForm
        return context

class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweet_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context

# def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     return render(request, 'tweets.html', {
#         "tweets":queryset
#     })

# def tweet_list_detail(request, pk):
#     tweet =  Tweet.objects.get(pk=pk)
#     return render(request, 'tweet_detail.html', {
#         "tweet":tweet,
#     })