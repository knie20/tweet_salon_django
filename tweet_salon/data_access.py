from tweet_salon.models import TwitterUser, Tweet


# CRUD functions for interactions with mySQL


def create_tweet(current_tweet):
    tweet = Tweet()
    tweet.tweetId = current_tweet.tweetId
    tweet.userId = current_tweet.userId
    tweet.createdAt = current_tweet.createdAt
    tweet.text = current_tweet.text
    tweet.save()


def fetch_tweet_by_id(tweetId):
    return Tweet.objects.get(tweetId__exact=tweetId)


def filter_tweets(user_id):
    return Tweet.objects.filter(user_id__exact=user_id)


def update_tweet(tweet_id, **kwargs):
    tweet = Tweet.objects.get(tweet_id)
    tweet.text = kwargs.get("text")
    tweet.save()


def delete_tweet(tweet_id):
    Tweet.objects.get(tweet_id).delete()


def db_has_tweet(tweet_id):
    return Tweet.objects.filter(tweetId__exact=tweet_id).exists()


def create_user(current_user):
    user = TwitterUser()
    user.userId = current_user.userId
    user.handle = current_user.handle
    user.displayName = current_user.displayName
    user.save()


def fetch_user_by_id(user_id):
    return TwitterUser.objects.get(userId__exact=user_id)


def fetch_user_by_handle(handle):
    return TwitterUser.objects.get(handle__exact=handle)


def update_user(user_id, **kwargs):
    user = TwitterUser.objects.get(user_id)
    user.userId = kwargs.get('userId')
    user.handle = kwargs.get('handle')
    user.displayName = kwargs.get('displayName')
    user.save()


def delete_user(user_id):
    TwitterUser.objects.get(user_id).delete()


def db_has_user(handle):
    return TwitterUser.objects.filter(handle__exact=handle).exists()
