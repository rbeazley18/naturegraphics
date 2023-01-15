from email import message
from django.forms import ModelForm
from .models import Contact
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox 


class ContactForm(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox )
    
    class Meta:
        model = Contact
        fields = ('email', 'subject', 'message')

        
    