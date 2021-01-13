import tweepy
from tweepy import OAuthHandler

consumer_key = #
consumer_secret = #
access_token = #
access_secret = #

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

name = 'nytimes'
tweetcount = 5

results = api.user_timeline(id=name , count = tweetcount)

for tweet in results:
    print(tweet.text, "\n")
