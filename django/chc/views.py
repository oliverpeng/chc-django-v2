from django.shortcuts import render


def home(request):
	return render(request, 'home.html')

def what_we_do(request):
	return render(request, 'what-we-do.html')

def who_we_are(request):
	return render(request, 'who-we-are.html')

def churches(request):
	return render(request, 'churches.html')

def give(request):
	return render(request, 'give.html')
