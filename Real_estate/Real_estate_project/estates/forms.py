from django import forms
from .models import Contact, Newsletter, Property, PropertyContact


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
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter message'}),
        }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Subscribe mail'}),
        }
  
 #this below works for the administrative uploading of properties       
class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
#this below works for clients to show interest in the listing details page
class PropertyContactForm(forms.ModelForm):
    class Meta:
        model = PropertyContact
        fields = '__all__'