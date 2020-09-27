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

positionGroupsDict = dict(OL=OL, DB=DB, DE=DE, FB=FB, QB=QB, WR=WR, DT=DT, RB=RB, TE=TE, LB=LB, K=K, P=P)
positionGroupsDFDictTrain = {}
positionGroupsDFDictTest = {}
xgboostDataDict = {}
xgboostLabelsDict = {}

positionGroupsTrainingParamsDict = dict(DB={} , DE={}, FB={}, WR={}, DT={}, RB={}, TE={}, LB={}, K={}, P={}, QB={}, OL={})
positionGroupsTrainingParamsDict["OL"] = { 'max_depth':100, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1, 'enable_experimental_json_serialization': True}
positionGroupsTrainingParamsDict["DB"] = {'max_depth':200, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1, 'enable_experimental_json_serialization': True}
positionGroupsTrainingParamsDict["DE"] = {'max_depth':200, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1, 'enable_experimental_json_serialization': True}
positionGroupsTrainingParamsDict["WR"] = {'max_depth':50, 'eta':1.5, 'lambda': 0.5, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1, 'enable_experimental_json_serialization': True}
positionGroupsTrainingParamsDict["DT"] = {'max_depth':20, 'eta':1.0, 'lambda': 0.5, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1, 'enable_experimental_json_serialization': True}
positionGroupsTrainingParamsDict["RB"] = {'max_depth':50, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1, 'enable_experimental_json_serialization': True}
positionGroupsTrainingParamsDict["TE"] = {'max_depth':10, 'eta':0.05, 'lambda': 0.05, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1, 'enable_experimental_json_serialization': True}
positionGroupsTrainingParamsDict["K"] = {'max_depth':100, 'eta':1.25, 'lambda': 0.5, 'grow_policy': 'lossguide', 'alpha':1, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1, 'enable_experimental_json_serialization': True}
positionGroupsTrainingParamsDict["P"] = {'max_depth':200, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':.4, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1, 'enable_experimental_json_serialization': True}
positionGroupsTrainingParamsDict["TE"] = {'max_depth':100, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1, 'enable_experimental_json_serialization': True}
positionGroupsTrainingParamsDict["QB"] = {'max_depth':100, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1, 'enable_experimental_json_serialization': True}
positionGroupsTrainingParamsDict["FB"] = {'max_depth':100, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1, 'enable_experimental_json_serialization': True}
positionGroupsTrainingParamsDict["LB"] = {'max_depth':100, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1, 'enable_experimental_json_serialization': True}

positionGroupsPosWeightsToBeSquaredDict = dict(WR=.5, DT=.75, RB=.75, TE=.4, LB=.75, K=.5, P=.00025, QB=.75, OL=.75, DB=.75, DE=.75, FB=.5 )

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
    if positionGroup == 'WR' or positionGroup == 'K' :
       train = train.drop(['TotalYears'],axis=1)
    train = train.drop(['Name','URL', 'Position','LastYear' ,'Active','HallOfFame'],axis=1)

    test = positionGroupsDFDictTest[positionGroup]
    if positionGroup == 'WR' or  positionGroup == 'K':
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
    bst.save_model(str(positionGroup) +'.json')
    # make prediction
    #preds = bst.predict(xgtest)
    # in the future do the prediction on the active players

    #print(preds)
    print()
    #bst = xgb.Booster({'nthread': 4})  # init model
    bst.load_model('model_file_name.json') 
    preds = bst.predict(xgtest)
    # in the future do the prediction on the active players

    print(preds)
## ADD Weights, be able to tune weights
#https://stackoverflow.com/questions/48079973/xgboost-sample-weights-vs-scale-pos-weight

# Train and test multiple model