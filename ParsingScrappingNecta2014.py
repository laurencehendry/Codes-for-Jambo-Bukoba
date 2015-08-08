import requests # Import the request package 
import csv # Import the csv package
from bs4 import BeautifulSoup # Import the BeautifulSoup package
import time
####################

grades = csv.writer(open("File2014_grades.csv", "w")) # Define object "writer" named c which can later be sued to write csv
schools = csv.writer(open("File2014_schools.csv", "w")) # Define object "writer" named c which can later be sued to write csv
 
################# Get links from first page

url = r"C:/Users/Christopher/Google Drive/Python/Parsing/Necta 2014/index.html"
page = open(url)
soup = BeautifulSoup(page.read())

list1 = []
list2 = []
listx = []
for link in soup.find_all('a'):
    list1.append(link.get('href'))
    print(link.get('href'))
    list2.append(link.contents)
    print(link.contents)
    
print(list1)
string = 'C:/Users/Christopher/Google Drive/Python/Parsing/Necta 2014/'
newlist1 = [string + x for x in list1]
print(newlist1)
 
################# Get links from second page
list2 = []
 
 
for x in newlist1:
    url = x
    page = open(url)
    print("Nex website!1")
    soup = BeautifulSoup(page.read())
    for link in soup.find_all('a'):
        list2.append(link.get('href'))
        print(link.get('href'))
        print(link.contents)
        schools.writerow(link.contents)
        schools.writerow(link.get('href'))
     
print(list2)
string = 'C:/Users/Christopher/Google Drive/Python/Parsing/Necta 2014/results/'
newlist2 = [string + x for x in list2]
print(newlist2)
 
################# Get links from second third
list3 = []
 
for x in newlist2:
    url = x
    page = open(url)
    print("Nex website!2")
    soup = BeautifulSoup(page.read())
    for link in soup.find_all('a'):
        list3.append(link.get('href'))
        print(link.get('href'))
        print(link.contents)
        schools.writerow(link.contents)
        schools.writerow(link.get('href'))    
     
print(list3)
string = 'C:/Users/Christopher/Google Drive/Python/Parsing/Necta 2014/results/'
newlist3 = [string + x for x in list3]
print(newlist3)
 
############### Get actual data   

for x in newlist3:
    url = x
    page = open(url)
    print("Next website!3")
    soup = BeautifulSoup(page.read())
    school = soup.find_all('h3')
    print(school)
    grades.writerow(school)
    for trs in soup.find_all('tr'):
        tds = trs.find_all('td')
        row = [elem.text.strip().encode('utf-8') for elem in tds]
        grades.writerow(row)     
        print(row)
        