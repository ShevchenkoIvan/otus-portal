from django.shortcuts import render
import socket
import os


def index_view(request):
    name_host = socket.gethostname()
    file = open('./test_secret.txt', 'r')
    config_file = open('./test_config.txt', 'r')
    secret = file.read()
    config = config_file.read()
    env_sec = os.environ.get('MY_ENV')
    context = {
        'name_host': name_host,
        'secret': secret,
        'secret_env': env_sec,
        'config': config,
    }

    return render(request, 'otus/index.html', context)
