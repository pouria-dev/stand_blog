from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Article, Category
from .forms import Contact_Form, Comment_Form
from django.core.paginator import Paginator
from .models import Comment, Message
from django.urls import reverse


def index(request):
    article = Article.objects.filter(status=True)
    article_ordring = Article.objects.all()[:3]

    return render(request, 'blog/index.html', {'objects': article, 'article_ordring': article_ordring})


def contact(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = Contact_Form(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            name = form.cleaned_data["name"]
            text = form.cleaned_data["text"]
            email = form.cleaned_data["email"]
            Message.objects.create(name=name, text=text, email=email)

            # redirect to a new URL:
            return redirect(reverse("blog:home"))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Contact_Form()

    return render(request, "blog/contact.html", {"form": form})


def article(request):
    article = Article.objects.filter(status=True)

    paginator = Paginator(article, 1)  # Show 4 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', {'objects': page_obj})


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    comment = Comment.objects.all()

    if request.method == "POST":
        form = Comment_Form(request.POST)

        if form.is_valid():
            text = form.cleaned_data['text']

            Comment.objects.create(text=text, post=article)


    else:
        form = Comment_Form()

    return render(request, 'blog/article-details.html', {'objects': article,
                                                         'comments': comment,
                                                         "form": form})


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()

    return render(request, 'blog/blog.html', {'objects': articles})


def search(request):
    q = request.GET.get('q')
    search_title = Article.objects.filter(title__icontains=q)  # sensitive without "i" in contains
    paginator = Paginator(search_title, 1)  # Show 1 article per pages.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/blog.html', {'objects': page_obj})
