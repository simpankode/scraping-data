from typing import Counter
from urllib import response
import tweepy
import config
import pandas as pd

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = "gojek -is:retweet"

response = client.get_recent_tweets_count(query=query, granularity="day")

for tweet in response.data:
    print(tweet)