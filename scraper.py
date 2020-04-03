from requests import get
from bs4 import BeautifulSoup
import csv

#url from which the data for coronavirus is scraped. 
world_url="https://www.worldometers.info/coronavirus/"
india_url="https://www.business-standard.com/article/current-affairs/coronavirus-in-numbers-latest-covid-19-cases-and-deaths-in-india-and-world-120031600116_1.html"



#sends request to the site and check the status
def connect():
    global worldr
    worldr=get(world_url)
    #check whether success



#function to scrape the web
def scrape():
    #parses html from request and navigates to the main table
    soup=BeautifulSoup(worldr.content,'html.parser')
    soup=soup.find('table',id='main_table_countries_today')

    #row list to write to csv files
    rows=[]
    row=[]

    #for table head
    tablehead=soup.thead.tr.find_all('th')
    for headings in tablehead:
        row.append(str(headings.text))
    rows.append(row)
    row=[]

    #for total data
    total=soup.find_all('tbody')[1].find_all('td')
    for numbers in total:
        row.append(str(numbers.text))
    rows.append(row)
    row=[]
    
    #for data of countries
    entries=soup.tbody.find_all('tr')
    for entry in entries:
        details=entry.find_all('td')
        for detail in details:
            row.append(str(detail.text))
        rows.append(row)
        row=[]

    return rows



#function to write the rows list to csv file
def writeToCsv(rows,path):
    
    with open(path+'corona_data_world.csv','w') as file:
        writer=csv.writer(file)
        writer.writerows(rows)



#function to read the rows list from csv file and return it
def readFromCsv(path):

    rows=[]
    with open(path+'corona_data_world.csv','r') as file:
        reader=csv.reader(file)
        for row in reader:
            rows.append(row)

    #this removes empty lists from the list
    rows = [x for x in rows if x != []]
    return rows