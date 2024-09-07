import mysql.connector
import sys
from tabulate import tabulate

def Add_pl(Name,Team):
    conobj = mysql.connector.connect(host='localhost',user='root',passwd='lovemysql#1234', database='school')
    if not conobj.is_connected():
        print("Unsuccessful Coneection")
        sys.exit()
    curobj = conobj.cursor()
    curobj.execute("Select * from player")
    data = curobj.fetchall()
    PID = data[-1][0]+1
    curobj.execute("Insert into player values({},\"{}\",{},{},{},\"{}\")".format(PID,Name,0,0,0,Team))
    conobj.commit()
    print("Record Added Successfully")
    conobj.close()

def Del_pl(ID):
    conobj = mysql.connector.connect(host="localhost", user="root", passwd="lovemysql#1234", database="school") 
    if not conobj.is_connected():
        print("Unsuccessful Connection")
        sys.exit()
    curobj = conobj.cursor()
    try:
         curobj.execute("Delete from player where player_id like {}".format(ID))
         conobj.commit()
    except:
        print(" ")
    else:
        print("Record Deleted Successfully")
    conobj.close()

def Mod_pl(ID,GS=0,YC=0,RC=0):
    conobj = mysql.connector.connect(host='localhost',user='root',passwd='lovemysql#1234',database='school')
    if not conobj.is_connected():
        print("Unsuccessful Connection")
        sys.exit()
    curobj = conobj.cursor()
    try:
        curobj.execute("Update player set GS = GS + {} , YC = YC + {}, RC = RC + {} where Player_ID = \"{}\"".format(GS,YC,RC,ID))
        conobj.commit()
    except:
        print(" ")
    else:
        print("Player successfully modified")
    conobj.close()

def Search_pl(Name=None , ID=None):
    conobj = mysql.connector.connect(host='localhost',user='root',passwd='lovemysql#1234',database='school')
    if not conobj.is_connected():
        print("Unsuccessful Connection")
        sys.exit()
    curobj = conobj.cursor()
    if Name == None:
        curobj.execute("select * from player where Player_id = {}".format(ID))
        data = curobj.fetchall()
        conobj.close()
        if data == []:
            s = "No record found"
            return s
        else:
            print(tabulate(data,headers=["Player_ID","Name","GS","YC","RC","Team"],tablefmt='double_grid'))
    else:
        curobj.execute("Select * from player where Name = \"{}\"".format(Name))
        data = curobj.fetchall()
        conobj.close()
        if data == []:
            s= "No record found"
            return s
        else:
            print(tabulate(data,headers=["Player_ID","Name","GS","YC","RC","Team"],tablefmt='double_grid'))
    
def List_all(Team=None):
    conobj = mysql.connector.connect(host='localhost',user='root',passwd='lovemysql#1234', database='school')
    if not conobj.is_connected():
        print("Unsuccessful Connection")
        sys.exit()
    curobj = conobj.cursor()
    if Team == None:
        curobj.execute("select * from player")
    else:
        curobj.execute("select * from player where team = \"{}\"".format(Team))
    data = curobj.fetchall()
    if data == []:
        print("No Record Found")
    else:
        print(tabulate(data,headers=["Player_ID","Name","GS","YC","RC","Team"],tablefmt='double_grid'))
    conobj.close()
