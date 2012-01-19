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
