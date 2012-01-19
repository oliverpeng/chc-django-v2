class MC_Exception(Exception):
	def __init__(self, err_code, message):
		Exception.__init__(self, message)
		self.err_code = err_code

def list_subscribe(email_address, merge_vars={}):
	""" Subscribe to MailChimp newsletter

	"""

	import urllib, urllib2, json
	from django.conf import settings

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
			raise MC_Exception(result['code'], result['error'])
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
	send_mail(subject, message, sender, recipients)
