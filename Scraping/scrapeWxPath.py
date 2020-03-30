from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv
import re

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
chrome_driver  = r"/Users/danielarcese/Downloads/chromedriver"
driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)


driver.get(r"https://www.pro-football-reference.com/players/B/BradTo00.htm")

#driver.find_element_by_xpath("""/html/body/div[2]/div[5]/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]/a""").click()

rows = driver.find_elements_by_id("all_passing")


#14x Pro Bowl
#3x All-Pro
#6x SB Champ
#3x MVP
#2007 AP Off. PoY
#2007 Bert Bell Award (Player of the Year)
#2009 AP Comeback Player
#2009 PFWA Comeback Player
#2010 AP Off. PoY
#Ap Def. PoY





rows2 = driver.find_elements_by_id("bling")

tableNames = ["all_passing", "all_passing_playoffs", "all_passing_advanced", "\
all_kitchen_sink_detailed_passing", "all_rushing_and_receiving ", "all_rushing_and_receiving_playoffs"]
#all_detailed_rushing_and_receiving

tableValues = [driver.find_elements_by_id(table) for table in tableNames]


for row in rows2:
    print(row.text)

driver.quit()

""" >>> for key in a_dict:
...     print(key, '->', a_dict[key])
...

color -> blue
fruit -> apple
pet -> dog """
with open('TB.csv', 'w', newline='') as csvWriteFile:
    spamwriter = csv.writer(csvWriteFile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

    for table in tableValues:
        spamwriter.writerow(tableNames[tableValues.index(table)])
        for row in table:
            spamwriter.writerow(row.text.split(' '))

#driver.quit()

