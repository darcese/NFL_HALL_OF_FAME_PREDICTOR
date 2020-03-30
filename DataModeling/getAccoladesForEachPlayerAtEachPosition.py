#grab all files in Positions CSV
import glob, os 
from os import path

#for csv
import csv

#scraping
from bs4 import BeautifulSoup
import requests
import json
import re
import time


os.chdir("positionCSVs")

old_file_names = []
new_file_names = []
countedSameLineAccolades = ["MVP","Pro Bowl","All-Pro","SB Champ"]

#for each file
for file in glob.glob("*.csv"):
    old_file_names.append(file)

os.chdir("..")
try:
    os.mkdir("positionCSVsWithAccolades")
except OSError:
    print(OSError)


os.chdir("positionCSVsWithAccolades")

#get old files to create new file names based on the old ones
for file in old_file_names:
    new_file_names.append(file[0:len(file)-4] + "_WithAccolades" + ".csv")

#make a new file linked to that position
for file in new_file_names:
    if not(path.exists(file)):
        f = open(file,'w')
        f.close()


#go into each of the old position files first



for idx,val in enumerate(old_file_names):
    os.chdir("../positionCSVs")

    with open(val) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')   
        arrayToHoldAllPlayersAtAPositionInfoForNewCSVs = []     
        #skip  column names
        columnNames = csvfile.readline()
        #for each player
        for row in readCSV:
            
            #get current column values in old csv       
            #Name,URL,Position,HallOfFame,TotalYears,LastYear,Active
            #/A/AbruFr20.htm
            arrayToHoldSinglePlayerInfo = row
            #use html column to go to their page
            #check if they have the bling tag
            url = "https://www.pro-football-reference.com/players" + arrayToHoldSinglePlayerInfo[1]
            response = requests.get(url, timeout=5)
            content = BeautifulSoup(response.content, "html.parser")
            time.sleep(2.5)
            backNumber = 4


            #add bling column values to their columns
            try:        
                text = content.find(id="bling").text
                for accolade in countedSameLineAccolades:
                    if accolade in text:
                        accoladeIndex = text.index(accolade)
                        accoladeTimesPreFilter = text[accoladeIndex-backNumber: accoladeIndex]
                        accoladeTimes = int(re.sub("[^0-9]", "", accoladeTimesPreFilter))
                        arrayToHoldSinglePlayerInfo.append(accoladeTimes)
                    else:
                        arrayToHoldSinglePlayerInfo.append(0)
                arrayToHoldSinglePlayerInfo.append(text.count("AP Off. PoY" + "AP Def. PoY"))         
             #if not theyll have column values of 0
            except:
                for accolade in countedSameLineAccolades:
                    arrayToHoldSinglePlayerInfo.append(0)
                #line below is just for AP Off. Poy and Def. Poy
                arrayToHoldSinglePlayerInfo.append(0)
             
            #add single player info to the array holding all players at a position   
            arrayToHoldAllPlayersAtAPositionInfoForNewCSVs.append(arrayToHoldSinglePlayerInfo)
        csvfile.close() 

        
    os.chdir("../positionCSVsWithAccolades")
    with open(new_file_names[idx]) as csvWriteFile:
        spamwriter = csv.writer(csvWriteFile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        headerColumn = [column for column in columnNames]
        headerColumn += countedSameLineAccolades + ["AP PoY"]
        print(headerColumn)
        spamwriter.writerow(headerColumn)
        for row in arrayToHoldAllPlayersAtAPositionInfoForNewCSVs:
            spamwriter.writerow(row)
            csvWritefile.close()

     