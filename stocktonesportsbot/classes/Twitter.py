# In order to use thee Twitter API you must create a Twitter account, apply for a developer account
# (just fill out some questions about what you are doing), and then create an application to obtain
# the API Key API Secret

import tweepy
import time
import os

class TweetData:

    def __init__(self):
        # Twitter api key, this connects tweepy to the Twitter API using your API key
        self.auth = tweepy.OAuthHandler(os.environ["TWITTER_API_KEY"], os.environ["TWITTER_API_SECRET"])
        self.api = tweepy.API(self.auth)

    def tweet_dates(self):
        # Gets all tweets (MAX last 3200?) for a user
        tweets = tweepy.Cursor(self.api.user_timeline, screen_name='@StocktonEsports', tweet_mode="extended").items()
        tweets2 = []
        # Cycles through the iteration object and adds it to a list that we can manipulate
        while True:
            try:
                tweet = next(tweets)
            except tweepy.TweepError:
                time.sleep(60 * 15)
                tweet = next(tweets)
            except StopIteration:
                break
            tweets2.append(tweet)
        # Empty Array
        tmp = []
        # create array of tweet information: username,
        # tweet id, date/time, text (In this case we get when it was created)
        # create a new array that holds the date stamps for when each tweet was created
        tweets_for_csv = [tweet.created_at for tweet in tweets2]  # CSV file created
        for j in tweets_for_csv:
            # Appending tweets to the empty array tmp
            tmp.append(j)

        # Return the list of dates for when tweets were created
        return tmp
