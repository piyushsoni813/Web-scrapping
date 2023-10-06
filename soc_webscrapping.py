import csv
import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://itc.gymkhana.iitb.ac.in/wncc/soc/')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

rows = []
fields = ['Project','URL','Mentors','Mentees']
projDetails = []


names = soup.find_all('p', class_='lead text-center font-weight-bold text-dark')
print(len(names))
for name in names:
    label = name.text

count=0
divs = soup.find_all('div', class_='rounded hover-wrapper pr-3 pl-3 pt-3 pb-3 bg-white')
print(len(divs))
for d in divs:
    rows.append([names[count].text.strip(),'https://itc.gymkhana.iitb.ac.in'+d.get('href')])
    count += 1

for row in rows:
    leads = []
    req = requests.get(row[1])
    soup = BeautifulSoup(req.content, 'html.parser')
    lists = soup.find_all('li')
    for l in lists:
        l1 = l.find('p', class_='lead')
        if l1 is not None:
            leads.append(l1.text)
    
    projDetails.append([row[0],row[1],','.join(leads[:len(leads)-1]),"'"+str(leads[len(leads)-1])+"'"])

# name of csv file 
filename = "SoC_Projects_Detail.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(projDetails)
