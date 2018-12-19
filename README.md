# EC601_Mini_Project_1
This project is implemented for Boston University, EC601 Mini Project #1. The goal of this Mini Porject is to get familiar with the APIs. The functions includes:

* Download images from the designate twitter account timeline.
* Convert the images into a video.
* Analysis the content of the video and generate a label for the video.

## APIs

* [Tweepy](http://www.tweepy.org/) - An easy-to-use Python library for accessing the Twitter API.
* [FFmpeg](https://www.ffmpeg.org/) - A complete, cross-platform solution to record, convert and stream audio and video.
* [Google Cloud Video Intelligence](https://cloud.google.com/video-intelligence/) - Search and discover media content with Google Video Intelligence.

## Get Started

* Enter your keys for your twitter's developer account at here:

```
consumer_key = 'Please enter your consumer key'
consumer_secret = 'Please enter your consumer secret'
access_token = 'Please enter your access token'
access_token_secret = 'please enter your access token secret'
```

* Enter your Google Application Credintial's location at here:

```
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "Please enter your Google application credential location"
```

## Results

* The images are downloaded from the twitter account "@vangoghartist". Here are two sample images:
<img src="https://github.com/CliffWang113/EC601_Mini_Project_1/blob/master/image_0.jpg" height="250"><img src="https://github.com/CliffWang113/EC601_Mini_Project_1/blob/master/image_1.jpg" height="250">

* The label generated after analysis is：

```
art
```

## Authors

* **Chunpeng WANG** - *Initial work* - [CliffWang113](https://github.com/CliffWang113)
