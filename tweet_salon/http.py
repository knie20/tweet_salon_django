import requests

BASE_64_BEARER_TOKEN_CREDENTIALS = \
    'cmFia0FaeUdrMTh6bUN4SGtqODNCMFNOSTpBbmE4eUdaTDFlQXByT3k3VTdwT29sUTFRVmN0elNqc0l6M3RxNW93V0VHSmcxTEtZTA=='
OAUTH_OBTAIN_PATH = 'https://api.twitter.com/oauth2/token?grant_type=client_credentials'
USER_LOOKUP_PATH = 'https://api.twitter.com/1.1/users/lookup.json'
USER_TIMELINE_LOOKUP_PATH = 'https://api.twitter.com/1.1/statuses/user_timeline.json'


# obtain bearer token with credentials
def do_twitter_auth():
    res = requests.post(OAUTH_OBTAIN_PATH, headers={
        'Authorization': 'Basic ' + BASE_64_BEARER_TOKEN_CREDENTIALS,
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    })
    return res.json()['access_token']


# get user info from Twitter API with given handle
def get_user_by_handle(handle):
    res = requests.get(USER_LOOKUP_PATH + '?' + 'screen_name=' + handle, headers={
        'Authorization': 'Bearer ' + do_twitter_auth()
    })
    return res.json()


# get user info from Twitter API with given user id
def get_user_by_id(user_id):
    res = requests.get(USER_LOOKUP_PATH + '?' + 'screen_name=' + user_id, headers={
        'Authorization': 'Bearer ' + do_twitter_auth()
    })
    return res.json()


# get user's tweets from Twitter API with given handle and number of tweets
def get_user_timeline_by_handle(handle, count):
    res = requests.get(USER_TIMELINE_LOOKUP_PATH + '?' + 'screen_name=' + handle + '&' + 'count' + str(count), headers={
        'Authorization': 'Bearer ' + do_twitter_auth()
    })
    return res.json()
