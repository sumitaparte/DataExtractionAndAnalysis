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

# %a %b %d %H:%M:%S +%f %Y
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
consumer_key= '<consumer_key>'
consumer_secret= '<consumer_secret>'
access_token= '<access_token>'
access_token_secret= '<access_token_secret>'

keywords = ["Canada","University","Dalhousie University","Halifax","Canada Education"]

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


f= open("tweetText.txt","w+")
# open files and get data from search api for each keyword
with open('TwittercsvData.csv', mode='w') as TwittercsvData:
  writer = csv.writer(TwittercsvData, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  writer.writerow(['Tweet_Text', 'Location', 'Time', 'User', 'User_Location'])
  
  # running code for each keyword
  for keyword in keywords:
    tweets = tw.Cursor(api.search, q=keyword).items(600) 
    print(keyword) 
    
    # iterating over output and saving in csv and txt files
    for tweet in tweets:
      f.write("text:"+cleanData(tweet.text))
      writer.writerow([cleanData(tweet.text), (tweet.place.name if tweet.place is not None else "N/a"), tweet.created_at, cleanData(tweet.user.name), cleanData(checkNull(tweet.user.location))])
print("Done")
f.close()
