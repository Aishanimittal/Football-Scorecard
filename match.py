import mysql.connector
import sys
from tabulate import tabulate

def add_match(date,t1score,t2score,result):
    conobj = mysql.connector.connect(host='localhost',user='root',passwd='lovemysql#1234', database='school')
    if not conobj.is_connected():
        print("Unsuccessful Coneection")
        sys.exit()
    curobj = conobj.cursor()
    curobj.execute("Insert into matches values(\'{}\',{},{},\'{}\')".format(date,t1score,t2score,result))
    conobj.commit()
    print('Record added successfully')
    conobj.close() 

def Update_mat(Date,T1=None,T2=None):
    conobj = mysql.connector.connect(host='localhost', user='root',passwd='lovemysql#1234',database='school')
    if not conobj.is_connected():
        print("Unsuccessful Connection")
        sys.exit()
    curobj = conobj.cursor()
    curobj.execute("select * from matches where date_play = \"{}\"".format(Date))
    data = curobj.fetchall()
    conobj.commit()
    if T1 == None:
        if T2>data[0][1]:
            curobj.execute("update matches set FAS_Madrid = {}, winner = \"{}\" where date_play = \"{}\"".format(T2,"FAS_Madrid",Date))
        elif T2==data[0][1]:
            curobj.execute("update matches set FAS_Madrid = {}, winner = \"{}\" where date_play = \"{}\"".format(T2,"Draw",Date))
        else:
            curobj.execute("update matches set FAS_Madrid = {}, winner =\"{}\" where date_play =\"{}\"".format(T2,"FAS_United",Date))
    else:
        if T1>data[0][2]:
            curobj.execute("update matches set FAS_United = {}, winner = \"{}\" where date_play = \"{}\"".format(T1,"FAS_United",Date))
        elif T1==data[0][2]:
            curobj.execute("update matches set FAS_United = {}, winner = \"{}\" where date_play = \"{}\"".format(T1,"Draw",Date))
        else:
            curobj.execute("update matches set FAS_United = {}, winner = \"{}\" where date_play = \"{}\"".format(T1,"FAS_Madrid",Date))
    conobj.commit()
    conobj.close()
    print("Record Edited Successfully")

def del_match(date_):
    conobj = mysql.connector.connect(host='localhost',user='root',passwd='lovemysql#1234', database='school')
    if not conobj.is_connected():
        print("Unsuccessful Coneection")
        sys.exit()
    curobj = conobj.cursor()
    curobj.execute("DELETE FROM matches where date_play ='{}'".format(date_))
    conobj.commit()
    print('Record Deleted succesfully')
    conobj.close()

def see_all_matches():
    conobj = mysql.connector.connect(host='localhost',user='root',passwd='lovemysql#1234', database='school')
    if not conobj.is_connected():
        print("Unsuccessful Coneection")
        sys.exit()
    curobj = conobj.cursor()
    curobj.execute("SELECT * FROM matches")
    data=curobj.fetchall()
    print(tabulate(data,headers=["Date_Play","FAS_United","FAS_Madrid","Winner"],tablefmt='double_grid'))
    conobj.close()

def search_match(date_):
    conobj = mysql.connector.connect(host='localhost',user='root',passwd='lovemysql#1234', database='school')
    if not conobj.is_connected():
        print("Unsuccessful Coneection")
        sys.exit()
    curobj = conobj.cursor()
    curobj.execute("select * from matches where date_play = '{}'".format(date_))
    v=curobj.fetchall()
    conobj.close()
    if v == []:
        s= "No Record found"
        return s
    else:
        print(tabulate(v,headers=["Date_Play","FAS_United","FAS_Madrid","Winner"],tablefmt='double_grid'))

def date(d):
    flag = False
    m = ['01','02','03','04','05','06','07','08','09','10','11','12']
    da = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25',\
        '26','27','28','29','30',]
    if d[5:7] in m and d[8:] in da and ((d[4] and d[7]) == '-') :
        flag = True
    return flag
