from django import forms


# form used on index.html
class MainForm(forms.Form):
    handle = forms.CharField(max_length=15, label='@')
