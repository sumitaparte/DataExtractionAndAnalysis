import csv
import re
import requests

#cleaning data like removal of emoji,urls, special characters
def cleanData(inputString):
    inputString = re.sub(r'http\S+', ' ', inputString) # for urls, emoji
    inputString = re.sub('[^A-Za-z0-9\'"]+', ' ', inputString) # for special characters
    return inputString

#key obtained from newsAPI account
key = 'bb75b658000349b2bd6aa0e743c6ee6d'
url = 'https://newsapi.org/v2/everything?'

keywords = ["Canada","University","Halifax", "'Dalhousie University'","'Canada Education'"]

#opening and writing into csv file.
k=0
for keyword in keywords:
  print(keyword)
  parameters = {
    'q': keyword,
    'pageSize': 100,
    'apiKey': key
    }
  response = requests.get(url, params=parameters)
  # Convert the response to JSON format and pretty print it
  response_json = response.json()
  for i in response_json['articles']:
    filename= 'data_file_' + str(k) + '.txt'
    with open(filename, mode='w+', encoding='UTF-8') as newsapidata:
      dataname = 'Title: ' + str(i['title']) + ' Content: ' + str(i['content']) + ' Description: ' + str(i['description'])
      newsapidata.write(cleanData(dataname))
      k=k+1
     
print(str(k-1) + " documents generated.")    