from django import forms
from django import forms
from django.contrib.auth.models import User
from django import forms
from testapp.models import Yoga
from testapp.models import GYM
from testapp.models import MEDITATION
from testapp.models import ADVENTURE

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


class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','first_name','last_name','email']

class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)
