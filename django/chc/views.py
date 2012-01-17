from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django import forms

class SignupForm(forms.Form):
	fname = forms.CharField()
	lname = forms.CharField()
	city = forms.CharField()
	state = forms.CharField()
	country = forms.CharField()
	email = forms.EmailField()
	is_pastor = forms.BooleanField()
	phone = forms.CharField()
	church_name = forms.CharField()
	church_website = forms.CharField()
	take_offering = forms.BooleanField()
	contact_me = forms.BooleanField()
	receive_updates = forms.BooleanField()


def home(request):
	return render(request, 'home.html')

def join(request):
	return render(request, 'join/index.html')

def signup(request):
	from django.core.context_processors import csrf

	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			fname = form.cleaned_data['fname']
			lname = form.cleaned_data['lname']
			city = form.cleaned_data['city']
			state = form.cleaned_data['state']
			country = form.cleaned_data['country']
			email = form.cleaned_data['email']
			is_pastor = form.cleaned_data['is_pastor']
			phone = form.cleaned_data['phone']
			church_name = form.cleaned_data['church_name']
			church_website = form.cleaned_data['church_website']
			take_offering = form.cleaned_data['take_offering']
			contact_me = form.cleaned_data['contact_me']
			receive_updates = form.cleaned_data['receive_updates']
			
			if is_pastor:
				from django.core.mail import send_mail
				message = ""
    			send_mail("Pastor signed up", message, sender, recipients)

			return HttpResponseRedirect('/thanks/')
	else:
		form = SignupForm()

	c = { 'form': form}
	return render_to_response('join/signup.html', c, context_instance=RequestContext(request))

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
