import sys
import mysql.connector
from tabulate import tabulate

def team_points(team):
    conobj = mysql.connector.connect(host='localhost',user='root',passwd='lovemysql#1234', database='school')
    if not conobj.is_connected():
        print("Unsuccessful Coneection")
        sys.exit()
    curobj = conobj.cursor()
    curobj.execute("select count(winner) from matches where winner = \"{}\"".format(team))
    data = curobj.fetchall()
    curobj.execute("select count(winner) from matches where winner = \'DRAW\'")
    d = curobj.fetchall()
    points = data[0][0]*3 + d[0][0]
    conobj.close()
    return points

def team_wins(team):
    conobj = mysql.connector.connect(host='localhost',user='root',passwd='lovemysql#1234', database='school')
    if not conobj.is_connected():
        print("Unuccessful Coneection")
        sys.exit()
    curobj = conobj.cursor()
    curobj.execute("select count(winner) from matches where winner = \"{}\"".format(team))
    data = curobj.fetchall()
    conobj.close()
    return data[0][0]

def team_loss(team):
    conobj = mysql.connector.connect(host='localhost',user='root',passwd='lovemysql#1234', database='school')
    if not conobj.is_connected():
        print("Unsuccessful Coneection")
        sys.exit()
    curobj = conobj.cursor()
    l = ['fas_madrid', 'fas madrid']
    if team.lower() in l :
        curobj.execute("select count(winner) from matches where winner = \"{}\"".format('FAS_United'))
    else:
        curobj.execute("select count(winner) from matches where winner = \"{}\"".format('FAS_Madrid'))
    data = curobj.fetchall()
    conobj.close()
    return data[0][0]

def team_draws():
    conobj = mysql.connector.connect(host='localhost',user='root',passwd='lovemysql#1234', database='school')
    if not conobj.is_connected():
        print("Unsuccessful Coneection")
        sys.exit()
    curobj = conobj.cursor()
    curobj.execute("select count(winner) from matches where winner = \'DRAW\'")
    d = curobj.fetchall()
    conobj.close()
    return d[0][0]

def  max_goals(team=None):
    conobj = mysql.connector.connect(host='localhost',user='root',passwd='lovemysql#1234', database='school')
    if not conobj.is_connected():
        print("Unsuccessful Coneection")
        sys.exit()
    curobj = conobj.cursor()
    if team == None:
        curobj.execute("select name , gs , team from player where gs = ( select max(gs) from player)")
    else:
        curobj.execute("select name , gs , team from player where gs = ( select max(gs) from player ) and team = \"{}\" ".format(team))
    data = curobj.fetchall()
    conobj.close()
    return data

def max_yc(team=None):
    conobj = mysql.connector.connect(host='localhost',user='root',passwd='lovemysql#1234', database='school')
    if not conobj.is_connected():
        print("Unsuccessful Coneection")
        sys.exit()
    curobj = conobj.cursor()
    if team == None:
        curobj.execute("select name , yc , team from player where yc = ( select max(yc) from player)")
    else:
        curobj.execute("select name , yc , team from player where yc = ( select max(yc) from player) and team = \"{}\" ".format(team))
    data = curobj.fetchall()
    conobj.close()
    return data

def max_rc(team=None):
    conobj = mysql.connector.connect(host='localhost',user='root',passwd='lovemysql#1234', database='school')
    if not conobj.is_connected():
        print("Unsuccessful Coneection")
        sys.exit()
    curobj = conobj.cursor()
    if team == None:
        curobj.execute("select name , rc , team from player where rc = ( select max(rc) from player)")
    else:
        curobj.execute("select name , rc , team from player where rc = ( select max(rc) from player ) and team = \"{}\" ".format(team))
    data = curobj.fetchall()
    conobj.close()
    return data

def ovr(team):
    conobj = mysql.connector.connect(host='localhost',user='root',passwd='lovemysql#1234', database='school')
    if not conobj.is_connected():
        print("Unsuccessful Coneection")
        sys.exit()
    curobj = conobj.cursor()
    p = team_points(team)
    w = team_wins(team)
    l = team_loss(team)
    d = team_draws()
    g = max_goals(team)
    y = max_yc(team)
    r = max_rc(team)
    list = [[team, w, d, l, p, g[0][0],g[0][1],y[0][0], y[0][1],r[0][0], r[0][1]]]
    print(tabulate(list,headers=['Name','Wins', 'Draws','Loss','Points','Top Scorer','Goals',\
        'Top Yellow Card Receiver','Yellow Cards','Top Red Card Receiver','Red Cards'],tablefmt='double_grid'))
    conobj.close()
