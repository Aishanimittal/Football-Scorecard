import sys
from tabulate import tabulate
from Player import *
from match import * 
from reports import *

def main():
    TEAMS=['fas_united', 'fas_madrid']
    while True:
        print()
        print("================Apeejay School Football League================")
        print("         ================Main Menu================          ")
        print()
        print("Player info..............1")
        print("Matches info.............2")
        print("Reports..................3")
        print("Quit.....................4")
        print()
        c = input("Enter your choice : ")
        print()
        if c == '1':
            while True:
                print("         ===============Player Menu===============          ")
                print()
                print("Add Player...............1")
                print("Delete Player............2")
                print("Modify Player............3")
                print("Search Player............4")
                print("List All Players.........5")
                print("Main Menu................6")
                print()
                ch = input("Enter your choice : ")
                print()
                if ch == '1' :
                    print("         ================Add Player Menu================          ")
                    print()
                    s = input("Enter Player Name : ")
                    t = input("Enter player's team [FAS_madrid,FAS_united] : ")
                    if t.lower() in TEAMS:
                        Add_pl(s,t)
                    else:
                        print("Wrong Team Input")
                    print()
                elif ch == '2':
                    print("         ============Delete Player Menu============         ")
                        
                    try:
                        I = int(input("Enter Player ID :"))
                        check = Search_pl(ID = I)
                        if check == None:
                            confirm = input("Do you wish to delete the above record (Y/N) : ")
                            if confirm == 'Y' or confirm == 'y':
                                Del_pl(ID = I)
                            else: 
                                continue
                        else:
                            print(check)
                    except ValueError:
                        print("Enter the value in integer format")
                    print()
                        
                elif ch == '3':
                    while True:
                        print("         ============Modify Player Menu============         ")
                        print()
                        print("Modify Goals Scored...............1")
                        print("Modify Yellow Cards Booked........2")
                        print("Modify Red Cards Booked...........3")
                        print("Previous Menu.....................4")
                        print()
                        choi = input("Enter Your Choice : ")
                        print()
                        if choi == '1' :
                            print()
                            try:
                                n = int(input("Enter Player ID : "))
                                check = Search_pl(ID = n)
                                if check == None:
                                    print()
                                    g = int(input("Enter no. of Goals to be modified (with sign) :"))
                                    print()
                                    Mod_pl(n, GS = g)
                                    print()
                                else:
                                    print()
                                    print(check)
                            except ValueError:
                                print("Enter the value in integer format")
                            print()
                        elif choi == '2':
                            print()
                            try:
                                n = int(input("Enter Player ID : "))
                                print()
                                check = Search_pl(ID = n)
                                if check == None:
                                    print()
                                    y = int(input("Enter no. of Yellow Cards to be modified(with sign) :"))
                                    print()
                                    Mod_pl(n, YC = y)
                                    print()
                                else:
                                    print()
                                    print(check)
                                    print()
                            except ValueError:
                                print("Enter the value in integer format")
                        elif choi == '3':
                            print()
                            try:
                                n = int(input("Enter Player ID : "))
                                print()
                                check = Search_pl(ID = n)
                                print()
                                if check == None:
                                    print()
                                    r = int(input("Enter no. of Red Cards to be modified(with sign) :"))
                                    print()
                                    Mod_pl(n, RC = r)
                                else:
                                    print()
                                    print(check)
                            except ValueError:
                                print("Enter the value in integer format")
                            print()
                        elif choi == '4':
                            break
                        else:
                            print("Wrong Input")
                elif ch == '4':
                    while True:
                        print("         ============Search Player Menu============         ")
                        print()
                        print("Search Player through Name...........1")
                        print("Search Player through ID.............2")
                        print("Previous Menu........................3")
                        print()
                        choic = input("Enter Your Choice :")
                        print()
                        if choic == '1':
                            print()
                            n = input("Enter Player Name :")
                            print()
                            check = Search_pl(Name = n)
                            if check != None:
                                print(check)
                            print()
                        elif choic == '2':
                            print()
                            try:
                                I = int(input("Enter Player ID :"))
                                print()
                                check = Search_pl(ID = I)
                                if check != None :
                                    print(check)
                            except ValueError:
                                print("Enter the value in integer format")
                            print()
                        elif choic == '3':
                            break
                        else:
                            print("Wrong Choice")
                elif ch == '5':
                    while True:
                        print("         ===========List All Player Menu===========         ")
                        print()
                        print("List All Players of all Teams................1")
                        print("List Players of a Specific Team..............2")
                        print("Previous Menu................................3")
                        print()
                        choice = input("Enter your Choice:")
                        print()
                        if choice == '1':
                            print()
                            List_all()
                            print()
                        elif choice == '2':
                            print()
                            t = input("Enter Team Name:")
                            if t.lower() in TEAMS:
                                List_all(Team = t)
                            else:
                                print("Wrong Team Input")
                            print()
                        elif choice == '3':
                            break
                        else:
                            print("Wrong Choice")
                elif ch == '6':
                    break
                else:
                    print("Wrong Input")
        elif c == '2':
            while True:
                print("         ===============Matches Menu===============         ")
                print()
                print("Add Match info...............1")
                print("Update Match info............2")
                print("Delete Match info............3")
                print("View All Matches.............4")
                print("Search a Match...............5")
                print("Main Menu....................6")
                print()
                ch = input("Enter Your Choice :")
                print()
                if ch == '1':
                    print("         ===============Add Match Menu===============         ")
                    print()
                    print("Enter date int the format ['yyyy-mm-dd'] ")
                    d = input("Enter the date :")
                    flag = date(d)
                    if flag :
                        check = search_match(d)
                        if check != None:
                            print()
                            try:
                                t1 = int(input("Enter FAS United's score :"))
                                t2 = int(input("Enter FAS Madrid's score :"))
                                if t1 > t2:
                                    result = 'FAS_United'
                                elif t2 > t1:
                                    result = 'FAS_Madrid'
                                else:
                                    result = 'Draw'
                                add_match(d,t1,t2,result)
                            except ValueError:
                                print("Enter the value in integer format")
                        else:
                            print("Record Already Exists")
                    else:
                        print("Wrong Date Format Input")
                elif ch == '2':
                    while True:
                        print()
                        print("         ===============Update Match Menu===============         ")
                        print()
                        print("Update FAS United's Score...........1")
                        print("Update FAS Madrid's Score...........2")
                        print("Previous Menu.......................3")
                        print()
                        cho = input("Enter Your Choice :")
                        print()
                        if cho == '1':
                            print()
                            print("Enter date int the format ['yyyy-mm-dd'] ")
                            d = input("Enter the date of the match to be updated :")
                            flag = date(d)
                            if flag:
                                s = search_match(d)
                                if s == None:
                                    try:
                                        t1 = int(input("Enter FAS United's updated score :"))
                                        Update_mat(d, T1 = t1)
                                    except ValueError:
                                        print("Enter the value in integer format")
                                else:
                                    print(s)
                                print()
                            else:
                                print("Wrong Date Format Input")
                        elif cho == '2':
                            print("Enter date int the format ['yyyy-mm-dd'] ")
                            d = input("Enter the date of the match to be updated :")
                            flag = date(d)
                            if flag:
                                s = search_match(d)
                                if s == None:
                                    try:
                                        t2 = int(input("Enter FAS Madrid's updated score :"))
                                        Update_mat(d, T2 = t2)
                                    except ValueError:
                                        print("Enter the value in integer format")
                                else:
                                    print(s)
                            else:
                                print("Wrong Date Format Input")
                        elif cho == '3':
                            break
                        else:
                            print("Wrong Input")
                elif ch == '3':
                    print()
                    print("         ===============Delete Match Menu===============         ")
                    print()
                    print("Enter date int the format ['yyyy-mm-dd'] ")
                    d = input("Enter the date of the match to be deleted :")
                    flag = date(d)
                    if flag:
                        s = search_match(d)
                        if s == None:
                            confirm = input("Do you wish to Delete the above record (Y/N) : ")
                            if confirm == 'Y' or confirm == 'y':
                                del_match(d)
                            else:
                                continue
                        else:
                            print(s)
                    else:
                        print("Wrong Date Format Input")
                    print()
                elif ch == '4':
                    print()
                    print("         ===============All Matches Menu===============         ")
                    see_all_matches()
                    print()
                elif ch == '5':
                    print()
                    print("         ===============Search Matches Menu===============         ")
                    print()
                    print("Enter date int the format ['yyyy-mm-dd'] ")
                    d = input("Enter the date of the match to be viewed :")
                    flag = date(d)
                    if flag:
                        s = search_match(d)
                        if s == None:
                            print()
                        else:
                            print(s)
                        print()
                    else:
                        print("Wrong Date Format Input")
                elif ch == '6':
                    break
                else:
                    print("Wrong Choice")
        elif c == '3':
            while True:
                print("Team Points..............1")
                print("Team Wins................2")
                print("Team Loss................3")
                print("Team Draws...............4")
                print("Most Goals Scored........5")
                print("Most Yellow Cards........6")
                print("Most Red Cards...........7")
                print("Overall Team Stats.......8")
                print("Main Menu................9")
                print()
                ch = input("Enter your choice :")
                print()
                if ch == '1':
                    print()
                    print("         ===============Team Points Menu===============         ")
                    print()
                    t = input("Enter team name (FAS_United/FAS_Madrid) :")
                    if t.lower() in TEAMS:
                        p = team_points(t)
                        print("Points = ",p)
                    else:
                        print("Wrong Team Input")
                    print()
                elif ch == '2':
                    print()
                    print("         ===============Team Wins Menu===============         ")
                    print()
                    t = input("Enter team name (FAS_United/FAS_Madrid) :")
                    if t.lower() in TEAMS:
                        w = team_wins(t)
                        print("No. of wins = ", w)
                    else:
                        print("Wrong Team Input")
                    print()
                elif ch == '3':
                    print()
                    print("         ===============Team Loss Menu===============         ")
                    print()
                    t = input("Enter team name (FAS_United/FAS_Madrid) :")
                    if t.lower() in TEAMS:
                        l = team_loss(t)
                        print("No. of losses = ", l)
                    else:
                        print("Wrong Team Input")
                    print()
                elif ch == '4':
                    print()
                    print("         ===============Team Draws Menu===============         ")
                    print()
                    t = input("Enter Team name (FAS_United/FAS_Madrid) :")
                    if t.lower() in TEAMS:
                        d = team_draws()
                        print("No. of draws =", d)
                    else:
                        print("Wrong Team Input")
                    print()
                elif ch == '5':
                    while True:
                        print()
                        print("         ===============Most Goals Menu===============         ")
                        print()
                        print("Overall Most scorer............1")
                        print("Team Best Scorer...............2")
                        print("Previous Menu..................3")
                        print()
                        cho = input("Enter Your Choice :")
                        print()
                        if cho == '1':
                            print()
                            g = max_goals()
                            print(tabulate(g, headers=['Name',"Goals","Team"], tablefmt = 'double_grid'))
                            print()
                        elif cho == '2':
                            print()
                            team = input("Enter Team (FAS_United/FAS_Madrid) :")
                            if team.lower() in TEAMS:
                                g = max_goals(team)
                                print(tabulate(g, headers=['Name',"Goals","Team"], tablefmt = 'double_grid'))
                            else:
                                print("Wrong Team Input")
                            print()
                        elif cho == '3':
                            break
                        else:
                            print("Wrong Choice")
                elif ch == '6':
                    while True:
                        print()
                        print("         ===============Most Yellow Cards Menu===============         ")
                        print()
                        print("Overall Most Yellow Card Booked............1")
                        print("Player with Most Yellow Card in a Team.....2")
                        print("Previous Menu..............................3")
                        print()
                        cho = input("Enter Your Choice :")
                        print()
                        if cho == '1':
                            print()
                            y = max_yc()
                            print(tabulate(y, headers=['Name',"Yellow Cards","Team"], tablefmt = 'double_grid'))
                            print()
                        elif cho == '2':
                            print()
                            team = input("Enter Team (FAS_United/FAS_Madrid) :")
                            if team.lower() in TEAMS:
                                y = max_yc(team)
                                print(tabulate(y, headers=['Name',"Yellow Cards","Team"], tablefmt = 'double_grid'))
                            else:
                                print("Wrong Team Input")
                            print()
                        elif cho == '3':
                            break
                        else:
                            print("Wrong Choice")
                elif ch == '7':
                    while True:
                        print()
                        print("         ===============Most Red Cards Menu===============         ")
                        print()
                        print("Overall Most Red Card Booked.............1")
                        print("Player with Most Red Card in a Team......2")
                        print("Previous Menu............................3")
                        print()
                        cho = input("Enter Your Choice :")
                        print()
                        if cho == '1':
                            print()
                            r = max_rc()
                            print(tabulate(r, headers=['Name',"Red Cards","Team"], tablefmt = 'double_grid'))
                            print()
                        elif cho == '2':
                            print()
                            team = input("Enter Team (FAS_United/FAS_Madrid) :")
                            if team.lower() in TEAMS:
                                r = max_rc(team)
                                print(tabulate(r, headers=['Name',"Red Cards","Team"], tablefmt = 'double_grid'))
                            else:
                                print("Wrong Team Input")
                            print()
                        elif cho == '3':
                            break
                        else:
                            print("Wrong Choice")
                elif ch == '8':
                    print()
                    print("         ===============Overall Team Stats Menu===============         ")
                    print()
                    t = input("Enter team name (FAS_United/FAS_Madrid) :")
                    if t.lower() in TEAMS:
                        ovr(t)
                    else:
                        print("Wrong Team Input")
                    print()
                elif ch == '9':
                    break
                else:
                    print("Wrong Input")
        elif c == '4':
            sys.exit()
        else:
            print("Wrong Choice")

main()
