import re
import tweepy as tw 
import datetime
import csv

def cleanData(inputString):
    inputString = re.sub(r'http\S+', '', inputString) # for urls
    inputString = re.sub('[^A-Za-z0-9\.\,\'"]+', ' ', inputString) # for special characters
    return inputString
    
def checkNull(value):
  return (value if value != "" else "Nan")

def convert_timestamp(date_object): 
  date_object = date_object.strftime('%c')
  return date_object

def tryreTweet(value1):
  try:
    retweet = cleanData(value1.retweeted_status.text)
  except AttributeError: 
    retweet = "Nan"
  return retweet

#consumer key, consumer secret, access token, access secret.
consumer_key= 'EuW9HwrY1ublqrgmDWI1emzj4'
consumer_secret= 'D5YmwcZwZXwTBTNjXkCieRnZUAGOb67KTN372EMqWOpn29Jnu1'
access_token= '2563114477-09WupIuie5i7Agz74UHN9vhvgSzuT0Xytp4OpeA'
access_token_secret= 'B7bt0XiEyzRiNI4AU5v3o8rlwzLeAF5QaAlIT4ezy5jds'

keywords = ["Canada","University","'Dalhousie University'","Halifax","'Canada Education'"]

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# open files and get data from search api for each keyword
f= open("tweetText.txt","w+")

# running code for each keyword
for keyword in keywords:
  tweets = tw.Cursor(api.search, q=keyword).items(200) 
  print(keyword) 
  
  # iterating over output and saving in csv and txt files
  for tweet in tweets:
    f.write("text:"+cleanData(tweet.text))
print("Done")
f.close()