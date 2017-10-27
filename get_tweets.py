import tweepy
import ConfigParser
import sys
from pprint import pprint

Config = ConfigParser.ConfigParser()
Config.read("config.ini")
auth = tweepy.OAuthHandler(Config.get("twitter", "api_key") , Config.get("twitter", "api_secret") )
auth.set_access_token(Config.get("twitter", "access_token"), Config.get("twitter", "access_token_secret"))
api = tweepy.API(auth)

tuitero=sys.argv[1]
print "Extracting " + tuitero + "'s tweets"
tuitero_file = open("original_tweets/"+tuitero+".txt", 'w')


tweets = api.user_timeline(screen_name=tuitero, count=sys.argv[2])
tweets_string = ""
for tweet in tweets:
    if not hasattr(tweet, 'retweeted_status'):
        tweets_string += tweet.text + "\n-----\n"
 
tuitero_file.write(tweets_string.encode('utf8'))
