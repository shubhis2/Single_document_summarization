from sklearn.cluster import KMeans
import global_var as gv
import pandas as pd
from nltk.tokenize import sent_tokenize
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import FreqDist
import numpy as np
from nltk.cluster.kmeans import KMeansClusterer
import nltk
import numpy
path="/home/yashu/8TH_PRO/Final/Model/test_large"
result=[]
filelist=[]
for file in os.listdir(path):
        if file.endswith(".txt"):
            res=[]
            with open(path+"/"+file,'r') as f:
                    sentences=sent_tokenize(f.read())
                    for i in sentences:
                        res.append(i.translate(gv.table))
            result.append(res)
            filelist.append(file)

print(filelist)
print(result)
vectorizer = TfidfVectorizer(stop_words='english')
#print("clustering for:",filelist[0])
train_vectors = vectorizer.fit_transform(result[0])
for i in train_vectors:
    print(i)
"""
k_sentences = 4
model = KMeans(n_clusters=k_sentences, init='k-means++', max_iter=100, n_init=1)
c=model.fit_predict(train_vectors)



#print(model.get_params())
#print(model.score(train_vectors))

dd=model.transform(train_vectors)
#centroids = model.cluster_centers_

#print("centroid information")
#print(centroids)
final=[]

for i in dd:
    res=[]
    for j  in i:
        res.append(float(j))
    final.append(res)
#print(final)
cc=list(zip(c,final,result[0]))

#ccc=list(zip(cc,result[0]))
#print(pp)
ppp={}
#print(cc[0])

for i in cc:
    if i[0] not in ppp:
        ppp[i[0]]=[]
        ppp[i[0]].append((i[2],i[1][i[0]]))
    else:
        ppp[i[0]].append((i[2],i[1][i[0]]))
        
print(ppp[0]) 


#Y = vectorizer.transform(["chrome browser to open."])
#prediction = model.predict(train_vectors)

pp=list(zip(prediction,result[0]))
ppp={}
for i in pp:
    if i[0] not in ppp:
        ppp[i[0]]=[]
        ppp[i[0]].append(i[1])
    else:
       ppp[i[0]].append(i[1])
print(lenppp[0]))
"""
#vectors = [numpy.array(f) for f in train_vectors]

kclusterer = KMeansClusterer(4, distance=nltk.cluster.util.cosine_distance, repeats=25)
#assigned_clusters = kclusterer.cluster(train_vectors, assign_clusters=True)
#print(assigned_clusters)
