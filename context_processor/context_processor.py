# context_processor.py
# This file contains context processors for the Django application.
## It provides additional context data from model to all templates with out views.



from blog.models import Article , Category
def recent_article(request):

    recent = Article.objects.order_by('-created')

    return {'recent':recent}

def article_category(request):
    category = Category.objects.all()
    return {'category':category}