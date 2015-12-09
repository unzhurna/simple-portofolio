from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
