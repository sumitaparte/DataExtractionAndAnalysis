import math,csv

totalDocs=499
canadaDoc = 0
halifaxDoc=0
universityDoc=0
canadaEduDoc=0
dalUniDoc=0
rowList = [] 
def findLog(document, df):
  try:
    val = math.log10(document/df)
    val = round(val,2)
  except ZeroDivisionError: 
    val = "inf"
  return val

for num in range(498):
  canada=0
  halifax=0
  university=0
  canEducation=0
  dalUniversity=0
  fileName = "data_file_" +str(num+1) + ".txt"
  with open(fileName,'r', encoding="utf-8") as f:
    content = (f.readline().lower())
    words = content.split(" ")  
    #print(words)
    
    for i in range(len(words)):
            
        if words[i]=='canada':
            canada = canada+1
            
        if words[i]=='university':
            university = university+1

        if words[i]=='halifax':
            halifax = halifax+1    
            
        if(i< len(words) and words[i]=='canada'and words[i+1]=='education'):
            canEducation = canEducation+1
            
        if(i< len(words) and words[i]=='dalhousie'and words[i+1]=='university'):
            dalUniversity = dalUniversity+1
    
    if(canada >0):
        canadaDoc = canadaDoc + 1 
        # file name, Total num of word, num of canada
        line = str(num+1) +","+str(len(words)) +","+str(canada)
        rowList.append(line)      
        
    if(university >0):
        universityDoc = universityDoc + 1   
            
    if(halifax >0):
        halifaxDoc = halifaxDoc + 1    
        
    if(canEducation >0):
        canadaEduDoc = canadaEduDoc + 1 
        
    if(dalUniversity >0):
        dalUniDoc = dalUniDoc + 1 
# for end #

freqCan = findLog(totalDocs,canadaDoc)
freqUni = findLog(totalDocs,universityDoc)
freqHali = findLog(totalDocs,halifaxDoc) 
freqCanEdu = findLog(totalDocs,canadaEduDoc)    
freqDalUni = findLog(totalDocs,dalUniDoc) 

with open('Semantic_analysis.csv','w') as output_semantic:
 writer = csv.writer(output_semantic)
 writer.writerow(['Total documents',totalDocs])
 writer.writerow(['Search Query','Document Containing Term(df)','Total documents(N)/number of  documents  term  appeared (df)','Log10(N/df)'])
 writer.writerow(['Canada',canadaDoc, (str(totalDocs) +"/"+ str(canadaDoc)), str(freqCan)])
 writer.writerow(['University',universityDoc, (str(totalDocs) +"/"+ str(universityDoc)), str(freqUni)])
 writer.writerow(['Halifax',halifaxDoc,(str(totalDocs) +"/"+ str(halifaxDoc)), str(freqHali)])
 writer.writerow(['Canada Education',canadaEduDoc,(str(totalDocs) +"/"+ str(canadaEduDoc)), str(freqCanEdu)])
 writer.writerow(['Dalhousie University',dalUniDoc,(str(totalDocs) +"/"+ str(dalUniDoc)), str(freqDalUni)])

#document has the highest occurrence of the word “Canada”.
max=0
with open('Semantic_analysis_canada.csv','w') as f:
  writer = csv.writer(f)
  writer.writerow(['Term', 'Canada'])  
  writer.writerow(['Canada appeared in '+  str(canadaDoc) + ' documents', 'Total words(m)', 'Frequency(f)', 'f/m'])
  for i in range(canadaDoc):
      row = rowList[i].split(",")
      freq= round(int(row[2])/int(row[1]),2)
      writer.writerow(["Article #"+ row[0], row[1], row[2], freq ])
     
      if(freq>max):
        max=freq
        article = row[0] 
fileName = "data_file_" +str(article) + ".txt"
print("FileName:"+fileName)
with open(fileName,'r') as f:
    content = (f.readlines())
    print(content)