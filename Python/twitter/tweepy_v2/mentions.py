from urllib import response
import tweepy
import config
import pandas as pd

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

user_id = 2244994945

response = client.get_users_mentions(user_id, max_results=100)

columns = ["author_id", "mentions"]
data = []
for tweet in response.data: 
    data.append([tweet.id, tweet.text])


df = pd.DataFrame(data, columns=columns)

df.to_csv('mentions.csv')