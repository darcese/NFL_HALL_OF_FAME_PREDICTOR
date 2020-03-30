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

from sklearn import svm

#Name,URL,Position,HallOfFame,TotalYears,LastYear,Active
# A utility mprethod to create a tf.data dataset from a Pandas Dataframe
#HallOfFame     int64
#TotalYears     int64
#dtype: object
#[0]
#16
#1092


CombinedBins=[]
for i in range(0,30):
  #  CombinedBins.append([i,NoHOFandYearsBuckets[i],HOFandYearsBuckets[i]])
    pass
print(CombinedBins)

#years,NoHOF tally, NoHOF tally
#[12, 16, 3], [13, 8, 4], [14, 8, 2], [15, 1, 3], [16, 2, 1]
#avg years 14, 16+8+8+1+2 noHOF, 3,4,2,3,1 noHOF
#lets find a HOF upsample amount that makes it a (3,4,2,3,1)/(16+8+8+1+2)+(3,4,2,3,1) probability a 14 year player makes the HOF
print((3+4+2+3+1)/(16+8+8+1+2+3+4+2+3+1))

# this is also sort of the prediction function. probably rename later and separate into 2
def findRightupSampleFunction(HOFupSampleTimes,NoHOFupSampleTimes):
    """ returns the temperature in degrees Fahrenheit """
   
    PredictedValue = 0

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
            for upSampleCounter in range(1,HOFupSampleTimes):
                FHOF = FHOF + 1
                yy.append(val)
                xx.append([x[idx]])

            HOFandYearsBuckets[x[idx]]+=1
        else:
            NoHOF = NoHOF+1
            yy.append(val)
            xx.append([x[idx]])
            #up-sample here to add more granular control of artifical ratio of hofers to non hofers
            for upSampleCounter in range(1,NoHOFupSampleTimes): # 12 and 6 seem to work well
                FHOF = FHOF + 1
                yy.append(val)
                xx.append([x[idx]])

            NoHOFandYearsBuckets[x[idx]]+=1

    clf = svm.SVC(probability=True)
    clf.fit(xx[:-1], yy[:-1])

    PredictedValue = clf.predict_proba([[14]])[0][1]

    return PredictedValue


predictionsGettingBetter = True
initialHOFupSampleTimes = 0
initialNoHOFupSampleTimes = 0
predictionGoal = 0.270833
previousPredictionDifference = 1


HOFupSampleTimes = initialHOFupSampleTimes
NoHOFupSampleTimes = initialNoHOFupSampleTimes
LastChanged = "Nothing"
PredictionsWorseCounter = 0
ChangesCounter = 0
ZeroAgainCounter = 0
min([1,2])
while predictionsGettingBetter:


    # 0,0 2,1, 1,1 1,0  0,1 2,1
    UpSampleAdditionsArrary = [[0,0],[1,1],[1,0],[2,1],[3,2],[4,3],[5,3],[5,2],[0,1],[1,2],[2,3],[3,4],[3,5],[5,2]]
    PredictionDifferencesArray = []

    for idx, val in enumerate( UpSampleAdditionsArrary):
        
        PredictionDifferencesArray.append( \
            abs(findRightupSampleFunction(HOFupSampleTimes + val[0],\
            NoHOFupSampleTimes + val[1])- predictionGoal))
        

    indexOfBestMove = PredictionDifferencesArray.index(min(PredictionDifferencesArray))
    
    #if indexOfBestMove > 0 and ChangesCounter < 100:
    if ChangesCounter < 10 and ZeroAgainCounter < 4:
        print("pre addition" , HOFupSampleTimes  , NoHOFupSampleTimes)
        HOFupSampleTimes += UpSampleAdditionsArrary[indexOfBestMove][0]
        NoHOFupSampleTimes += UpSampleAdditionsArrary[indexOfBestMove][1]
        
        print("post addition ", HOFupSampleTimes , NoHOFupSampleTimes)
        ChangesCounter += 1
        
        if indexOfBestMove == 0 :
            ZeroAgainCounter+=1
        else:
            ZeroAgainCounter=0

    else:
        predictionsGettingBetter = False
        print("last prediction", findRightupSampleFunction(HOFupSampleTimes,\
            NoHOFupSampleTimes))
        print("difference = " ,findRightupSampleFunction(HOFupSampleTimes,\
            NoHOFupSampleTimes) - predictionGoal)





   
# ok this doesn't work . big discrete jumps in upsampling may be smooth enough. maybe try ratios next



print(str(HOFupSampleTimes)+" "+str(NoHOFupSampleTimes))

        
        
        

## ok so the next step is to not just end after predictionsGetting Better goes worse one time. if it does get worse
## adding to the one that didn't get added to last time and see if that gets better

#ok shit that almost worked but not really. brainstorm later and get back to it
