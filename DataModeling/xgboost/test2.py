import xgboost as xgb
# read in data

# GET DATA
# Use position CSVs
OL = ["C", "G", "OL", "OT", "T"]
DB = ["CB","DB","FS","S","SS"]
DE = ["DE", "DL"]
FB = ["FB", "WB"]
WR =["FL","WR","SE", "E"]
DT = ["DG", "DL", "DT", "NT"]
RB = ["HB", "RB","TB","WB"]
TE = ["TE"]
LB = ["ILB", "LB", "OLB"]
K = ["K"]
P = ["P"]
QB = ["QB"]
positionGroupsDict = dict(OL=OL, DB=DB , DE=DE, FB=FB, WR=WR, DT=DT, RB=RB, TE=TE, LB=LB, K=K, P=P, QB=QB)
positionGroupsDFDict = {}
xgboostDataDict = {}
xgboostLabelsDict = {}

# create pandas df for each position group using files inside positionCSVsCurrentInclusive
import pandas as pd
import os
os.chdir('..')
fakeDFtoGetColumns = pd.read_csv('positionCSVsWithAccolades/B_WithAccolades.csv')
for positionGroup, positions in positionGroupsDict.items():
    # make the empty dataframe
    positionGroupsDFDict[positionGroup] = pd.DataFrame(columns=fakeDFtoGetColumns.columns)
    for position in positions:
        positionGroupsDFDict[positionGroup] = pd.concat([positionGroupsDFDict[positionGroup], pd.read_csv('positionCSVsWithAccolades/'+ position +'_WithAccolades.csv')])

    #print(positionGroupsDFDict[positionGroup].head(3))

    
        #a = positionGroupsDFDict[positionGroup].loc[positionGroupsDFDict[positionGroup]['Position'] == position]
        #print(a)
    # SEE how much of each class there is for each position group,
    print(positionGroup)
    print(positionGroupsDFDict[positionGroup].HallOfFame.value_counts().to_string())
    print(positionGroupsDFDict[positionGroup].HallOfFame.mean())
    print()

    train = positionGroupsDFDict[positionGroup]
    target = train['HallOfFame']
    train = train.drop(['Name','URL', 'Position','LastYear' ,'Active'],axis=1)

    test = train

    xgtrain = xgb.DMatrix(train.values, target.values)
    xgtest = xgb.DMatrix(test.values)

    param = {'max_depth':10, 'eta':1, 'objective':'binary:logistic' }
    num_round = 2
    bst = xgb.train(param, xgtrain, num_round)
    # make prediction
    preds = bst.predict(xgtest)

    print(preds)
    print()
## ADD Weights, be able to tune weights
#https://stackoverflow.com/questions/48079973/xgboost-sample-weights-vs-scale-pos-weight

# Train and test multiple model