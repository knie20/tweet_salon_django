from django.shortcuts import render
from django.http import HttpResponseRedirect
from tweet_salon.functions import *
from tweet_salon.forms import MainForm
from django.forms.models import model_to_dict


def index(req):
    form = MainForm(req.POST)
    return render(req, 'index.html', {'form': form})


def go_to_user(req):
    if req.method == 'POST':
        handle = req.POST.get('handle')
        twitter_user = retrieve_user(handle)
        # store user info into session as dict
        req.session['twitter_user'] = model_to_dict(twitter_user)
        # redirect to user page
        return HttpResponseRedirect('/user/' + handle)


def user(req):
    # get user info from session, where go_to_user has stored them
    twitter_user = req.session.get('twitter_user')
    # now that user's info is known, get user's tweets
    user_timeline = retrieve_timeline(twitter_user.get('handle'))
    return render(req, 'user.html', {'twitter_user': twitter_user, 'user_timeline': user_timeline})
