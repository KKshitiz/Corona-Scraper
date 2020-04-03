import requests
from bs4 import BeautifulSoup

demo_url="http://example.webscraping.com/places/default/search"
world_url="https://www.worldometers.info/coronavirus/"
india_url="https://www.business-standard.com/article/current-affairs/coronavirus-in-numbers-latest-covid-19-cases-and-deaths-in-india-and-world-120031600116_1.html"
worldr=requests.get(world_url)
indiar=requests.get(india_url)
demor=requests.get(demo_url)
print(worldr,indiar)

def country_wise():

    #parses html from request and navigates to the main table
    soup=BeautifulSoup(worldr.content,'html.parser')
    soup=soup.find('table',id='main_table_countries_today')

    #for table head
    tablehead=soup.thead.tr.find_all('th')
    for headings in tablehead:
        print(headings.text,end=" ")
    print("\n")

    #for total data
    total=soup.find_all('tbody')[1].find_all('td')
    for numbers in total:
        print(numbers.text,end=" ")
    
    entries=soup.tbody.find_all('tr')
    for entry in entries:
        details=entry.find_all('td')
        for detail in details:
            print(detail.text,end=" ")
        print("\n")

def india():
    return


if __name__ == "__main__":
    country_wise()
