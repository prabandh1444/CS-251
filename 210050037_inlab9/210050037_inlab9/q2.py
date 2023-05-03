from calendar import c
from importlib.resources import contents
import sys
import csv
import sqlite3
import pandas as pd
state = sys.argv[1]
connection = sqlite3.connect('zipcodesDB.db')
con=connection.cursor()

con.execute("""CREATE TABLE zipcodesInfo(
                zip_code TEXT,
                latitude REAL,
                longitude REAL,
                city TEXT,
                state TEXT,
                country TEXT,
                PRIMARY KEY(`zip_code`))""")
file = open('zipcodes.csv')
contents_in_file=csv.reader(file)
inserter = "INSERT INTO zipcodesInfo(zip_code,latitude,longitude,city,state,country) VALUES(?, ?, ?, ?, ?, ?)"
con.executemany(inserter,contents_in_file)
connection.commit()
df = pd.read_csv ('zipcodes.csv')
l=[]
max_latitude=0
max_city=''
for index, row in df.iterrows():
    if(row['state']==state):
        if(row['latitude']>max_latitude):
            max_latitude=row['latitude']
            max_city=row['city']
for index, row in df.iterrows():
     if(row['state']==state):
        if(row['city']==max_city):
            l.append(row['zip_code']) 
l.sort()
str1=''
for i in l:
    if(len(str(i))==3):
        str1=str1+"00"+str(i)+","
    elif(len(str(i))==4):
        str1=str1+"0"+str(i)+","
    else:
        str1=str1+str(i)+','
if l==[]:
    print('NOT FOUND')
else:
    print(str1[:-1])


