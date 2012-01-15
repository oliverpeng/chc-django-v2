from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def join(request):
	return render(request, 'join/index.html')

def pray(request):
	return render(request, 'join/pray.html')

def sendprayer(request):
	return render(request, 'join/sendprayer.html')

def chclive(request):
	return render(request, 'join/chclive.html')

def partner(request):
	return render(request, 'join/partner.html')

def what_we_do(request):
	return render(request, 'what-we-do.html')

def who_we_are(request):
	return render(request, 'who-we-are.html')

def churches(request):
	return render(request, 'churches.html')

def give(request):
	return render(request, 'give.html')
