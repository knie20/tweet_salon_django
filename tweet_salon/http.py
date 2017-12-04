import requests

BASE_64_BEARER_TOKEN_CREDENTIALS = \
    'cmFia0FaeUdrMTh6bUN4SGtqODNCMFNOSTpBbmE4eUdaTDFlQXByT3k3VTdwT29sUTFRVmN0elNqc0l6M3RxNW93V0VHSmcxTEtZTA=='
OAUTH_OBTAIN_PATH = 'https://api.twitter.com/oauth2/token?grant_type=client_credentials'
USER_LOOKUP_PATH = 'https://api.twitter.com/1.1/users/lookup.json'


def do_twitter_auth():
    res = requests.post(OAUTH_OBTAIN_PATH, headers={
        'Authorization': 'Basic ' + BASE_64_BEARER_TOKEN_CREDENTIALS,
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    })
    return res.json()['access_token']


def get_user_by_handle(handle):
    res = requests.get(USER_LOOKUP_PATH + '?' + 'screen_name=' + handle, headers={
        'Authorization': 'Bearer ' + do_twitter_auth()
    })
    return res.json()


def get_user_by_id(user_id):
    res = requests.get(USER_LOOKUP_PATH + '?' + 'screen_name=' + user_id, headers={
        'Authorization': 'Bearer ' + do_twitter_auth()
    })
    return res.json()