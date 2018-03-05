import os
import tweepy
from creds import * #Custom file containing your private Twitter Credentials 

def tweet(message):
    auth = tweepy.OAuthHandler(CON_KEY, CON_SECRET)
    auth.set_access_token(AUTH_TOKEN, AUTH_TOKEN_SECRET)
    api = tweepy.API(auth)
    api.update_status(message)

#Put any message you want to be tweeted 
tweet('INSERT_TWEET')    