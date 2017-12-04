from django import forms


class MainForm(forms.Form):
    handle = forms.CharField(label='handle', max_length=15)