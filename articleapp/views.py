from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.list import MultipleObjectMixin

from articleapp.forms import ArticleCreateForm
from articleapp.models import ArticleCreateModel
from commentapp.forms import CommentForms
from commentapp.models import CommentModel


class ArticleCreateView(CreateView):
    model = ArticleCreateModel
    form_class = ArticleCreateForm
    # success_url = reverse_lazy('mainpage:mainpage')
    template_name = 'article_create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.article = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:article_detail', kwargs={'pk': self.object.pk})

class ArticleDetailView(DetailView, FormMixin):
    model = ArticleCreateModel
    form_class = CommentForms
    context_object_name = 'target_article'
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        object_list = CommentModel.objects.filter(writer=self.get_object())
        return super(ArticleDetailView, self).get_context_data(object_list=object_list, **kwargs)
