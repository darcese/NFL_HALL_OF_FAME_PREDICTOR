""" from bs4 import BeautifulSoup
html = open("divs.html").read()
soup = BeautifulSoup(html)
print soup.find(id='abc1') """

from bs4 import BeautifulSoup
import requests
import json
import re

url = "https://www.pro-football-reference.com/players/M/MannPe00.htm"
#url = "https://www.pro-football-reference.com/players/R/ReedEd00.htm"
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")


tableNames = ["all_passing", "all_passing_playoffs", "all_passing_advanced", "\
all_kitchen_sink_detailed_passing", "all_rushing_and_receiving ", "all_rushing_and_receiving_playoffs"]

#content.find(id=tableNames[0])

#print(content.find(id=tableNames[0]).text)





countedSameLineAccolades = ["MVP","Pro Bowl","All-Pro","SB Champ"]

#separateAccolades = Set("AP Off. PoY","AP Def. PoY")
backNumber = 4

""" if  "MVP" in text:
    allProIndex = text.index("MVP")
    allProTimesS= text[allProIndex-4:allProIndex]
    allProTimesN = int(re.sub("[^0-9]", "", allProTimesS))
    print(allProTimesN) """

for accolade in countedSameLineAccolades:
    if accolade in text:
        accoladeIndex = text.index(accolade)
        accoladeTimesPreFilter = text[accoladeIndex-backNumber: accoladeIndex]
        accoladeTimes = int(re.sub("[^0-9]", "", accoladeTimesPreFilter))
        print(accolade + " " + str(accoladeTimes))

""" if "Pro Bowl" in text:
    proBowlIndex = text.index("Pro Bowl")
    proBowlTimesS = text[proBowlIndex -4:proBowlIndex]
    proBowlTimesN = int(proBowlTimesS.replace('x','').replace(' ',''))
    print(proBowlTimesN)

if "All-Pro" in text:
    allProIndex = text.index("All-Pro")
    allProTimesS= text[allProIndex-4:allProIndex]
    allProTimesN = int(allProTimesS.replace('x','').replace(' ',''))
    print(allProTimesN)

if "SB Champ" in text:
    allProIndex = text.index("SB Champ")
    allProTimesS= text[allProIndex-4:allProIndex]
    allProTimesN = int(allProTimesS.replace('x','').replace(' ',''))
    print(allProTimesN)


if  "MVP" in text:
    allProIndex = text.index("MVP")
    allProTimesS= text[allProIndex-4:allProIndex]
    allProTimesN = int(re.sub("[^0-9]", "", "allProTimesS")
    print(allProTimesN)
"""

print("AP Off. PoY", text.count("AP Off. PoY"))
  

print("AP Def. PoY", text.count("AP Def. PoY"))
