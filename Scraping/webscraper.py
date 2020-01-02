from bs4 import BeautifulSoup
import requests
import json


url = 'https://www.pro-football-reference.com/players/B/BrunMa00.htm'
response = requests.get(url, timeout=5)
content = BeautifulSoup(response.content, "html.parser")



# finding values in a stat column example
# for tweet in content.findAll('td', attrs={"class": "right", "data-stat": "pass_att" }):
#  print(tweet.text.encode('utf-8'))


 
# for finding position example. its in the tag but then you need to add more logic
# metatags = content.find_all('meta',attrs={"name":"Description"})
# for tag in metatags:
#	print(tag)

#Make list of every player. 1st database has player name and their href to their stats page

#https://www.pro-football-reference.com/players/A/


#<a href="/players/Z/ZuttJe20.htm">Jeremy Zuttah</a> --> example href_str
# for each letter find all players and the relative path of their file and put that into a json file
player_list = []
letters = [chr(i) for i in range(ord('a'),ord('z')+1)]
for letter in letters:
    letter_capitalized = letter.capitalize()
    url =  "https://www.pro-football-reference.com/players" + "/" + letter_capitalized + "/"
    response = requests.get(url, timeout=25)
    content = BeautifulSoup(response.content, "html.parser")
    for href in content.findAll('a', href=True):
        href_str = str(href)
        if "players" in href_str and "title" not in href_str: 
            try:  
                html_file_start_index = href_str.index("/" + letter_capitalized + "/") 
                html_file_end_index = href_str.index('.htm"')
                #print(href_str[html_file_start_index:html_file_end_index+4])
                closing_a_tag_index = href_str.index("</a>")
                player_name = href_str[html_file_end_index+6:closing_a_tag_index]
                #print(player_name)

                
                #<b><a href="/players/V/ValdMa00.htm">Marquez Valdes-Scantling</a> (WR)</b>
                if href.parent.name == 'b' or href.parent.name == 'p':
                    
                    
                    #<p><b><a href="/players/A/AbduAm00.htm">Ameer Abdullah</a> (RB)</b> 2015-2019</p>
                    if href.parent.name == 'b':
                        active = True
                        href_parent_parent_str = str(href.parent.parent)
                        pos_start = href_parent_parent_str.index("(")
                        pos_end = href_parent_parent_str.index(")")
                        pos = href_parent_parent_str[pos_start+1:pos_end]
                        years_start = href_parent_parent_str.index("</b>") + 4
                        years_end = href_parent_parent_str.index("</p>")
                        years_pre_filter = href_parent_parent_str[years_start:years_end]                        
                        hall_of_fame = False

                        
                    #<p><a href="/players/A/AbbeJo20.htm">Joe Abbey</a> (E) 1948-1949</p>
                    #<p><a href="/players/M/MackTo00.htm">Tom Mack</a>+ (G) 1966-1978</p> <- HOF example
                    #<p><a href="/players/A/AbruFr20.htm">Frank Abruzzino</a> (BB-LB-C-G-E-WB-DB) 1931-1933</p>
                    elif href.parent.name == 'p':
                        active = False
                        href_parent_str = str(href.parent)
                        pos_start = href_parent_str.index("(")
                        pos_end = href_parent_str.index(")")
                        pos = href_parent_str[pos_start+1:pos_end]
                        #years_start = href_parent_str.index(")") + 1
                        years_end = href_parent_str.index("</p>")
                        years_pre_filter = href_parent_str[pos_end+1:years_end] 
                                                
                        if "+" in href_parent_str :
                            hall_of_fame = True
                        else:
                            hall_of_fame = False
                    
                    else:
                        pass

                    years = years_pre_filter.replace(" ", "")
                    years_splitter = years.index("-")
                    first_year = int(years[0:years_splitter])
                    last_year = int(years[years_splitter+1:years_splitter+5])
                
                    player_object = {
                    "name": player_name,
                    "url": href_str[html_file_start_index:html_file_end_index+4],
                    "position": pos,
                    "hall of fame" : hall_of_fame,
                    "first year" : first_year,
                    "last year" : last_year,
                    "active" : active,
                    }             
                    player_list.append(player_object)
                    
            except: 
                pass
        else:
            pass
    print(letter + " done")

with open('player_list.json', 'w') as outfile:
    json.dump(player_list, outfile)





# then we scrape their stats page to find their position. this becomes the master database
# next we have a database per position so well check the masterdatabase and then run a script that
# scrapes for one position at a time and puts them into their own seperate databases but the players in the master will be linked to their
# positional database which will have position specific stats
# then we work on the machine learning/ predictive algorithms
# then go back the ui