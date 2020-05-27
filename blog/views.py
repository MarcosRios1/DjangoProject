from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Michelle Obama',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 5th, 2020'
    },
    {
        'author': 'John Doe',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'April 8th, 2020'
    }
]


def home(request):
    context = {
        'title': 'Blog',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})