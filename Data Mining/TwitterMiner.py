import tweepy
from tweepy import OAuthHandler

consumer_key = '0QVZp8SyuB46PieJH5o8En5Xj'
consumer_secret = 'NhXvOGa9k6nm34FMdUzfUTu0tdMM10VzfybQ99QCsQJ7Sz0N3W'
access_token = '67682537-3APG0D5HbVOB2qJ0IoJVrtqCfE8GCM3owYBpZ5o9L'
access_secret = 'LPM6dLg6h9gQy8Mg4lQRM96aDoLAzjSq88G8ZxeLkNlvZ'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

name = 'nytimes'
tweetcount = 5

results = api.user_timeline(id=name , count = tweetcount)

for tweet in results:
    print(tweet.text, "\n")