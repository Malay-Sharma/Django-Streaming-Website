from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = ' col-md-4 '
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = ''

		self.fields['first_name'].widget.attrs['class'] = ' col-md-4 '
		self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
		self.fields['first_name'].label = ''
		self.fields['first_name'].help_text = ''

		self.fields['last_name'].widget.attrs['class'] = ' col-md-4 '
		self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
		self.fields['last_name'].label = ''
		self.fields['last_name'].help_text = ''

		self.fields['email'].widget.attrs['class'] = ' col-md-4 '
		self.fields['email'].widget.attrs['placeholder'] = 'User Email'
		self.fields['email'].label = ''
		self.fields['email'].help_text = ''

		self.fields['password1'].widget.attrs['class'] = ' col-md-4 '
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = ''

		self.fields['password2'].widget.attrs['class'] = ' col-md-4 '
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = ''