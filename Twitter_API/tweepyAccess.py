import tweepy
from tweepy import OAuthHandler
import csv
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS
import pika
import json

consumer_key="N2oXB2loL73OQ87R7yQ50Dicu"
consumer_secret="LlrU3ZuuoMWaGIFNNDkdLnyUrKSOZSk8x8DLKsPYA5omVXQUo6"
access_key="1238352975132626944-BfCcBHGNpgELefKXTEiwEHHigQ03ec"
access_secret="c4E5Mgo7HrY85dXG7wpeYnS5Mow0ZtsMVNXFkkoddT1ZJ"

@app.route("/tweepyAccess", methods=['POST'])
def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
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

	#write the csv	
	with open('../Restaurant_UI/%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["text"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("cupcakeg1t8")
	app.run(port=5000, debug=True)

