from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow  as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import pandas as pd
import pandas_profiling as pdpf

import matplotlib.pyplot as plt

from tensorflow import feature_column
from keras import layers
import sklearn
from sklearn.model_selection import train_test_split

print('hello')
print(tf.__version__)

#'dataset= np.loadtxt("positionCSVs/RB.csv",delimiter=",")
# split into input (X) and output (Y) variables

data = pd.read_csv("positionCSVs/RB.csv")

print(data.head(5))
print(data.shape)
print(data.isnull().sum())
#pdpf.ProfileReport(data)

#train, test = train_test_split(data, test_size=0.5)
#train, val = train_test_split(train, test_size=0.5)
#print(len(train), "train examples")
#print(len(val), "validation examples")
#print(len(test), "test examples")
del data['Name']
del data['URL']
del data['LastYear']
del data['Active']
#data.drop(['Name','Position','LastYear','Active'], axis=1)
print(data.dtypes)
y = data.pop('HallOfFame').values
x = data.pop('TotalYears').values
yy = []
xx = []
HOF = 0
FHOF = 0
NoHOF =0


HOFandYearsBuckets = [0] * 30
NoHOFandYearsBuckets = [0] * 30


for idx, val in enumerate(y):
    
    if val == 1:
        HOF = HOF+1
        yy.append(val)
        xx.append([x[idx]])
        #up-sample to artificially add more HOFers
        for upsampleCounter in range(1,12):
            FHOF = FHOF + 1
            yy.append(val)
            xx.append([x[idx]])

        HOFandYearsBuckets[x[idx]]+=1
    else:
        NoHOF = NoHOF+1
        yy.append(val)
        xx.append([x[idx]])
        #up-sample here to add more granular control of artifical ratio of hofers to non hofers
        for upsampleCounter in range(1,6): # 12 and 6 seem to work well
            FHOF = FHOF + 1
            yy.append(val)
            xx.append([x[idx]])

        NoHOFandYearsBuckets[x[idx]]+=1

    




  



 
       
       
   
#xcounts = train['TotalYears'].value_counts()
#print(xcounts)


from sklearn import svm
clf = svm.SVC(probability=True)

clf.fit(xx[:-1], yy[:-1])
print(clf.predict_proba([[14]]))
print(HOF)
print(NoHOF)
#Name,URL,Position,HallOfFame,TotalYears,LastYear,Active
# A utility mprethod to create a tf.data dataset from a Pandas Dataframe
#HallOfFame     int64
#TotalYears     int64
#dtype: object
#[0]
#16
#1092

print(NoHOFandYearsBuckets)
print(HOFandYearsBuckets)

CombinedBins=[]
for i in range(0,30):
    CombinedBins.append([i,NoHOFandYearsBuckets[i],HOFandYearsBuckets[i]])

print(CombinedBins)

#years,NoHOF tally, NoHOF tally
#[12, 16, 3], [13, 8, 4], [14, 8, 2], [15, 1, 3], [16, 2, 1]
#avg years 14, 16+8+8+1+2 noHOF, 3,4,2,3,1 noHOF
#lets find a HOF upsample amount that makes it a (3,4,2,3,1)/(16+8+8+1+2)+(3,4,2,3,1) probability a 14 year player makes the HOF
print((3+4+2+3+1)/(16+8+8+1+2+3+4+2+3+1))