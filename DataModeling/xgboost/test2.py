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
positionGroupsDFDictTrain = {}
positionGroupsDFDictTest = {}
xgboostDataDict = {}
xgboostLabelsDict = {}

# create pandas df for each position group using files inside positionCSVsCurrentInclusive
import pandas as pd
import os
os.chdir('..')
fakeDFtoGetColumns = pd.read_csv('positionCSVsWithAccolades/B_WithAccolades.csv')
for positionGroup, positions in positionGroupsDict.items():
    # make the empty dataframe
    positionGroupsDFDictTrain[positionGroup] = pd.DataFrame(columns=fakeDFtoGetColumns.columns)
    positionGroupsDFDictTest[positionGroup] = pd.DataFrame(columns=fakeDFtoGetColumns.columns)
    for position in positions:
        positionGroupsDFDictTrain[positionGroup] = pd.concat([positionGroupsDFDictTrain[positionGroup], pd.read_csv('positionCSVsWithAccolades/'+ position +'_WithAccolades.csv')])
        positionGroupsDFDictTest[positionGroup] = pd.concat([positionGroupsDFDictTest[positionGroup], pd.read_csv('positionCSVsWithAccoladesCurrentInclusiveForTesting/'+ position +'_WithAccolades.csv')])
    #print(positionGroupsDFDict[positionGroup].head(3))

    
        #a = positionGroupsDFDict[positionGroup].loc[positionGroupsDFDict[positionGroup]['Position'] == position]
        #print(a)
    # SEE how much of each class there is for each position group,
    print(positionGroup)
    print(positionGroupsDFDictTrain[positionGroup].HallOfFame.value_counts().to_string())
    averageHOFLikelihood = positionGroupsDFDictTrain[positionGroup].HallOfFame.mean()
    print()

    train = positionGroupsDFDictTrain[positionGroup]
    target = train['HallOfFame']
    train = train.drop(['Name','URL', 'Position','LastYear' ,'Active','HallOfFame'],axis=1)

    test = positionGroupsDFDictTest[positionGroup]
    test = test.drop(['Name','URL', 'Position','LastYear' ,'Active','HallOfFame'],axis=1)
    xgtrain = xgb.DMatrix(train.values, target.values)
    xgtest = xgb.DMatrix(test.values)
    #lambda 1 default alpha default 0
    #param = {'max_depth':15, 'eta':1.75, 'objective':'binary:logistic', 'scale_pos_weight':  (1/averageHOFLikelihood)}
    param = {'max_depth':100, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  (1/averageHOFLikelihood)}
    # test and tune this
    num_round = 2
    bst = xgb.train(param, xgtrain, num_round)
    # make prediction
    preds = bst.predict(xgtest)
    # in the future do the prediction on the active players

    print(preds)
    print()
## ADD Weights, be able to tune weights
#https://stackoverflow.com/questions/48079973/xgboost-sample-weights-vs-scale-pos-weight

# Train and test multiple model