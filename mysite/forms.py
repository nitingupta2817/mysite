from django import forms

class UserForm(forms.Form):
    num1 = forms.IntegerField(label='Number 1')
    num2 = forms.IntegerField(label='Number 2')

