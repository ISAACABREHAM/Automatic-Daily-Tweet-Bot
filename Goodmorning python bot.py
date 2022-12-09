import tweepy
import schedule
import time
import keys

# *NOTE*  Import all api keys from a seperate script rather than writng them out in script (for security)

# I used terminal to download schedule and time modules because my original bot just tweeted from python. Now i'm setting a time and date to auto tweet 




# Authenticate with Twitter using OAuthHandler instance method

auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

# Define the tweet message
tweet_message = "Good Afternoon World!"

# Schedule the tweet to be sent every day at 8 AM
def tweet():
    api.update_status(tweet_message)

schedule.every().day.at("08:00").do(tweet)

while True:
    schedule.run_pending()
    time.sleep(1)
