from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import re

#consumer key, consumer secret, access token, access secret.
consumer_key= 'EuW9HwrY1ublqrgmDWI1emzj4'
consumer_secret= 'D5YmwcZwZXwTBTNjXkCieRnZUAGOb67KTN372EMqWOpn29Jnu1'
access_token= '2563114477-09WupIuie5i7Agz74UHN9vhvgSzuT0Xytp4OpeA'
access_token_secret= 'B7bt0XiEyzRiNI4AU5v3o8rlwzLeAF5QaAlIT4ezy5jds'

def cleanData(inputString):
    inputString = inputString.encode('ascii', 'ignore').decode('ascii') # for emoji
    inputString = re.sub(r'http\S+', '', inputString) # for urls
    inputString = re.sub('[^A-Za-z0-9\.\,\'"]+', ' ', inputString) # for special characters
    return inputString

def tryreTweet(value1):
  try:
    retweet = cleanData(value1["retweeted_status"]["text"])
  except KeyError: 
    retweet = "Nan"
  return retweet

f1= open("streamerAPI.txt","w+")
    
class listener(StreamListener):
  def on_data(self, data):
   
    all_tweets = json.loads(data)
    
    # clean and save data in variable
    tweet_text = cleanData(all_tweets["text"])
    location = all_tweets["place"]["name"] if all_tweets["place"] is not None else 'Nan'
    user = cleanData(all_tweets["user"]["name"])
    user_location = cleanData(all_tweets["user"]["location"] if all_tweets["user"]["location"] is not None else 'Nan')
    created_at = all_tweets["created_at"]
    retweet_count = all_tweets["retweet_count"]
    retweet = tryreTweet(all_tweets)
    
    # write into csv and txt files
    f1.write("text:"+tweet_text)

    writer.writerow([tweet_text, location, created_at, user, user_location, retweet_count, retweet])
    return(True)

  def on_error(self, status):
      print("ERROR in here!")
      print (status)
      

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

with open('mongoDbStreamData.csv', 'w') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(['tweet_text', 'Location', 'Created_at', 'User', 'UserLocation', 'retweet_count', 'retweet'])
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=["Canada, University, Dalhousie University, Halifax, Canada Education"])