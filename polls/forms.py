from django import forms

class NameForm(forms.Form):
	
    name = forms.CharField(label='hung', max_length=100)

class LoginForm(forms.Form):

	username = forms.CharField(label='Username', max_length=100)
	password = forms.CharField(label='Password', max_length=100)

class RegistrationForm(forms.Form):

	firstName = forms.CharField(label='firstName', max_length=100)
	midName = forms.CharField(label='midName', max_length=100)
	lastName = forms.CharField(label='lastName', max_length=100)
	email = forms.CharField(label='email', max_length=100)
	dateOfBirth = forms.CharField(label='dateOfBirth', max_length=100)
	phoneNumber = forms.CharField(label='phoneNumber', max_length=100)
	username = forms.CharField(label='username', max_length=100)
	password = forms.CharField(label='password', max_length=100)