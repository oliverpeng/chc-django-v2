from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django import forms

class SignupForm(forms.Form):
	fname = forms.CharField(required=False, label='First Name')
	lname = forms.CharField(required=False, label='Last Name')
	city = forms.CharField(required=False, label="City")
	state = forms.CharField(required=False, label="State / Province")
	country = forms.CharField(required=False, label = "Country")
	email = forms.EmailField(label="Email Address")
	is_pastor = forms.BooleanField(required=False, label="Check here if you are a pastor.")
	phone = forms.CharField(required=False, label="Phone")
	church_name = forms.CharField(required=False, label="Church Name")
	church_website = forms.URLField(required=False, label="Church Website")
	take_offering = forms.BooleanField(required=False, label="I'm on board. Our church will take an offering at the next crisis.")
	contact_me = forms.BooleanField(required=False, label="I am interested. Please contact me.")
	receive_updates = forms.BooleanField(required=False, label="I would like to receive updates.")


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
			
			#if is_pastor:
			#	from django.core.mail import send_mail
			#	message = ""
			#	send_mail("Pastor signed up", message, sender, recipients)

			import urllib
			import urllib2
			import json

			url = 'http://us1.api.mailchimp.com/1.3/'
			method = 'listSubscribe'    	
			params = {
				'apikey': '420524bc6e7e2495ddd87a95dd48a3dd-us1',
				'id': '9b182b13d8',
				'email_address': email,
				'merge_vars': {
					'FNAME': fname,
					'LNAME': lname,
					'CITY': city,
					'STATE': state,
					'CHURCH': church_name,
					'WEBSITE': church_website
				}
			}
			
			urlencoded_json = urllib.quote( json.dumps(params) );
			response = urllib2.urlopen("%s?method=%s" %(url, method), urlencoded_json)
			data = response.read()
			response.close()
			result = json.loads(data)
			raise Exception

			return HttpResponseRedirect( reverse('thanks') )
		else:
			pass
	else:
		form = SignupForm()

	c = { 'form': form}
	return render_to_response('join/signup.html', c, context_instance=RequestContext(request))

def thanks(request):
	return render(request, 'join/thanks.html')

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
