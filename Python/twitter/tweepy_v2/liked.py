from urllib import response
import tweepy
import config
import pandas as pd

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

user_id = 2244994945

response = client.get_liked_tweets(user_id, max_results=100, tweet_fields=["created_at"])

columns = ["author_id", "created_at"]
data = []
for tweet in response.data: 
    data.append([tweet.id, tweet.created_at])


df = pd.DataFrame(data, columns=columns)

df.to_csv('liked.csv')