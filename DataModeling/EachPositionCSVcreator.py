import csv
import re

TrueAsString = "true"  
allPositions = []

with open('/Users/danielarcese/Desktop/Code/WebProjectsAndTests/NFL_Hall_Of_Fame_Predictor/DataModeling/nflPlayersAndCareerLengths.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
   
    for row in readCSV:
        #re.split('; |, |\*|\n',a)
        currentPlayersListedPositions = re.split('-|/',row[3])#'row[3].split('-')

        for position in currentPlayersListedPositions:
            position = position.replace('position:"','').replace('\\n',"").replace('"','')
            if position not in allPositions and len(position)> 0:
                allPositions.append(position)


for EachPosition in allPositions:
    print(EachPosition)
    #DataModeling/positionCSVs/T.csv
    with open('positionCSVs/' + EachPosition+ '.csv', 'w', newline='') as csvWriteFile:
        spamwriter = csv.writer(csvWriteFile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

        with open('/Users/danielarcese/Desktop/Code/WebProjectsAndTests/NFL_Hall_Of_Fame_Predictor/DataModeling/nflPlayersAndCareerLengths.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
   
                
            spamwriter.writerow(['Name','URL','Position','HallOfFame','TotalYears','LastYear','Active'])
            for row in readCSV:  #
                currentPlayersListedPositions = re.split('-|/',row[3])#'row[3].split('-')


                for NowPositions in currentPlayersListedPositions:
                    position1 = NowPositions.replace('position:"','').replace('\\n',"").replace('"','')
                    if position1 == EachPosition:
                        try:
                            if int(row[6].replace('last year:','')) < 2015: #modern inclusive verion comments this line out

                                spamwriter.writerow([row[1].replace('\\n',"").replace('name:','')[1:-1],
                                row[2][5:-1],
                            
                                row[3].replace('position:"','')[0:-1],
                                1 if TrueAsString in row[4].replace('hall of fame:','') else 0,
                                (int(row[8].replace('totalYears:','').replace('.0','')[0:-1])),
                                (int(row[6].replace('last year:',''))),
                                #Active or not
                                (TrueAsString in row[7].replace('active:','')),
                                ]
                                )
                                # last year is index 7
                        except:

                            if int(row[7].replace('last year:','')) < 2015: #modern inclusive version comments this line out
                                # work around for 5 olineman with a comma , in between positions like G, T ie
                                # '{"_id":{"$oid":"5e198f2757d6d0dad8ec2091"}', 'name:"Desmond Wynn"', 'url:"/W/WynnDe01.htm"', 'position:"G', 'T"', 'hall of fame:false', 'first year:2012', 'last year:2012'
                                print(row)
                                spamwriter.writerow([row[1].replace('name:','')[1:-1],
                                row[2][5:-1],
                                # clumsy position workaround clean this up jk never touch and forget instead
                                (row[3]+ '-' + row[4]).replace('position:"','').replace('"','').replace("'",""),
                                1 if TrueAsString in row[5].replace('hall of fame:','') else 0,
                                (int(row[9].replace('totalYears:','').replace('.0','')[0:-1])),
                                (int(row[7].replace('last year:','').replace('.0',''))),
                                #Active or not
                                (TrueAsString in row[8].replace('active:',''))]
                                )
                                print((row[3]+ '-' + row[4]).replace('position:"','').replace('"','').replace("'",""))
                        
                            

