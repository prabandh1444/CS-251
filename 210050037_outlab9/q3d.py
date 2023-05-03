import sqlite3
import csv
connect = sqlite3.connect('ipl.db')

connect.execute("DROP TABLE IF EXISTS POINTS_TABLE;")
connect.execute('''CREATE TABLE POINTS_TABLE
         (team_id INT,
         team_name TEXT,
         points INT,
         nrr REAL);''')
cursor = connect.cursor()
file1 = open("team.csv")
next(file1)
rows1 = csv.reader(file1)
cursor.executemany("INSERT INTO POINTS_TABLE VALUES (?,?,0,0)", rows1)
file1.close()

c = connect.execute(f'''SELECT match_winner,team1,team2,win_type,win_margin FROM MATCH''').fetchall()
non_l=[]
for i in c:
    l=list(i)
    if(l[0]!='NULL'):
        if(int(l[0])==l[1]):
            l=l[1:]
        else:
            t=l[1]
            l[1]=l[2]
            l[2]=t
            l=l[1:]
    else:
        l=l[1:]
    non_l.append(l)
for i in non_l:
    if i[2]=='runs':
        connect.execute(f'''UPDATE POINTS_TABLE SET points = points+2, nrr=nrr+'{i[3]/20}' WHERE team_id ='{i[0]}' ''')
        connect.execute(f'''UPDATE POINTS_TABLE SET  nrr=nrr-'{i[3]/20}' WHERE team_id ='{i[1]}' ''')
    if i[2]=='wickets':
        connect.execute(f'''UPDATE POINTS_TABLE SET points = points+2, nrr=nrr+'{i[3]/10}' WHERE team_id ='{i[0]}' ''')
        connect.execute(f'''UPDATE POINTS_TABLE SET  nrr=nrr-'{i[3]/10}' WHERE team_id ='{i[1]}' ''')
    if i[2]=='Tie' or i[2]=='NA':
        connect.execute(f'''UPDATE POINTS_TABLE SET points = points+1 WHERE team_id ='{i[0]}' ''')
        connect.execute(f'''UPDATE POINTS_TABLE SET  points = points+1 WHERE team_id ='{i[1]}' ''')
j=connect.execute(f'''SELECT * FROM POINTS_TABLE''').fetchall()
j.sort(key=lambda soc:(soc[2],soc[3]),reverse=True)
for i in j:
    print(i[0],i[1],i[2],'%.2f' %i[3],sep=',')
