# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:06:56 2019

@author: Erick
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
    
    
#from twython import Twython
#from twython import TwythonStreamer 
#import json as json



 
"""

#INTERVAL = 60 * 60 * .5  # update every 30 mins
INTERVAL = 15  # every 15 seconds, for testing

# Keys have been regenerated
APP_KEY = "XX"
APP_SECRET = "XX"
OAUTH_TOKEN = "XX" 
OAUTH_TOKEN_SECRET = "XX"

"""
#auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
#api = tweepy.API(auth)
"""
twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

all_data = []
#search = twitter.search(q='Flightscope', count=10) # Just pulled first tweet as data is long
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            all_data.append(data)
            print(data['text'])
            try:
                print(data['user']['name'])
            except:
                print('Username unavailable')
            try:
                print(data['user']['screen_name'])
            except:
                print('Screen name unavailable')
            try:
                print(data['entities']['urls'][0]['url'])
            except:
                try:
                    print(data['retweeted_status']['entities']['urls'][0]['url'])
                except:
                    try:
                        print(data['entities']['media'][0]['display_url'])
                    except:
                        try:
                            print(data['quoted_status_permalink']['url'])
                        except:
                            print('URL unavailable')
                        
    def on_error(self, status_code, data):
        print(status_code)

stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
count = 0
go = True

#while True:
results = []
while go:
    print("about to search Twitter...")
    #ad = get_ad()
    #api.update_status(ad)
    #search = twitter.search(q='Flightscope', count=10)
    
    #search = twitter.cursor(twitter.search, q='Flightscope')
    #for result in search:
        #results.append(result)
    stream.statuses.filter(track='Baseball')
    time.sleep(INTERVAL)
    count += 1
    if count >= 1:
        go = False
"""