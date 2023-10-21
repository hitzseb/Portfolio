from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email_address = forms.EmailField()
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
