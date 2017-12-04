from tweet_salon.models import TwitterUser, Tweet


def create_tweet(**kwargs):
    tweet = Tweet()
    tweet.tweetId = kwargs.get('tweetId')
    tweet.userId = kwargs.get('userId')
    tweet.createdAt = kwargs.get('createdAt')
    tweet.text = kwargs.get('text')
    tweet.save()


def get_tweet_by_id(tweetId):
    return Tweet.objects.get(tweetId__exact=tweetId)


def filter_tweet(**kwargs):
    return Tweet.objects.filter(**kwargs)


def update_tweet(tweetId, **kwargs):
    tweet = Tweet.objects.get(tweetId)
    tweet.text = kwargs.get("text")
    tweet.save()


def delete_tweet(tweetId):
    Tweet.objects.get(tweetId).delete()
