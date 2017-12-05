from django import forms


class MainForm(forms.Form):
    handle = forms.CharField(max_length=15)
