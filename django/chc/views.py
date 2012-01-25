from django.shortcuts import render


def home(request):
	return render(request, 'home.html')

def what_we_do(request):
	return render(request, 'what-we-do/index.html')

def projects(request):
    return render(request, 'what-we-do/projects.html')

def who_we_are(request):
	return render(request, 'who-we-are.html')

def churches(request):
	return render(request, 'churches.html')

def give(request):
	return render(request, 'give.html')

def media(request):
    return render(request, 'media.html')