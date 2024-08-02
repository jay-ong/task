from django.shortcuts import render
from .utils import scrape_movie

from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from .models import Movie

def index(request):
    movies = scrape_movie()
    return render(request, 'index.html', {'movies': movies})


def movies(request):
    title_query = request.GET.get('title')
    source_query = request.GET.get('source')

    matching_items = []

    movie_items = Movie.objects.all()
    for item in movie_items:
        if source_query.lower() in item.endpoint.strip().lower():
            for movie in item.result.get('items', []):
                if title_query.lower() in movie['title'].strip().lower():
                    endpoint = item.endpoint.rsplit("/", 1)[0]
                    matching_items.append({
                        'title': movie['title'].strip(),
                        'link_title': movie['link_title'],
                        'poster': movie['poster'],
                        'tags': movie['tags'],
                        'endpoint': endpoint
                    })

    return JsonResponse(matching_items, safe=False)

def sources(request):
    items = []

    source_items = Movie.objects.values("endpoint").distinct()
    for item in source_items:
        endpoint = item['endpoint'].rsplit("/", 1)[0]
        items.append(endpoint)

    return JsonResponse(items, safe=False)