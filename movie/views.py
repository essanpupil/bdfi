from django.shortcuts import render


def home(request):
    return render(request, 'movie/index.html')


def left_sidebar(request):
    return render(request, 'movie/left-sidebar.html')


def rigth_sidebar(request):
    return render(request, 'movie/right-sidebar.html')


def no_sidebar(request):
    return render(request, 'movie/no-sidebar.html')
