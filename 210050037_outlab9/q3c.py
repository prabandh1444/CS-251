import sqlite3

connect = sqlite3.connect('ipl.db')

Ci = connect.execute(f'''SELECT SUM(runs_scored),striker FROM BALL_BY_BALL GROUP BY striker''').fetchall()
Ci.sort(key=lambda soc:(soc[0],soc[1]),reverse=True)
for i in range(0,20):
    name = connect.execute(f'''SELECT player_name FROM PLAYER WHERE player_id ='{Ci[i][1]}' ''').fetchall()
    print(Ci[i][1],name[0][0],Ci[i][0],sep=',')