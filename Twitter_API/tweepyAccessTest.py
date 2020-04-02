import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
import mysql.connector
from mysql.connector import errorcode
import time
import json
from tweepy import OAuthHandler
import csv
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/esm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Tweets_Table(db.Model):

	__tablename__ = 'tweets2'
	tweets = db.Column(db.String(200))
	id = db.Column(db.Integer, primary_key = True)


ckey="N2oXB2loL73OQ87R7yQ50Dicu"
csecret="LlrU3ZuuoMWaGIFNNDkdLnyUrKSOZSk8x8DLKsPYA5omVXQUo6"
atoken="1238352975132626944-BfCcBHGNpgELefKXTEiwEHHigQ03ec"
asecret="c4E5Mgo7HrY85dXG7wpeYnS5Mow0ZtsMVNXFkkoddT1ZJ"

def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = 'cupcakeg1t8',count=20)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print("getting tweets before %s" % (oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=20,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print("...%s tweets downloaded so far" % (len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	| you can comment out data you don't need
	outtweets = [[tweet.text.encode("utf-8"),] for tweet in alltweets]

	listofthings = []
	for tweets in outtweets:
		for tweet in tweets:
			newtwt = tweet.decode('utf-8')
			asd = Tweets_Table(tweets=newtwt)
		

			db.session.add(asd)
			db.session.commit()




if __name__ == '__main__':
	while True:
		get_all_tweets("cupcakeg1t8")
		time.sleep(1800)
		#  30 mins
 