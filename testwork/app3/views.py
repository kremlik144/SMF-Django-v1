from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Author, Post




def hello(request):
    'Ответ на основе функции'

    return HttpResponse('Hello def')

def year_post(request, year):
    'Ответ на основе функции'

    return HttpResponse(f'Hello def - {year}')

def hello_name(request):
    'Ответ на основе функции'

    context = {'name':'Sergo'}
    return render(request, 'app3/index.html', context)

def son(request):
    'Ответ на основе функции'

    return render(request, 'app3/son.html')

def son2(request):
    'Ответ на основе функции'

    return render(request, 'app3/son2.html')


class HelloViev(View):
    'Ответ на основе класса '

    def get(self, request):
        return HttpResponse('Hello class')
    


def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'app3/author_posts.html', {'author':author, 'posts':posts})


def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'app3/post_full.html', {'post':post})