
import numpy as np 
import pandas as pd 

import pickle
# get all position CSVsWithAccolades you care about
# group positions that are 'equivalent for your purposes' ie RB, TB, HB
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

# this function returns an array of the form [[inputsArrays], outputsArray]
# ie [ [[1,2],[3,4]], [1,2] ]
def getPlayersStatsAsArray(positionGroupAsArrayOfPositionNamesAsStrings, csvFilePath, fileEndingString):
    positions = positionGroupAsArrayOfPositionNamesAsStrings
    playersStatsAsInputs = []
    playerStatsAsOutputs = []
    
    for position in positions:
        data = pd.read_csv(csvFilePath + position + fileEndingString)
        numberOfPlayers= data.count()
       # you will have to rewrite this later if you get different stats
       #Name,URL,Position,HallOfFame,TotalYears,LastYear,Active,MVP,Pro Bowl,All-Pro,SB Champ,AP PoY
       #Karim Abdul-Jabbar,/A/AbduKa00.htm,RB,0,5,2000,False,0,0,0,0,0
       #Active and LastYear are now irrelevant since when creating the csv files
       # i excluded players who are active and lastyear greater than 2015 which
       # means you aren't yet eligible for the hall of fame
       # in the future this can be rewritten to pop strings taken as arguments
        HallOfFame = data.pop('HallOfFame').values
        TotalYears = data.pop('TotalYears').values
        MVP = data.pop('MVP').values
        ProBowl = data.pop('Pro Bowl').values
        AllPro = data.pop('All-Pro').values
        SbChamp = data.pop('SB Champ').values
        APpoy = data.pop('AP PoY').values

        playersFromThisPositionAsInputs = [ 
                                           [ TotalYears[index],\
                                             MVP[index], \
                                             ProBowl[index], \
                                             AllPro[index], \
                                             SbChamp[index], \
                                             APpoy[index] \
                                            ] for index, element in  enumerate(TotalYears)]
        
        playersFromThisPositionAsOutputs = [element for element in HallOfFame]

        #print(len( playersFromThisPositionAsOutputs))

        playersStatsAsInputs += playersFromThisPositionAsInputs
        playerStatsAsOutputs += playersFromThisPositionAsOutputs

    return [playersStatsAsInputs, playerStatsAsOutputs]

#PlayerStatsArray = getPlayersStatsAsArray(OL,"positionCSVsWithAccolades/", "_WithAccolades.csv")

########################################################################

from sklearn import svm
# inputsArray ie [[1,2],[3,4]], outputsArray ie [0,1]
def getTrainedSVM(inputsArray, outputsArray):
  clf = svm.SVC(probability=True)
  clf.fit(inputsArray, outputsArray)
  return clf

#[0][1] is yes % [0][0] is no %
# willie roaf
#print(getTrainedSVM(PlayerStatsArray[0],PlayerStatsArray[1]).predict_proba([[13,0,11,4,0,0]])[0][1])

#print(positionGroupsDict)

  
def createAndSaveModels(positionGroupsDict,csvFilePathForGetPlayerStatsAsArray, fileEndingStringForGetPlayerStatsAsArray , savePathForModels):
    try:
       from joblib import dump, load
       import glob, os 
       from os import path   
    except:
        print("Oops!",sys.exc_info()[0],"occured. while importing basic libraries")
   
    # create save path
    try:
        os.mkdir(savePathForModels)
    #''OSerror when already made
    except OSError:
        pass
    
    
    for k, v in positionGroupsDict.items():
        #creation and then training
        PlayerStatsArray = getPlayersStatsAsArray(v,csvFilePathForGetPlayerStatsAsArray, fileEndingStringForGetPlayerStatsAsArray)
        trainedModel = getTrainedSVM(PlayerStatsArray[0], PlayerStatsArray[1])

        #saving
        os.chdir(savePathForModels)
        dump(trainedModel, k + '.joblib')
        os.chdir('..')

    
createAndSaveModels(positionGroupsDict, "positionCSVsWithAccolades/" , "_WithAccolades.csv", "AlreadyTrainedModelFiles")


