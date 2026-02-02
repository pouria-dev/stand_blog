"""
views.py - Blog system

Them main views list:
    - index page
    - article detail
    - article list include searching functionality
    - about page
    - contact page
    - categories list



Decorators that used in this file
    - login_check

"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Article, Category, Comment
from .forms import Contact_Form, Comment_Form
from django.core.paginator import Paginator
from .models import Comment, Message
from django.urls import reverse , reverse_lazy
from django.contrib.auth import authenticate
from decorators.decorators import login_check
from django.views.generic import TemplateView , FormView , ListView

class IndexView(ListView):
    model = Article
    template_name = "blog/index.html"
    context_object_name = "articles"
    def get_queryset(self):
        return Article.objects.filter(status=True).order_by('-id')[:3]  # ordering by newest articles first

class AboutView(TemplateView):
    template_name = "blog/about.html"


class ArticleListView(ListView):
    model = Article
    template_name = "blog/list.html"
    context_object_name = "articles"
    paginate_by = 4  # Number of articles per page

    def get_queryset(self):
        queryset = super().get_queryset()
        searching = self.request.GET.get("q")
        if searching:
            queryset = queryset.filter(title__icontains=searching)
        return queryset
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '') # q is key , '' is default value
        return context
    

class CategoryListView(ListView):
    model = Article
    template_name = "blog/list.html"
    context_object_name = "articles"
    
    def get_queryset(self):
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=slug)
        return category.articles.all()

class ContactView(FormView):
    template_name = "blog/contact.html"
    form_class = Contact_Form
    success_url = reverse_lazy("blog:contact")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)



@login_check  # this decorator is for check the user if anonymous , in decorators folder
def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    comment = Comment.objects.filter(article=article, parent__isnull=True)

    if request.method == "POST":
        form = Comment_Form(request.POST)
        parent_id = request.POST.get("parent_id")

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.article = article

            if parent_id:
                try:
                    comment_parent = Comment.objects.get(id=parent_id)
                    comment.parent = comment_parent
                except Comment.DoesNotExist:
                    comment.parent = None

            comment.save()

            return redirect(reverse("blog:detail", kwargs={"slug": slug}))

    else:
        form = Comment_Form()

    return render(
        request,
        "blog/detail.html",
        {"objects": article, "form": form, "comments": comment},
    )

    
