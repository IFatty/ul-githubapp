from django.shortcuts import render
import requests


def search(request):
    username = request.GET['username']
    api = "https://api.github.com/users"
    context = {}
    if len(username) > 0:
        api = (api + "/" + username)
        response = requests.get(api)
        context = {"users": [response.json()]}
    else:
        response = requests.get(api)
        context = {"users": response.json()}
    return render(request, 'search.html', context)


def index(request):
    context = {}
    return render(request, 'index.html', context)
