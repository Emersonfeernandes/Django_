from django import forms

class UserForm(forms.Form):
    filme1 = forms.CharField(max_length=30)
    filme2 = forms.CharField(max_length=30)
    filme3 = forms.CharField(max_length=30)
    filme4 = forms.CharField(max_length=30)
    filme5 = forms.CharField(max_length=30)
