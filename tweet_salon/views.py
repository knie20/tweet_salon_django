# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from tweet_salon.functions import *
from tweet_salon.forms import MainForm
from django.forms.models import model_to_dict


def index(req):
    form = MainForm(req.POST)
    return render(req, 'index.html', {'form': form})


@require_http_methods(['POST'])
def go_to_user(req):
    if req.method == 'POST':
        handle = req.POST.get('handle')
        twitter_user = retrieve_user(handle)
        req.session['twitter_user'] = model_to_dict(twitter_user)
        return HttpResponseRedirect('/user/' + handle)


def user(req):
    twitter_user = req.session.get('twitter_user')
    user_timeline = retrieve_timeline(twitter_user.get('handle'))
    user_model = TwitterUser()
    user_model.userId = twitter_user.get('userId')
    user_model.handle = twitter_user.get('handle')
    user_model.displayName = twitter_user.get('displayName')
    persist_user(user_model, user_timeline)
    return render(req, 'user.html', {'twitter_user': twitter_user, 'user_timeline': user_timeline})
