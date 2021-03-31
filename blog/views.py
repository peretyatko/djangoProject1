from django.shortcuts import render

posts = [
    {'author': 'Peretya',
     'title': 'Blog Post1',
     'content': 'First post content',
     'date_posted': 'August 27, 2018'
     },
    {'author': 'Mark',
     'title': 'Blog Post2',
     'content': 'Second post content',
     'date_posted': 'August 28, 2021'
     }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
