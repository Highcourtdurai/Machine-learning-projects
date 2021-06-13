import pandas as pd
import numpy as np

data=pd.read_csv("spam.csv",encoding="latin-1")

x=data.iloc[:,1].values
y=data.iloc[:,0].values

from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
import string
import re

stop=set(stopwords.words('english'))
punc=set(string.punctuation)
lemmetizer=WordNetLemmatizer()

# print("stop")
# print("punc")
# print("lemmeatizer.lemmatize('dogs")

def clean(msg):
    msg=" ".join([i for i in msg.lower().split() if i not in stop])
    msg="".join([i for i in msg if i not in punc])
    msg="".join([lemmetizer.lemmatize(i) for i in msg])
    msg=re.sub(r"\d+","",msg)
    msg=re.sub(r"\s+"," ",msg)
    return msg
    
for i in range(len(x)):
    x[i]=clean(x[i])
    
vectorizer=CountVectorizer()
x=vectorizer.fit_transform(x)  

#print(vectorizer.vocabulary_)


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)

from sklearn.naive_bayes import MultinomialNB
classifier=MultinomialNB()
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

print(classifier.score(x_test,y_test))


print(classifier.predict(vectorizer.transform([clean("Sorry my roommates took forever, it ok if I come by now?")])))







