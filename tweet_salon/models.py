from django.db import models


# models used for passing data


class Tweet(models.Model):
    tweetId = models.BigIntegerField(unique=True, default=0)
    userId = models.BigIntegerField(default=0)
    text = models.CharField(max_length=400)
    createdAt = models.CharField(max_length=40)

    def __str__(self):
        return "%s %s %s %s" % (self.tweetId, self.userId, self.text, self.createdAt)


class TwitterUser(models.Model):
    userId = models.BigIntegerField(unique=True, default=0)
    handle = models.CharField(unique=True, max_length=15)
    displayName = models.CharField(max_length=75)

    def __str__(self):
        return "%s %s %s" % (self.userId, self.handle, self.displayName)

