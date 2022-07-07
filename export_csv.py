from urllib import response
import tweepy
import config
import pandas as pd

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = "gojek -is:retweet"

response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=["created_at", "lang"], expansions=["author_id"])

columns = ["author_id", "created_at", "lang",  "tweet"]
data = []
for tweet in response.data: 
    data.append([tweet.author_id, tweet.created_at, tweet.lang, tweet.text])

df = pd.DataFrame(data, columns=columns)

df.to_csv('tweets.csv')