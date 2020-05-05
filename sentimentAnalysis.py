import csv
   
positiveWordList=[]
negativeWordList=[]
tweet_data =[]
data_list=[]
positive_word_count={}
negative_word_count={}

with open('positive-words.txt') as posword:
  positiveWordList = [pos.strip() for pos in posword.readlines()]

with open('negative-words.txt', encoding='ISO-8859-1') as negword:
  negativeWordList = [neg.strip() for  neg in negword.readlines()]

with open('tweetText.txt') as f:
  tweet_data =  [text.split("text:") for text in f.readlines()];
  
with open('polarity.csv','w') as pol:
   writer = csv.writer(pol)
   writer.writerow(['Tweet','Message','Match','Polarity'])
   
   for count in range(len(tweet_data[0])): 
       dict = {}
       # iterarting line by line to split each tweet and comparing words against positive and negative word list
       # then adding into a dictionery to create bag of words   
       # word as key and the count a value
       tweet = tweet_data[0][count].split(" ")
       for i in range(len(tweet)):
         dict_key = tweet[i].lower()
         if dict_key in dict.keys():
           dict[dict_key] = dict[dict_key] + 1
         else:
           dict[dict_key] = 1

       positiveWordCount=0
       negativeWordCount=0
       neutral=0
       polarity="neutral"
       matchWordList=""
       matchPositiveList =""
       matchNegativeList = ""
       for value in dict.keys():
         if value in positiveWordList:
          positiveWordCount=positiveWordCount+1
          matchPositiveList=matchPositiveList + value +","
          if value in positive_word_count:
            positive_word_count[value] += 1
          else:
            positive_word_count[value] = 1
      
         elif value in negativeWordList:
           negativeWordCount=negativeWordCount+1
           matchNegativeList=matchNegativeList + value +","
           if value in negative_word_count:
              negative_word_count[value] += 1
           else:
              negative_word_count[value] = 1
         else:
           neutral=neutral+1 

       if(positiveWordCount>negativeWordCount):
         polarity="positive"  
         matchWordList=matchPositiveList
       elif(positiveWordCount<negativeWordCount):
         polarity="negative"  
         matchWordList=matchNegativeList
       else:
          matchWordList="NONE," 
       writer.writerow([count,tweet_data[0][count],matchWordList[:-1],polarity]);   


with open('positivetAB.csv', 'w') as f:
    for key in positive_word_count.keys():
        f.write("%s,%s\n"%(key,positive_word_count[key]))
              
with open('negativeTAB.csv', 'w') as f:
    for key in negative_word_count.keys():
        f.write("%s,%s\n"%(key,negative_word_count[key]))