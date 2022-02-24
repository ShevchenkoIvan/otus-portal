from django.shortcuts import render
import socket


def index_view(request):
    name_host = socket.gethostname()

    return render(request, 'otus/index.html', {'name_host': name_host})
