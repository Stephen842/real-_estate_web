from django import forms
from .models import Contact, Newsletter, Property


class CommentForm(forms.Form):
    author = forms.CharField(
                max_length = 100,
                widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            )

    body = forms.CharField(
            widget = forms.Textarea(attrs = {'class': 'form-control', 'placeholder': 'Leave a comment'}),
            )

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'