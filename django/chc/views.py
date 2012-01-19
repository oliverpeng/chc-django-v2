from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext


def home(request):
	return render(request, 'home.html')

def join(request):
	from lib.Forms import SubscribeForm

	form = SubscribeForm()
	c = { 'form': form }
	return render_to_response('join/index.html', c, context_instance=RequestContext(request))

def subscribe(request):
	from lib.Forms import SubscribeForm
	import lib.MailChimp as MailChimp
	error_msgs = []

	if request.method == 'POST':
		form = SubscribeForm(request.POST)
		if form.is_valid():
			try:
				email = form.cleaned_data['email']
				merge_vars = {
					'GROUPINGS': [{'id': 705, 'groups': 'Subscribe to newsletter.'}]
				}
				MailChimp.list_subscribe(email, merge_vars)
				return HttpResponseRedirect( reverse('subscribe_thanks') )
			except MailChimp.MC_Exception as e:
				if e.err_code == 214: # user already subscribed
					request.session['signup.is_duplicate'] = True
					request.session['signup.email'] = form.cleaned_data['email']
					request.session['signup.mailchimp_link'] = MailChimp.extract_href(e.message)

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
	from lib.Forms import SignupForm
	import lib.MailChimp as MailChimp
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
				MailChimp.list_subscribe(email, merge_vars)

				if is_pastor:
					MailChimp.email_pastor_subscribed(fname=fname, lname=lname, church_name=church_name,
						city=city, state=state, country=country, church_website=church_website,
						phone=phone, email=email)
				return HttpResponseRedirect( reverse('thanks') )
			except MailChimp.MC_Exception as e:
				if e.err_code == 214: # User already subscribed
					request.session['signup.is_duplicate'] = True
					request.session['signup.email'] = form.cleaned_data['email']
					request.session['signup.mailchimp_link'] = MailChimp.extract_href(e.message)
					
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
