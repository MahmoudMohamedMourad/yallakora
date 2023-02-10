import requests
from bs4 import BeautifulSoup
import csv 

date = input ("please enter a Date in the following format MM/DD/YYYY : ")
page = requests.get(f"https://www.yallakora.com/Match-Center/?date={date}")
matches_details=[]

def main (page) :
    srs = page.content 
    soup = BeautifulSoup(srs,"lxml")
    
    
    championships= soup.find_all("div", {'class':'matchCard'}) 
   
    def get_match_info(championships):
        global matches_details
        championship_title= championships.contents[1].find('h2').text.strip()
        all_matches=championships.contents[3].find_all('li')
        number_of_matches =len(all_matches)
      
        for i in range(number_of_matches):
            #get team numes
            team_A = all_matches[i].find('div',{'class':'teamA'}).text.strip()
            team_B = all_matches[i].find('div',{'class':'teamB'}).text.strip()
            
            
            # get score 
            match_result=all_matches[i].find('div',{'class':'MResult'}).find_all('span',{'class':'score'})
            score= match_result[0].text.strip() + " - " + match_result[1].text.strip()
            
            #get match tim 
            match_time =str(all_matches[i].find('div',{'class':'MResult'}).find('span',{'calss':'time'})).strip()
           #add match info to matches_detalis
            matches_details.append({"نوع البطوله":championship_title,"الفريق الاول":team_A,
            "الفريق الثاني":team_B ,"ميعاد المباره":match_time, "النتيجه":score})
    print(championships)
    for i in range(len(championships)):
        get_match_info(championships[i])
    print(matches_details)
         
    keys = matches_details[0].keys()
    keys = list(matches_details[0].keys())
    print(keys)
    with open('C:/Users/M/Desktop/work/yallakora/matches-details.csv','w', encoding="utf-8") as output_file:
      dict_witer=csv.DictWriter(output_file, fieldnames=keys)
      dict_witer.writeheader()
      dict_witer.writerows(matches_details[:])
      print("file created")
        
main(page)    