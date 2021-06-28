from django.shortcuts import render
from django.http import HttpResponse

def indice(request):
	response = HttpResponse()

	if request.method == 'GET':
		response.write("Usei o método GET")
	elif request.method == 'POST':
		response.write("Usei o método POST")

	return response