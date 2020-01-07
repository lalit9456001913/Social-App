from django import forms
from twitter.models import Post,Liked,Dislike
from django.contrib.auth.models import User
class User_form(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control',
                'placeholder':'Enter User Name'}
    ),required=True,max_length=20)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'form-control',
               'placeholder': 'Enter Mail Id'}
    ), required=True, max_length=20)
    first_name=forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Enter First Name'}
    ),required=True,max_length=20)
    last_name=forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Enter Lasr Name'}
    ),required=True,max_length=20)
    password = forms.CharField(widget=forms.PasswordInput(), required=True, max_length=20)
    confirm_password=forms.CharField(widget=forms.PasswordInput(),required=True,max_length=20)

    class Meta():
        model=User
        fields=['username','email','first_name','last_name','password']

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('title','text',)

class LikedForm(forms.ModelForm):
    class Meta:
        model=Liked
        fields=('post_id',)

class DislikeForm(forms.ModelForm):
    class Meta:
        model=Dislike
        fields=('post_id',)