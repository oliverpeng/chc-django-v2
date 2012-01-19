from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django import forms

class SignupForm(forms.Form):
	fname = forms.CharField(label='First Name')
	lname = forms.CharField(label='Last Name')
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
	receive_updates = forms.BooleanField(required=False, label="I would like to receive updates.", initial=True)

	def clean(self):
		cleaned_data = self.cleaned_data
		church_name = cleaned_data.get('church_name')
		is_pastor = cleaned_data.get('is_pastor')
		if is_pastor and not church_name:
			raise forms.ValidationError('Please enter a church name if you are a pastor')
		return cleaned_data

class SubscribeForm(forms.Form):
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email Address'}))

class MailChimpException(Exception):
	def __init__(self, err_code, message):
		Exception.__init__(self, message)
		self.err_code = err_code

def mailchimp_subscribe(email_address, merge_vars={}):
	""" Subscribe to MailChimp newsletter

	"""

	import urllib, urllib2, json, settings

	url = 'http://us1.api.mailchimp.com/1.3/'
	method = 'listSubscribe'
	params = {
		'apikey': settings.MC_API_KEY,
		'id': settings.MC_LIST_ID,
		'email_address': email_address,
		'merge_vars': merge_vars
	}

	urlencoded_json = urllib.quote( json.dumps(params) );
	response = urllib2.urlopen("%s?method=%s" %(url, method), urlencoded_json)
	data = response.read()
	response.close()
	result = json.loads(data)

	try:
		if 'error' in result:
			raise MailChimpException(result['code'], result['error'])
	except TypeError:
		# thrown when results is not iterable (eg bool)
		pass

	return result

def extract_href(err_msg):
	""" Specialized function for extracting out href attribute from a MailChimp 214 error message

	"""

	import re
	match = re.search(r'href=[\'"]?([^\'" >]+)', err_msg)
	href = match.group(1) if match else ''
	return href

def email_pastor_subscribed(fname, lname, church_name, city, state, country, church_website, phone, email):
	""" Email admin notifying that a pastor signed up

	"""

	from django.core.mail import send_mail
	import textwrap
	subject = "Pastor %s %s of %s has signed up" %(fname, lname, church_name)
	message = u"""A form submission has been processed. Please check that the user is listed in MailChimp before contacting him/her.
It is possible they may not have confirmed their sign up via their confirmation email.

First Name: %s
Last Name: %s
City: %s
State: %s
Country: %s

Church: %s
Website: %s

Phone: %s
Email: %s""" % (fname, lname, city, state, country, church_name, church_website, phone, email) 
	sender = 'oliverpeng@gmail.com'
	recipients = ['oliverpeng@gmail.com']
	send_mail(subject, textwrap.dedent(message), sender, recipients)

# =============================================================================
#  Views
# =============================================================================

def home(request):
	return render(request, 'home.html')

def join(request):
	form = SubscribeForm()
	c = { 'form': form }
	return render_to_response('join/index.html', c, context_instance=RequestContext(request))

def subscribe(request):
	error_msgs = []

	if request.method == 'POST':
		form = SubscribeForm(request.POST)
		if form.is_valid():
			try:
				email = form.cleaned_data['email']
				merge_vars = {
					'GROUPINGS': [{'id': 705, 'groups': 'Subscribe to newsletter.'}]
				}
				mailchimp_subscribe(email, merge_vars)
				return HttpResponseRedirect( reverse('subscribe_thanks') )
			except MailChimpException as e:
				if e.err_code == 214: # user already subscribed
					request.session['signup.is_duplicate'] = True
					request.session['signup.email'] = form.cleaned_data['email']
					request.session['signup.mailchimp_link'] = extract_href(e.message)

					return HttpResponseRedirect( reverse('subscribe_thanks') )
				else:
					error_msgs.append("Oops! It looks like an error occurred. Please try again!")
			pass
		else:
			pass
	else:
		form = SubscribeForm()

	c = { 'form': form, 'error_msgs': error_msgs }
	return render_to_response('join/subscribe.html', c, context_instance=RequestContext(request))

def signup(request):
	error_msgs = []

	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			try:
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
				is_pastor = form.cleaned_data['is_pastor']
				contact_me = form.cleaned_data['contact_me']
				take_offering = form.cleaned_data['take_offering']
				contact_me = form.cleaned_data['contact_me']
				receive_updates = form.cleaned_data['receive_updates']

				groupings = []
				groups_705 = []
				if is_pastor:
					groupings.append({'id': 707, 'groups': 'Yes'})
				
				if take_offering:
					groups_705.append('Our church will take an offering at the next crisis.')
				if contact_me:
					groups_705.append('Please contact me.')
				if receive_updates:
					groups_705.append('Subscribe to newsletter.')
				
				groupings.append({'id': 705, 'groups': ','.join(groups_705)})

				merge_vars = {
					'FNAME': fname,
					'LNAME': lname,
					'CITY': city,
					'STATE': state,
					'COUNTRY': country,
					'PHONE': phone,
					'CHURCH': church_name,
					'WEBSITE': church_website,
					'GROUPINGS': groupings
				}
				mailchimp_subscribe(email, merge_vars)

				if is_pastor:
					email_pastor_subscribed(fname=fname, lname=lname, church_name=church_name,
						city=city, state=state, country=country, church_website=church_website,
						phone=phone, email=email)
				return HttpResponseRedirect( reverse('thanks') )
			except MailChimpException as e:
				if e.err_code == 214: # User already subscribed
					request.session['signup.is_duplicate'] = True
					request.session['signup.email'] = form.cleaned_data['email']
					request.session['signup.mailchimp_link'] = extract_href(e.message)
					
					return HttpResponseRedirect( reverse('thanks') )
				else:
					error_msgs.append("Oops! It looks like an error occurred. Please try again!")
		else:
			pass
	else:
		form = SignupForm()

	c = { 'form': form, 'error_msgs': error_msgs }
	return render_to_response('join/signup.html', c, context_instance=RequestContext(request))

def thanks(request):
	c = {}
	c['is_duplicate'] = request.session.get('signup.is_duplicate', False)
	c['email'] = request.session.get('signup.email', 'your email')
	c['mailchimp_link'] = request.session.get('signup.mailchimp_link', '')

	try:
		del request.session['signup.is_duplicate']
		del request.session['signup.email']
		del request.session['signup.mailchimp_link']
	except KeyError:
		pass

	return render(request, 'join/thanks.html', c)

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
