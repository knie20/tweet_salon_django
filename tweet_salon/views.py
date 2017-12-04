# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from tweet_salon.http import *
from tweet_salon.forms import MainForm


def index(req):
    return render(req, 'index.html')


def go_to_user(req):
    if req.method == 'POST':
        form = MainForm(req.POST)
        if form.is_valid():
            return HttpResponseRedirect('/user/' + form.handle)


