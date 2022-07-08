from urllib import response
import tweepy
import config
import pandas as pd

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

tweet_id = 1460323737035677698

response = client.get_liking_users(tweet_id, user_fields=["profile_image_url"])

columns = ["username", "profile_image_url"]
data = []
for tweet in response.data: 
    data.append([tweet.username, tweet.profile_image_url])


df = pd.DataFrame(data, columns=columns)

df.to_csv('liking.csv')