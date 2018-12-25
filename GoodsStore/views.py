from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from .forms import NewArticleForm
from .models import Article

class IndexView(ListView):
    model = Article
    template_name = "index.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "detail.html"

class ArticleView(ListView):
    model = Article
    template_name = "detail_all.html"

class ArticleCreateView(CreateView):
    model = Article
    template_name = "add_article.html"
    form_class = NewArticleForm

    def get_success_url(self):
        return reverse('detail', args=(self.object.id,))