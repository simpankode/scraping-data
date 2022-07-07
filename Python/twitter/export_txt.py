from urllib import response
import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN)

query = "gojek -is:retweet"

file_name = "tweets.txt"

with open(file_name, "a+") as filehandler:
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100, tweet_fields=["created_at", "lang"], expansions=["author_id"]).flatten(limit=1000):
            filehandler.write('%s\n' % tweet.author_id)
            filehandler.write('%s\n' % tweet.created_at)
            filehandler.write('%s\n' % tweet.lang)
            filehandler.write('%s\n' % tweet.text)
            filehandler.write('\n')

