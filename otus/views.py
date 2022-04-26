from django.shortcuts import render
import socket


def index_view(request):
    name_host = socket.gethostname()
    file = open('./test_secret.txt', 'r')
    secret = file.read()

    return render(request, 'otus/index.html', {'name_host': name_host, 'secret': secret})
