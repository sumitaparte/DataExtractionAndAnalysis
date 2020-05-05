import re, string
from pyspark.sql.functions import col
from pyspark import SparkContext, SparkConf
config = SparkConf().setMaster("spark://ip-172-31-25-40.us-east-2.compute.internal:7077").setAppName("MapReduceCount")

sc = SparkContext(conf = config) 

text_file = sc.textFile('newsTweetText.txt')

string.punctuation
punc = '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~'

# for removing punctuations and converting into lowercase
def uni_to_clean_str(x):
    converted = x.encode('utf-8')
    lowercased_str = converted.lower()
    lowercased_str = lowercased_str.replace('--',' ')
    clean_str = lowercased_str.translate(None, punc)
    return clean_str

# for converting the input of words into 2 words. 
def form_Phrases(line):
            single_words = uni_to_clean_str(line).split()
            return [a + " " + b for a,b in zip(single_words, single_words[1:])]

################################## MAIN #######################
			
# for Single words	
one_RDD = text_file.flatMap(lambda x: uni_to_clean_str(x).split())
one_RDD = one_RDD.map(lambda x: (x,1))
one_RDD = one_RDD.reduceByKey(lambda x,y: x + y)

# copy into a DF
dfword = spark.createDataFrame(one_RDD).toDF("Word", "Count")
# output for single words
data = dfword.filter(col('Word').isin(['education','canada','university','dalhousie','expensive', 'faculty', 'graduate'])).show()
data.rdd.repartition(1).saveAsTextFile("WordOutputFile.txt")

# for phrases				
two_RDD=text_file.flatMap(form_Phrases)
two_RDD=two_RDD.map(lambda x :(x,1))
two_RDD=two_RDD.reduceByKey(lambda x,y: x + y)

dfphrase = spark.createDataFrame(two_RDD).toDF("Word", "Count")
data1 = dfphrase.filter(col('Word').isin(['bad school','bad schools','good school','good schools','poor school', 'poor schools', 'computer science'])).show()

data1.rdd.repartition(1).saveAsTextFile("PhraseOutputFile.txt")