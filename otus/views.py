from django.shortcuts import render
import socket
import os


def index_view(request):
    name_host = socket.gethostname()
    file = open('./test_secret.txt', 'r')
    secret = file.read()
    env_sec = os.environ['APPDATA']

    return render(request, 'otus/index.html', {'name_host': name_host, 'secret': secret, 'secret_env': env_sec})
