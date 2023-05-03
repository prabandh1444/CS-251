import sqlite3

connect = sqlite3.connect('ipl.db')

Ci=connect.execute(f'''SELECT venue_name FROM MATCH''').fetchall()

Ci = [*set(Ci)]

avg =[]
for i in Ci:
    l = connect.execute(f'''SELECT match_id FROM MATCH WHERE venue_name = '{i[0]}' ''').fetchall()
    avgr=0
    for j in l:
        t = connect.execute(f'''SELECT SUM(runs_scored+extra_runs) FROM BALL_BY_BALL WHERE match_id ='{j[0]}' ''').fetchall()
        if(t[0][0]!=None):
            avgr=avgr+t[0][0]
    avgr = avgr/len(l)
    avg.append([i[0],avgr])
avg.sort(key=lambda soc:(soc[1],soc[0]),reverse=True)
for i in avg:
    if(i[1]!=0):
        print(i[0],'%.2f' % i[1],sep=',')
