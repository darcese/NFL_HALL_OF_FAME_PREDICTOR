import xgboost as xgb
# read in data

# GET DATA
# Use position CSVs
OL = ["C", "G", "OL", "OT", "T"]
DB = ["CB","DB","FS","S","SS"]
DE = ["DE", "DL"] #check this one again
FB = ["FB", "WB"]
WR =["FL","WR","SE", "E"]
DT = ["DG", "DL", "DT", "NT"]
RB = ["HB", "RB","TB","WB"]
TE = ["TE"]
LB = ["ILB", "LB", "OLB"]
K = ["K"]
P = ["P"]
QB = ["QB"]

positionGroupsDict = dict(RB=RB, TE=TE, LB=LB, K=K, P=P, OL=OL, DB=DB, DE=DE, FB=FB, QB=QB, WR=WR, DT=DT )
positionGroupsDFDictTrain = {}
positionGroupsDFDictTest = {}
xgboostDataDict = {}
xgboostLabelsDict = {}

positionGroupsTrainingParamsDict = dict(DB={} , DE={}, FB={}, WR={}, DT={}, RB={}, TE={}, LB={}, K={}, P={}, QB={}, OL={})
positionGroupsTrainingParamsDict["OL"] = {'max_depth':100, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1}
positionGroupsTrainingParamsDict["DB"] = {'max_depth':200, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1}
positionGroupsTrainingParamsDict["DE"] = {'max_depth':200, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1}
positionGroupsTrainingParamsDict["WR"] = {'max_depth':50, 'eta':1.5, 'lambda': 0.5, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1}
positionGroupsTrainingParamsDict["DT"] = {'max_depth':20, 'eta':1.0, 'lambda': 0.5, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1}
positionGroupsTrainingParamsDict["RB"] = {'max_depth':100, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1}
positionGroupsTrainingParamsDict["TE"] = {'max_depth':100, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1}
positionGroupsTrainingParamsDict["K"] = {'max_depth':100, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1}
positionGroupsTrainingParamsDict["P"] = {'max_depth':100, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1}
positionGroupsTrainingParamsDict["TE"] = {'max_depth':100, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1}
positionGroupsTrainingParamsDict["QB"] = {'max_depth':100, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1}
positionGroupsTrainingParamsDict["FB"] = {'max_depth':100, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1}

positionGroupsPosWeightsToBeSquaredDict = dict(WR=.5, DT=.75, RB=.75, TE=.75, LB=.75, K=.75, P=.75, QB=.75, OL=.75, DB=.75, DE=.75, FB=.5 )

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
    if positionGroup == 'WR':
       train = train.drop(['TotalYears'],axis=1)
    train = train.drop(['Name','URL', 'Position','LastYear' ,'Active','HallOfFame'],axis=1)

    test = positionGroupsDFDictTest[positionGroup]
    if positionGroup == 'WR':
        test = test.drop(['TotalYears'],axis=1)
    test = test.drop(['Name','URL', 'Position','LastYear' ,'Active','HallOfFame'],axis=1)

    xgtrain = xgb.DMatrix(train.values, target.values)
    xgtest = xgb.DMatrix(test.values)

    #lambda 1 default alpha default 0
    #param = {'max_depth':15, 'eta':1.75, 'objective':'binary:logistic', 'scale_pos_weight':  (1/averageHOFLikelihood)}
    positionGroupsTrainingParamsDict[positionGroup]['scale_pos_weight'] = (1/averageHOFLikelihood)**positionGroupsPosWeightsToBeSquaredDict[positionGroup]
    param = positionGroupsTrainingParamsDict[positionGroup]
    
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