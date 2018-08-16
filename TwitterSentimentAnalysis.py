# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 11:52:19 2018

@author: Harsh
"""

import tweepy
from textblob import TextBlob
from tweepy import OAuthHandler

consumer_key= 'YOUR_CONSUMER_KEY'
consumer_secret= 'YOUR_CONSUMER_SECRET'

access_token='YOUR_ACCESS_TOKEN'
access_token_secret='YOUR_ACCESS_TOKEN_SECRET'
try:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
except:
    print("Error Auth Failed")
public_tweets = api.search('KEYWORD')# -*-searching for tweets with a keyword-*-
# -*-analysis of tweets for sentiment-*-
for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
print("\n")

    