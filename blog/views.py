from django.shortcuts import render

posts = [
    {
        'author': 'Ara',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date': 'August 27, 2018'
    },
    {
        'author': 'Bebito',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date': 'August 27, 2018'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
