from django import forms
from django import forms
from django.contrib.auth.models import User
from django import forms
from blog.models import Yoga
from blog.models import GYM
from blog.models import MEDITATION
from blog.models import ADVENTURE
from blog.models import PRANIC
from django.core import validators

def starts_with_d(value):
    if value[0] != 'S':
        raise forms.ValidationError('Name should starts with S')

class FeedbackForm(forms.Form):
    name=forms.CharField(max_length=64)
    age=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(20)])

class RegistrationYForm(forms.ModelForm):
    class Meta:
        model=Yoga
        fields='__all__'


class GYMForm(forms.ModelForm):
    class Meta:
        model=GYM
        fields='__all__'

class MEDITATIONForm(forms.ModelForm):
    class Meta:
        model=MEDITATION
        fields='__all__'


class ADVENTUREForm(forms.ModelForm):
    class Meta:
        model=ADVENTURE
        fields='__all__'

class PRANICForm(forms.ModelForm):
    class Meta:
        model=PRANIC
        fields='__all__'

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']

class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)
