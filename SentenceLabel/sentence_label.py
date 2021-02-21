import csv
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize
import string

#global variables
stopWords=set(stopwords.words('english'))
wordIndex={}
termFrequency={}
sentenceLabel=[]
charReplaceMapping={'.':' ','-':'',"'":' ','"':""," ":"","\n":"","\t":" "}
table=str.maketrans(charReplaceMapping)
output = open('/home/yashu/8TH_PRO/Final/Dataset/sentence_label_10_4_test0000.csv', 'w')
writer = csv.writer(output)

def sentenceTokenize(text):
	return sent_tokenize(text)

def wordTokenize(sentence):
	sentence=sentence.translate(table)
	return word_tokenize(sentence)

def isValidTerm(term):
	return term.isalnum() and term.lower() not in stopWords



def read_csv(filename):
    global termFrequency
    global sentenceLabel
    global table
    d=1
    s=0
    with open(filename) as csvfile:
        read = csv.reader(csvfile, delimiter=',')
        next(read)
        for row in read:
            list_of_text=sentenceTokenize(row[3])
            list_of_summary=sentenceTokenize(row[4])
            for sentence in list_of_summary:
                for word in sentence:
                    if isValidTerm(word):
                        if word not in termFrequency:
                            termFrequency[word]=1
                        else:
                            termFrequency[word]+=1
            list_of_summary=["".join(k.translate(table)) for k in list_of_summary]
            s+=len(list_of_summary)
            print(list_of_summary)
            for i in list_of_text:
                #i=i.strip().replace()
                #print("text::",i)
                #j=i.replace(" ","").replace("\t","")
                p="".join(i.translate(table))
                #print(p)
                l=[]
                if p != '':
                    if p in list_of_summary:
                        print("true summary")
                        l.append(d)
                        l.append(i)
                        l.append(1)
                        writer.writerow(l)
                        sentenceLabel.append((i,1))
                    else:
                        l.append(d)
                        l.append(i)
                        l.append(0)
                        writer.writerow(l)
                        sentenceLabel.append((i,0))
            d+=1
        print(s)
                
				



read_csv("/home/yashu/8TH_PRO/Final/Dataset/news_10_4.csv")

