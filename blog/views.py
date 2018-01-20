from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from .models import Post


def post_list(request):                                 # potrebujeme sablonu pro seznam polozek

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render(request, 'blog/post_list.html', {"posts": posts})   # zpracuje pozadavek na strance... a ma nachystany prazdny seznam
