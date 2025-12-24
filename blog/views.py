"""
views.py - Blog system

Them main views list:
    - article detail
    - article list
    - about page
    - contact page
    - category system
    - search system


Decorators that used in this file
    - login_check

"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import Article, Category, Comment
from .forms import Contact_Form, Comment_Form
from django.core.paginator import Paginator
from .models import Comment, Message
from django.urls import reverse
from django.contrib.auth import authenticate
from decorators.decorators import login_check


def index(request):
    article = Article.objects.filter(status=True)
    article_ordring = Article.objects.all()[:3]
    

    return render(
        request,
        "blog/index.html",
        {"objects": article, "article_ordring": article_ordring},
    )


def about(request):
    return render(request, "blog/about.html", {})



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
            return redirect(reverse("blog:home"))  #  If you to use app-name in python ,
            # you should use reverse function

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Contact_Form()

    return render(request, "blog/contact.html", {"form": form})


def article(request):
    article = (
        Article.objects.all()
    )  # Using the custom base-query-set to filter active articles
    # In manager.py, the get_queryset method filters articles with status=True
    searching = request.Get.get("q")
    results = Article.objects.filter(title_icontain = searching)
    paginator = Paginator(article, 1)  # Show 4 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "blog/blog.html", {"objects": page_obj})


@login_check  # this deocrator is for check the user if anonymous , in decorators folder
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
        "blog/article-details.html",
        {"objects": article, "form": form, "comments": comment},
    )


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = category.articles.all()
    # Reverse relationship is used here to get all articles related to the category
    # we use this by typing "model_name.related_name.all()" , the related_name is defined in the model
    # the default of related_name is "model_name_set" , so we can use "category.article_set.all()"
    # but we can change it to a more readable name like "articles" in the model

    return render(request, "blog/blog.html", {"objects": articles})


def searching_system(request):
    q = request.GET.get("q")
    result = Article.objects.filter(title__icontains=q) #Case-insensitive
    paginator = Paginator(result, 1)  # Show 1 contacts per page.

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number) # Rewrite paginator system in html file for handling q


    return render(request , "blog/blog.html" , context={"objects" : page_obj})