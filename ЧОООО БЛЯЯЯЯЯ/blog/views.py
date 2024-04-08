from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import ArticleForm, UserRegister, UserLogin, CommentForm
from .models import Article, Comment
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

class ArticleView(ListView):
    model = Article
    context_object_name = 'articles'
    extra_context = {
        'title': "Breaking"
    }
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Article.objects.filter(publish=True)
class ArticleByCategory(ArticleView):
    def get_queryset(self):
        return Article.objects.filter(category_id=self.kwargs['pk'],publish=True)

class ArticleDetail(DetailView):
    model = Article
    context_object_name = 'article'
    def get_queryset(self):
        return Article.objects.filter(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        article = Article.objects.get(pk=self.kwargs['pk'])
        context['comments'] = Comment.objects.filter(article=article)
        context['comment_form'] = CommentForm()
        return context
def profile(request):
    context = {
        'title':"Profile"
    }
    return render(request,'blog/profile.html', context)

def user_logout(request):
    logout(request)
    return redirect('index')

def user_login(request):
    if request.method == "POST":
        form = UserLogin(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('index')
    else:
        form = UserLogin()
    context = {
        'title':"Login",
        'form':form
    }
    return render(request,'blog/user_login.html', context)

def user_register(request):
    if request.method == "POST":
        form = UserRegister(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserRegister()
    context = {
        'title':"Register",
        'form':form
    }
    return render(request,'blog/user_register.html', context)


class AddArticle(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/add_article.html'
    extra_context = {
        'title': "Add Article"
    }

class EditArticle(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/add_article.html'
    extra_context = {
        'title': "Edit Article"
    }

class DeleteArticle(DeleteView):
    model = Article
    context_object_name = "article"
    extra_context = {
        "title":"Delete"
    }
    success_url = reverse_lazy('index')


def save_comment(request,article_id):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.article = Article.objects.get(pk=article_id)
        comment.save()
    else:
        pass
    return redirect('article', article_id)


class SearchResult(ArticleView):
    def get_queryset(self):
        word = self.request.GET.get('q')
        articles = Article.objects.filter(
            Q(title__icontains=word) | Q(content__icontains=word), publish=True
        )
        return articles


