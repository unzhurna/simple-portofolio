from django import forms

class ContactForm(forms.Form):
    fullname = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)
