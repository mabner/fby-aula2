from django.http import HttpResponse
from django.shortcuts import render


def indice(request):
    response = HttpResponse()

    if request.method == 'GET':
        response.write("Usei o método GET")
    elif request.method == 'POST':
        response.write("Usei o método POST")

    return response
