from django import template
from ..models import Category, Article

register = template.Library()

@register.simple_tag()
def get_categories():
    result = []
    categories = Category.objects.all()
    for category in categories:
        articles = Article.objects.filter(category=category)
        if len(articles) > 0:
            result.append(category)
    return result