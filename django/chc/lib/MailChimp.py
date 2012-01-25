from django.conf import settings

class MC_Exception(Exception):
	def __init__(self, err_code, message):
		Exception.__init__(self, message)
		self.err_code = err_code

def list_subscribe(email_address, merge_vars={}):
	""" Subscribe to MailChimp newsletter

	"""

	import urllib, urllib2, json

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

def email_notify(is_pastor, contact_me, take_offering, fname, lname, church_name, city, state, country, church_website, phone, email):
	""" Email admin notifying if subscriber meets any of these criteria: is_pastor, contact_me, take_offering

	"""

	from django.core.mail import send_mail
	subject = "CHC web subscription needs attention"

	alerts = []
	if is_pastor:
		alerts.append("I am a pastor")
	if contact_me:
		alerts.append("I am interested. Please contact me.")
	if take_offering:
		alerts.append("Our church will take an offering at the next crisis.")

	message = u"""A form submission has been processed. Please check that the user is listed in MailChimp before contacting him/her.
It is possible they may not have confirmed their sign up via their confirmation email.

The user checked yes to the following options:
%s

First Name: %s
Last Name: %s
City: %s
State: %s
Country: %s

Church: %s
Website: %s

Phone: %s
Email: %s""" % ('\n'.join(alerts), fname, lname, city, state, country, church_name, church_website, phone, email) 
	sender = 'churcheshelpingchurches@gmail.com'
	recipients = settings.SUBSCRIPTION_NOTIFICATIONS
	send_mail(subject, message, sender, recipients)
