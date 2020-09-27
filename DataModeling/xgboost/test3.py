import xgboost as xgb


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


import pandas as pd
import os
import datetime
import numpy as np
os.chdir('..')

# this is just dbs right now
param = {'max_depth':200, 'eta':1.5, 'lambda': 0.25, 'grow_policy': 'lossguide', 'alpha':0, 'tree_method': 'exact','objective':'binary:logistic', 'scale_pos_weight':  1, 'enable_experimental_json_serialization': True}


num_round = 2
bst = xgb.Booster({'nthread': 4}) 
bst.load_model('DB.json') 


date = datetime.date(1991, 10, 12)
print(f'{date} was on a {date:%A}')


data = np.random.rand(3, 6) # 6 columns of features right now.
print(data)
dtest = xgb.DMatrix(data)
ypred = bst.predict(dtest)
print(ypred)

# NEXT THING TO DO LOAD THE JSON PREDICTION FILE
# Hard code a fake player to predict on, match up player position with right predictive algorithm