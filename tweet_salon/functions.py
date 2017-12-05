from tweet_salon.data_access import *
from tweet_salon.http import *


# check if database has the user with the given handle
# if user exists, pull user info from database
# if user doesn't exist, pull user from API
def retrieve_user(handle):
    if db_has_user(handle):
        return fetch_user_by_handle(handle)
    else:
        user = json_user_to_model(get_user_by_handle(handle)[0])
        return user


# check if database has the user with the given handle
# if user exists, pull user's tweets from database
# if user doesn't exist, pull user's tweets from API
def retrieve_timeline(handle):
    tweets = []
    if db_has_user(handle):
        for tweet in filter_tweets(fetch_user_by_handle(handle).userId):
            tweets.append(tweet)
    else:
        for tweet in get_user_timeline_by_handle(handle, 100):
            tweets.append(json_tweet_to_model(tweet))

        persist_user(json_user_to_model(get_user_by_handle(handle)[0]), tweets)
    return tweets


# converts a json user obj to the TwitterUser class in models
def json_user_to_model(json_user):
    user = TwitterUser()
    user.userId = int(json_user['id_str'])
    user.handle = json_user['screen_name']
    user.displayName = json_user['name']
    return user


# converts a json tweet obj to the Tweet class in models
def json_tweet_to_model(json_tweet):
    tweet = Tweet()
    tweet.tweetId = int(json_tweet['id_str'])
    tweet.userId = int(json_tweet['user']['id_str'])
    tweet.createdAt = json_tweet['created_at']
    tweet.text = json_tweet['text']
    return tweet


# save a user and their timeline into the database
def persist_user(user, tweets):
    create_user(user)
    for tweet in tweets:
        create_tweet(tweet)
