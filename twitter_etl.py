#import the required modules
import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs 

#passing the API keys for getting data from twitter.
def run_twitter_etl():

    access_key = "" 
    access_secret = "" 
    consumer_key = ""
    consumer_secret = ""


    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)   
    auth.set_access_token(consumer_key, consumer_secret) 

    # # # Creating an API object 
    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name='@elonmusk', 
                            # 200 is the maximum allowed count
                            count=200,
                            include_rts = False,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended'
                            )

    #Actual twitter Data
    list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                        'text' : text,
                        'favorite_count' : tweet.favorite_count,
                        'retweet_count' : tweet.retweet_count,
                        'created_at' : tweet.created_at}
        
        list.append(refined_tweet)

    df = pd.DataFrame(list)
    df.to_csv('refined_tweets.csv')


import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs 

def run_twiiter_etl():
    access_key = "" 
    access_secret = "" 
    consumer_key = ""
    consumer_secret = ""


    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)   
    auth.set_access_token(consumer_key, consumer_secret) 

    # # # Creating an API object 
    api = tweepy.API(auth)
    # using get_user with screen_name
    screen_name = "elonmusk"
    user2 = api.get_user(screen_name=screen_name)

    print("user id",user2.id)
    print("user desc",user2.description)
    print("follower count",user2.followers_count)
    #print("timeline",user2.timeline)

    screen_names = ['elonmusk','iamsrk']
    list_tweet_info = []

    for each_screen_name in screen_names:
        user = api.get_user(screen_name=each_screen_name)
        tweet_dict = {
            "user_id" : user.id,
            "user_description" : user.description,
            "user_followers_count" : user.followers_count
        }
        list_tweet_info.append(tweet_dict)

    df = pd.DataFrame(list_tweet_info)
    df.to_csv('s3://nisha-airflow-twitter-project/tweets_info.csv')


        
