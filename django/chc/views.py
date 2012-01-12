from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def join(request):
	return render(request, 'home.html')

def what_we_do(request):
	return render(request, 'home.html')

def where_we_are(request):
	return render(request, 'home.html')

def churches(request):
	return render(request, 'home.html')

def give(request):
	return render(request, 'home.html')