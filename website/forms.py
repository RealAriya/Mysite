from django import forms
from website.models import Contact,Newsletter
from captcha.fields import CaptchaField


class NameForm(forms.Form):
    # this name here link to name in input if you want use in html form tags
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="email")
    subject = forms.CharField(label="subject", max_length=100)
    message = forms.CharField(label="message", widget=forms.Textarea)


class Contact_Form(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'subject': forms.TextInput(attrs={'required': False}), 
        }


class newsletter_Form(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'