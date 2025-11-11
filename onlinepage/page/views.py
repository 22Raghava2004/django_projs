from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.template import TemplateDoesNotExist

def home(request):
    # This sends a list of numbers 1–50 to home.html
    movie_ids = range(1, 51)
    return render(request, 'home.html', {'movie_ids': movie_ids})

def movie_detail(request, movie_id):
    try:
        # dynamically pick movie1.html, movie2.html, etc.
        return render(request, f'movie{movie_id}.html')
    except TemplateDoesNotExist:
        # if the file movie{movie_id}.html doesn’t exist, show error
        return HttpResponseNotFound(f"Movie {movie_id} page not found.")
