# Python function, take a request as an argument and returns dict of data as a context
from .models import Category


def menu_links(request):
    links = Category.objects.all()  # fetch all cats from db
    return dict(links=links)
