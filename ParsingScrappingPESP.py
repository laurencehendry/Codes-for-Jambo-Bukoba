import requests # Import the request package 
import csv # Import the csv package
from bs4 import BeautifulSoup # Import the BeautifulSoup package
####################

export = csv.writer(open("File2013_grades.csv", "w")) # Define object "writer" named Export which can later be sued to write csv

################# Get page

url = requests.get('http://pesptz.org/index.php/book_delivery/bydistrict?lang=english&r_id=6') # Grab page
page = url.content # Store in a variable
soup = BeautifulSoup(page) # Read into soup
print("Print Soup")
print(soup) # Show code
soup.prettify() # Prettify code
print("Prettify Soup")
print(soup.prettify()) # Show prettifed code

links = soup.find_all('a') # Find all a

########################################
# Get data from first level
########################################

for link in links:
    print("Link")
    print(link) # We got it
    
for link in links:
    fullLink = link.get('href') #But there is still a lot of HTML code around it, use contents and get to get rid of it
    print("Clean link")
    print(fullLink)

# But we want only the links inside the table, so use tr
listlinks1 = [] 
trs = soup.find_all('tr')
for tr in trs:
    for link in tr.find_all('a'):
        fulllink = link.get ('href')
        print(fulllink) #print in terminal to verify results
        listlinks1.append(fulllink)
        
print(listlinks1) # But there are still many links that we do not want, so comprehense the list and keep only the right ones
listlinks1 = [x for x in listlinks1 if "http://pesptz.org/index.php/book_delivery/byschool?lang=english&d_id=" in x]
print(listlinks1) # Now this a good list. We will use it to get data from the pages the links direct to

##########################
# Get data from second level
##########################

listlinks2 = []
for pages in listlinks1:
    url = requests.get(pages) 
    page = url.content
    print("Nex website!1")
    soup = BeautifulSoup(page) 
    trs = soup.find_all('tr')
    for tr in trs:
        for link in tr.find_all('a'):
            fulllink = link.get ('href')
            print(fulllink) #print in terminal to verify results
            listlinks2.append(fulllink)
        
print(listlinks2) # But there are still many links that we do not want, so comprehense the list and keep only the right ones
listlinks2 = [x for x in listlinks2 if "http://pesptz.org/index.php/book_delivery/bystandard?lang=english&s_id=" in x]
print("Now comes the clean list")
print(listlinks2) # Now this a good list. We will use it to get data from the pages the links direct to

###################################
# Get content
###################################

# With this, we are at the content level. All we need to do now is get the content from the cells and the header so that we know what is what
listcontents1 = []
for pages in listlinks2:
    url = requests.get(pages) 
    page = url.content
    soup = BeautifulSoup(page)
    print("Nex website!1")
    for tds in soup.find_all('td'): # Not a very elegant way but it works
        print("tds!!!!!!!!!!!1")
        print(tds.prettify())
        listcontents1.append(tds)
        
        
print(listcontents1)
export.writerow(listcontents1)
# print("Now comes the list!!!!!!!!!!!!!!!!!!!!!")     
# print(listcontents1)