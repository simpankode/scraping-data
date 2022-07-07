from urllib import response
import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = "gojek -is:retweet"

response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=["created_at", "lang"], expansions=["author_id"])

for tweet in response.data:
    print(tweet.author_id, tweet.created_at, tweet.lang)
    print(tweet.text)
    print("\n")