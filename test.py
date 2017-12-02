import random
import tweepy
import datetime
from credentials import *
from tweet import *
from alltweets import at



def PostTweet(t):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_with_media(t.imageName, t.status)


tw = random.choice(at)
if datetime.datetime.today().weekday() == 5:
    tw.status += " #screenshotsaturday"
printTweetToConsole(tw)
PostTweet(tw)
