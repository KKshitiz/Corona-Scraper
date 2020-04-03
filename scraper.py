import requests
from bs4 import BeautifulSoup
import csv

#url from which the data for coronavirus is scraped. 
world_url="https://www.worldometers.info/coronavirus/"
india_url="https://www.business-standard.com/article/current-affairs/coronavirus-in-numbers-latest-covid-19-cases-and-deaths-in-india-and-world-120031600116_1.html"
#gets the path of the directory where the file is kept
path=str(__file__).replace("\\","\\\\")[:-10]



def connect():

    worldr=requests.get(world_url)
    indiar=requests.get(india_url)
    print(worldr,indiar)



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
    
    entries=soup.tbody.find_all('tr')
    for entry in entries:
        details=entry.find_all('td')
        for detail in details:
            row.append(str(detail.text))
        rows.append(row)
        row=[]

    return rows

#function to write the rows list to csv file
def writeToCsv(rows):
    
    with open(path+'corona_data_world.csv','w') as file:
        writer=csv.writer(file)
        writer.writerows(rows)



#function to read the rows list from csv file and return it
def readFromCsv():

    rows=[]
    with open(path+'corona_data_world.csv','r') as file:
        reader=csv.reader(file)
        for row in reader:
            rows.append(row)
    return rows



if __name__ == "__main__":
    # rows=scrape()
    # writeToCsv(rows)
    print(readFromCsv())
