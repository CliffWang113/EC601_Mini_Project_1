#!/user/bin/env python

import tweepy
import json
import urllib.request
import ffmpeg
import io
import os
import subprocess
from PIL import Image
from google.cloud import vision
from google.cloud import videointelligence
from google.cloud.vision import types


consumer_key = 'Please enter your consumer key'
consumer_secret = 'Please enter your consumer secret'
access_token = 'Please enter your access token'
access_token_secret = 'please enter your access token secret'

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Please enter your Google application credential location"



def download_pics(screen_name):

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	#initialize a list to hold all the tweepy Tweets
	alltweets = []
		
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=1)

	#save most recent tweets
	alltweets.extend(new_tweets)

	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:

		#all subsequent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=10,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1

		print("...%s tweets downloaded so far" % (len(alltweets)))

		if len(alltweets) > 50:
			break
       
    #write tweet objects to JSON
	file = open('tweet.json', 'w')
	print("Writing tweet objects to JSON please wait...")
	for status in alltweets:
		json.dump(status._json,file,sort_keys = True,indent = 4)
    
    #close the file
	print("Done")
	file.close()

	pic_tweet = []
	for tweet in alltweets:
		try:
		    photo_link = tweet.entities['media'][0]['media_url']
		except (NameError, KeyError):
			pass
		else:
			pic_tweet.append(tweet.entities['media'][0]['media_url'])

	for index in range(len(pic_tweet)):
		file_name = "image_" + str(index) + '.jpg'
		urllib.request.urlretrieve(pic_tweet[index],file_name)

def making_video(video_name):
	subprocess.run(['ffmpeg', '-f', 'image2', '-i', './%*.jpg', '-r', '48', video_name + '.mp4'])

def google_vision_api(video_name):

	video_client = videointelligence.VideoIntelligenceServiceClient()
	features = [videointelligence.enums.Feature.LABEL_DETECTION]

	video_path = os.path.join('./' + '%s' %video_name + '.mp4')
	with io.open(video_path,'rb') as movie:
		input_content = movie.read()

	operation = video_client.annotate_video(features=features, input_content=input_content)
	print('\nProcessing video...')
	result = operation.result(timeout=90)
	print('\nFinished processing')

	segment_labels = result.annotation_results[0].segment_label_annotations
	for i, segment_label in enumerate(segment_labels):
		print('Video label description: {}'.format(segment_label.entity.description))
		for category_entity in segment_label.category_entities:
			print('Label category description: {}'.format(category_entity.description))


if __name__ == '__main__':

	twitt_account = '@taylornation13'
	#twitt_account = '@vangoghartist'
	download_pics(twitt_account)
	making_video(twitt_account)
	google_vision_api(twitt_account)
