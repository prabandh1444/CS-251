from distutils.filelist import findall
import requests
from bs4 import BeautifulSoup
import sys
 
course = sys.argv[1]

# Making a GET request
r = requests.get('https://www.cse.iitb.ac.in/academics/courses.php')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html5lib')

n1 = soup.find_all('div',class_='collapsible-body')


l=['CUHK','DTU','Geneva','KAIST','NTU','NUS','SFU']
t=n1[4].find_all('table')
l1=[4,1,6,3,5,0,2]
str=''
j=0
for i in l1:
    p=t[i].find_all('td')
    found =False
    for line in p:
        if course in line.text:
            found=True
        if(found):
            str=str+l[j]+":"+prev.text+";"
            found=False
        prev=line
    j=j+1
if(str=='') or not course[2:].isnumeric():
     print('NOT FOUND')
else:
    print(str[:-1])
