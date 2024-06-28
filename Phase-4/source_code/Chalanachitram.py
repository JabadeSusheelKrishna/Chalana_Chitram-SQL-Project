import subprocess as sp
import pymysql
import pymysql.cursors

def insert():
    try:
        row = {}
        print("Please Enter where you want to enter the Data in ")
        print("1.MOVIES")
        print("2.ASSISTANT_DIRECTORS")
        print("3.Actors")
        print("4.Actor_Names")
        print("5.Awards")
        print("6.Characters")
        print("7.DISTRIBUTIONS")
        print("8.Director")
        print("9.Events")
        print("10.PRODUCER")
        print("11.Songs")
        print("12.Songs_Names")

        some = (int(input()))
        if(some == 1):
            print("You Are Entering In Movies Table :- ")
            name = input("Enter Movie Name : ")
            Budget = int(input("Enter The Budjet : "))
            Censor = input("Enter Movie Censor : ")
            Language = input("Enter Movie Language : ")
            Collection = int (input("Enter Movie Collection : "))
            Year = int(input("Enter year : "))
            Hit_Flop = int (input("Enter Movie Hit/Flop : "))
            Production = input("Enter Movie Production : ")
            Duration = int(input("Enter Movie Duration : "))
            Actor_id = int (input("Enter Movie Actor id : "))
            Song_id = int (input("Enter Movie Actor Song id : "))

            query = "INSERT INTO MOVIES VALUES ('%s', %d, '%s', '%s', %d, %d, %d, '%s', %d, %d, %d)" % (name, Budget, Censor, Language, Collection, Year, Hit_Flop, Production, Duration, Actor_id, Song_id)
            cur.execute(query)
            con.commit()

            print("Inserted Into Database")

        elif(some == 2):
            print("You are entering in Assistant Directors")
            row['D_id'] = int(input("Enter D_id of Assistant"))
            row['fname'] = input("Enter Fname of Assistant : ")
            row['mname'] = input("Enter Mname of Assistant : ")
            row['lname'] = input("Enter Lname of Assistant : ")
            row['Department'] = input("Enter department of Assistant : ")
            row['work'] = input("Enter work od Assistant: ")

            query = "INSERT INTO ASSISTANT_DIRECTORS VALUES (%d, '%s', '%s' , '%s', '%s', '%s')" % (row['D_id'], row['fname'], row['mname'], row['lname'], row['Department'], row['work'])
            cur.execute(query)
            con.commit()

            print("Inserted Into Database")

        elif(some == 3):
            print("You are entering in Actors")
            name = (input("Enter Name of Actor as F_Name M_Name L_Name: ")).split(' ')
            row["F_Name"] = name[0]
            row["M_Name"] = name[1]
            row["L_Name"] = name[2]
            row["EXPERIENCE"] = int(input("Experience : "))
            row["Upcoming"] = input("Upcoming Movies : ")
            row["Best_Role"] = input("Best role of Actor : ")
            row["Actor_ID"] = int(input("Actor_ID"))
            query = "INSERT INTO Actors(F_Name,M_Name,L_Name,EXPERIENCE,Upcoming,Best_Role,Actor_ID) VALUES('%s','%s','%s',%d,'%s','%s',%d)" % (
                row["F_Name"], row["M_Name"], row["L_Name"], row["EXPERIENCE"], row["Upcoming"], row["Best_Role"], row["Actor_ID"])
                
            cur.execute(query)
            con.commit()
            print("Inserted Into Database")
        elif(some == 4):
            print("You are entering in Actor_Names")
            f_name = input("Enter f_name of Actor_Names : ")
            m_name = input("Enter m_name of Actor_Names : ")
            l_name = input("Enter l_name of Actor_Names : ")
            Actor_id = int (input("Enter Actor id : "))
            query= "INSERT INTO Actor_Names('%s','%s','%s',%d)" % (f_name,m_name,l_name,Actor_id)
            cur.execute(query)
            con.commit()
            print("Inserted Into Database")

        elif(some == 5):
            print("You are Entering in Awards")
            Name = input("Enter fname of Actor : ")
            Year = int (input("Enter Year : "))
            level = input("Enter level : ")
            No_of_films = int(input("Enter no of films : "))

            query = "INSERT INTO Awards VALUES ('%s', %d, '%s', %d)" % (Name, Year, level, No_of_films)
            cur.execute(query)
            con.commit()
            print("Inserted Into Database")

        elif(some == 6):
            print("You are entering in CharActers")
            Char_Id = int(input("Enter The Character Id : "))
            Name = input("Enter fname of Actor : ")
            Movie = input("Enter Movie Name : ")
            Specials = input("Enter Special of Character : ")
            A_ID = int(input("Enter Actor id : "))
            query = "INSERT INTO Characters VALUES (%d,'%s','%s','%s',%d)" % (Char_Id,Name,Movie,Specials,A_ID)         
            cur.execute(query)
            con.commit()

            print("Inserted Into Database")
        
        elif(some == 7):
            print("You are entering in Distributions")
            fname = input("Enter fname of Distributors : ")
            mname = input("Enter mname of Distributors : ")
            fname = input("Enter fname of Distributors : ")
            Theatre_count = int(input("Enter theatre count of Distributions : "))
            OTT = input("Enter OTT od Disributors : ")
            Release_date = input("Enter the release date of distribution : ")
            
            query = "INSERT INTO DISTRIBUTIONS VALUES ('%s', '%s', '%s',%d, '%s', '%s')" % (fname, mname, fname, Theatre_count, OTT, Release_date)

        elif(some == 8):
            print("You are entering in Director")
            name = (input("Enter Name of Director as F_Name M_Name L_Name: ")).split(' ')
            row["F_Name"] = name[0]
            row["M_Name"] = name[1]
            row["L_Name"] = name[2]
            row["DIRECTOR_ID"] = int(input("Director_ID : "))
            row["EXPERIENCE"] = int(input("Experience : "))
            row["HITS_FLOPS"] = float(input("HITS_FLOPS : "))
            row["Best_Movie"] = input("Best_Movie of Director : ")
            row["Upcoming"] = input("Upcoming Films : ")
            row["Films"] = int(input("Enter the number of films of the director : "))
            query = "INSERT INTO Director(F_Name,M_Name,L_Name,DIRECTOR_ID,EXPERIENCE,HIT_FLOPS,Best_Movie,Upcoming,Films) VALUES('%s','%s','%s',%d,%d,%f,'%s','%s',%d)" % (
                row["F_Name"], row["M_Name"], row["L_Name"],row["DIRECTOR_ID"],row["EXPERIENCE"],row["HITS_FLOPS"],row["Best_Movie"],row["Upcoming"],row["Films"])
            
            cur.execute(query)
            con.commit()
            print("Inserted Into Database")
            
        elif(some == 9):
            print("You are entering in Events")
            Name = input("Enter name of Event : ")
            date = input("Enter date of Event : ")
            Budget = int(input("Enter Budget of Event : "))
            Guest = input("Enter Guest of Event : ")
            Location = input("Enter location of Event : ")

            query = "INSERT INTO Events VALUES ('%s', '%s', %d, '%s', '%s')" % (Name, date, Budget, Guest, Location)
            cur.execute(query)
            con.commit()

            print("Inserted Into Database")

        elif(some == 10):
            print("You are entering in Producers")
            name = (input("Enter Name of Actor as F_Name M_Name L_Name: ")).split(' ')
            row["fname"] = name[0]
            row["lname"] = name[1]
            row["mname"] = name[2]
            row["experience"] = int(input("Experience : "))
            row["production"] = input("Production : ")
            row["Hits_flop_ratio"] = float(input("Hits_flops_ratio"))
            row["Investment"] = int(input("Investment : "))
            query = "INSERT INTO PRODUCER VALUES ('%s', '%s', '%s', %d, '%s', %f, %d)" % (row[fname], row[lname], row[mname], row[experience], row[production], row[Hits_flop_ratio], row[Investment])
            cur.execute(query)
            con.commit()

            print("Inserted Into Database")
            
        elif(some == 11):
            print("You are entering in Songs")
            Music_Director = input("Enter Music_Director of song : ")
            Singer = input("Enter Singer of song : ")
            Song_ID = int(input("Enter Song_ID of song : "))
            
            query = "INSERT INTO Songs VALUES ('%s','%s', %d)" % (Music_Director,Singer,Song_ID)
            cur.execute(query)
            con.commit()

            print("Inserted Into Database")
            
        elif(some == 12):
            print("You are entering in Song_Names")
            Name = input("Enter Name of Song_name : ")
            Lyrics = input("Enter lyrics of song_name : ")
            Music_Director = input("Enter Music_director of Song_name : ")
            Media = input("Enter media mode of Song_name : ")
            
            query = "INSERT INTO Songs_Names VALUES ('%s', '%s', '%s', '%s')" % (Name, Lyrics, Music_Director, Media)
            cur.execute(query)
            con.commit()

            print("Inserted Into Database")
            
    except Exception as f:
        con.rollback()
        print("::::::::::::Failed to insert into database::::::::::")
        print(">>>>>>>>>>>>>", f)

def delete():
    try:
        print("Please Enter where you want to Delete the Data in ")
        print("1.MOVIES")
        print("2.ASSISTANT_DIRECTORS")
        print("3.Actors")
        print("4.Actor_Names")
        print("5.Awards")
        print("6.Characters")
        print("7.DISTRIBUTIONS")
        print("8.Director")
        print("9.Events")
        print("10.PRODUCER")
        print("11.Songs")
        print("12.Songs_Names")

        some = int(input("Enter Your Choice Number : "))

        if(some == 1):
            q = input("Enter the Name ")
            query = "DELETE from MOVIES WHERE Name='%s'" % (q)
            
            cur.execute(query)
            con.commit()
            
        elif(some == 2):
            f = input("Enter the fname of Assistant Director")
            m = input("Enter the mname of Assistant Director")
            l = input("Enter the lname of Assistant Director")

            query = "DELETE from ASSISTANT_DIRECTORS WHERE fname = '%s' AND mname = '%s' AND lname = '%s'" % (f,m,l)
            cur.execute(query)
            con.commit()

        elif(some == 3):
            f = input("Enter Fname of Actor")
            m = input("Enter Mname of Actor")
            l = input("Enter Lname of Actor")
            
            query = "DELETE from Actors WHERE F_Name = '%s' AND M_Name = '%s' AND L_Name = '%s'" % (f,m,l)
            cur.execute(query)
            con.commit()

        elif(some == 4):
            f = input("Enter Original fNames")
            m = input("Enter Orginal Mname")
            l = input("ENter Original lName")

            query = "DELETE FROM Actors_Names WHERE O_FName = '%s' AND O_MName = '%s' AND O_LName = '%s'" % (f,m,l)
            cur.execute(query)
            con.commit()
            
        elif(some == 5):
            name = input("Enter Award Name ")
            
            query = "DELETE FROM Awards WHERE Name = '%s'" % (name)
            cur.execute(query)
            con.commit()

        elif(some == 6):
            name = input("Enter the Charecter Name :")
            query = "DELETE FROM Characters WHERE Name = '%s'" % (name)
            cur.execute(query)
            con.commit()
            
        elif(some == 7):
            f = input("Enter Distributions fNames")
            m = input("Enter Distributions Mname")
            l = input("ENter Distributions lName")
            query = "DELETE FROM DISTRIBUTIONS WHERE fname = '%s' AND mname = '%s' AND lname = '%s'" %(f,m,l)
            cur.execute(query)
            con.commit()
            
        elif(some == 8):

            f = input("Enter the Director Fname")
            m = input("Enter the Director mname")
            l = input("Enter the Director lname")

            query = "DELETE FROM Director WHERE F_name = '%s' AND M_name = '%s' AND L_name = '%s'"%(f,m,l)
            cur.execute(query)
            con.commit()

        elif(some == 9):
            
            name = input("Enter Event name")
            query = "DELETE FROM Events WHERE Name = '%s'" % (name)
            cur.execute(query)
            con.commit()
            
        elif(some == 10):
            F= input ("Enter Producer F_Name ")
            M= input ("Enter Producer M_Name ")
            L= input ("Enter Producer N_Name ")
            query = "DELETE FORM PRODUCER WHERE fname = '%s' AND mname = '%s' AND lname = '%s'"%(F,L,M)
            cur.execute(query)
            con.commit()


        elif(some == 11):

            song_id= int(input("Enter Song ID"))

            query = "DELETE FROM Songs WHERE Song_ID = %d" % (song_id)
            cur.execute(query)
            con.commit()
            
        elif(some == 12):

            name = input("Enter song name")
            query = "DELETE FROM Songs_Names WHERE Name = '%s'" % (name)
            cur.execute(query)
            con.commit()
            

    except Exception as g:
        con.rollback()
        print("::::::::::::Failed to Delete from database:::::::::::")
        print(">>>>>>>>>>>>>", g)

def update():
    try:
        print("Please Enter where you want to Update the Data in ")
        print("1.MOVIES")
        print("2.ASSISTANT_DIRECTORS")
        print("3.Actors")
        print("4.Actor_Names")
        print("5.Awards")
        print("6.Characters")
        print("7.DISTRIBUTIONS")
        print("8.Director")
        print("9.Events")
        print("10.PRODUCER")
        print("11.Songs")
        print("12.Songs_Names")
        some = int(input("Enter Your Choice Number : "))
        attribute = input("Enter What you want to Update (Attributes)")
        val = input("Enter Value : ")

        if(some == 1):
            q = input("Enter the Name")
            query = "UPDATE MOVIES SET %s = '%s' WHERE Name = '%s'" % (attribute, val, query)
            cur.execute(query)
            con.commit()
            
        elif(some == 2):
            f = input("Enter the fname of Assistant Director")
            m = input("Enter the mname of Assistant Director")
            l = input("Enter the lname of Assistant Director")

            query = "UPDATE ASSISTANT_DIRECTORS SET %s = '%s' WHERE fname = '%s' AND mname = '%s' AND lname = '%s'" % (attribute,val,f,m,l)
            cur.execute(query)
            con.commit()

        elif(some == 3):
            f = input("Enter Fname of Actor")
            m = input("Enter Mname of Actor")
            l = input("Enter Lname of Actor")
            
            query = "UPDATE from Actors SET %s = '%s'  WHERE F_Name = '%s' AND M_Name = '%s' AND L_Name = '%s'" % (attribute,val,f,m,l)
            cur.execute(query)
            con.commit()

        elif(some == 4):
            f = input("Enter Original fName")
            m = input("Enter Original Mname")
            l = input("ENter Original lName")

            query = "UPDATE Actors_Names SET %s = '%s'  WHERE O_FName = '%s' AND O_MName = '%s' AND O_LName = '%s'" % (attribute,val,f,m,l)
            cur.execute(query)
            con.commit()
            
        elif(some == 5):
            name = input("Enter Award Name ")
            
            query = "UPDATE Awards set %s = '%s' WHERE Name = '%s'" % (attribute,val,name)
            cur.execute(query)
            con.commit()

        elif(some == 6):
            name = input("Enter the Character NAme :")
            query = "UPDATE Characters SET %s = '%s' WHERE Name = '%s'" % (attribute,val,name)
            cur.execute(query)
            con.commit()
            
        elif(some == 7):
            f = input("Enter Distributions fNames")
            m = input("Enter Distributions Mname")
            l = input("ENter Distributions lName")
            query = "UPDATE DISTRIBUTIONS SET %s = '%s' WHERE fname = '%s' AND mname = '%s' AND lname = '%s'" %(attribute, val, f,m,l)
            cur.execute(query)
            con.commit()
            
        elif(some == 8):

            f = input("Enter the Director Fname")
            m = input("Enter the Director mname")
            l = input("Enter the Director lname")

            query = "UPDATE Director SET %s = '%s' WHERE F_Name = '%s' AND M_Name = '%s' AND L_Name = '%s'"%(attribute,val,f,m,l)
            cur.execute(query)
            con.commit()

        elif(some == 9):
            
            name = input("Enter Event name")
            query = "UPDATE Events set %s = '%s' WHERE Name = '%s'" % (attribute, val, name)
            cur.execute(query)
            con.commit()
            
        elif(some == 10):
            F= input ("Enter Producer F_Name ")
            M= input ("Enter Producer M_Name ")
            L= input ("Enter Producer N_Name ")
            query = "UPDATE PRODUCER SET %s = '%s' WHERE fname = '%s' AND lname = '%s' AND mname = '%s'"%(attribute,val,F,M,L)
            cur.execute(query)
            con.commit()


        elif(some == 11):

            song = int(input("ENter Song ID"))

            query = "UPDATE Songs SET %s = '%s' WHERE Song_ID = %d" % (attribute, val, song)
            cur.execute(query)
            con.commit()
            
        elif(some == 12):

            name = input("Enter song name")
            query = "UPDATE Songs_Names SET %s = '%s' WHERE Name = '%s'" % (attribute,val,name)
            cur.execute(query)
            con.commit()

    except Exception as h:
        con.rollback()
        print("::::::::::::Failed to Update from database:::::::::::")
        print(">>>>>>>>>>>>>", h)

def view():
    try:
        query = "SELECT * FROM MOVIES, PRODUCER WHERE Production = prodution and Name is not NULL order by Budget DESC LIMIT 10"
        query2 = "SELECT * FROM MOVIES JOIN PRODUCER ON prodution = Production order by Budget DESC LIMIT 10"
        cur.execute(query2)
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except Exception as i:
        con.rollback()
        print("::::::::::::Failed to view from database:::::::::::")
        print(">>>>>>>>>>>>>", i)

def Genre():
    try:
        g = input("Enter Genre name : ")
        query = "SELECT * FROM MOVIES, PRODUCER WHERE Genre = '%s' and Production = prodution" % (g)
        query2 = "SELECT * FROM MOVIES RIGHT JOIN PRODUCER ON Production = prodution WHERE Genre = '%s'" % (g)
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except Exception as j:
        con.rollback()
        print("::::::::::::Failed to Genre search from database:::::::::::")
        print(">>>>>>>>>>>>>", j)

def Actor():
    try:
        f = input("Enter actor's first name : ")
        query = "SELECT F_Name, M_Name, L_Name, EXPERIENCE, Upcoming, Best_Role FROM Actors WHERE F_Name = '%s'"%(f)
        cur.execute(query)
        rows = cur.fetchall()
        for row in rows:
            print(row)

    except Exception as k:
        con.rollback()
        print("::::::::::::Failed to Search Actor from database:::::::::::")
        print(">>>>>>>>>>>>>", k)

def Search():
    try:
        code = int(input("Details of Director = 0 and Movie = 1"))
        if(code == 0):
            name = input("Enter the Director Fname")
            query = "SELECT * FROM Director WHERE F_Name = '%s'" % (name)
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                print(row)
            
        elif(code == 1):
            name = input("Enter the Movie Name")
            query = "SELECT * FROM MOVIES where Name = '%s'" % (name)
            cur.execute(query)
            rows = cur.fetchall()
            for row in rows:
                print(row)
        else:
            print("Don't Play Games -_-")

    except Exception as l:
        con.rollback()
        print("::::::::::::Failed to Search from database:::::::::::")
        print(">>>>>>>>>>>>>", l)


def hireAnEmployee():
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new employee's details: ")
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Minit"] = name[1]
        row["Lname"] = name[2]
        row["Ssn"] = input("SSN: ")
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row["Address"] = input("Address: ")
        row["Sex"] = input("Sex: ")
        row["Salary"] = float(input("Salary: "))
        row["Dno"] = int(input("Dno: "))

        query = "INSERT INTO EMPLOYEE(Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Dno) VALUES('%s', '%c', '%s', '%s', '%s', '%s', '%c', %f, %d)" % (
            row["Fname"], row["Minit"], row["Lname"], row["Ssn"], row["Bdate"], row["Address"], row["Sex"], row["Salary"], row["Dno"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

def printall():
    query = "SELECT * FROM MOVIES"
    query1 = "SELECT * FROM Actors"
    query2 = "SELECT * FROM Characters"
    query3 = "SELECT * FROM Awards"
    query4 = "SELECT * FROM Director"
    query5 = "SELECT * FROM Actors_Names"
    query6 = "SELECT * FROM Songs"
    query7 = "SELECT * FROM Songs_Names"
    query8 = "SELECT * FROM Events"
    query9 = "SELECT * FROM PRODUCER"
    query10 = "SELECT * FROM ASSISTANT_DIRECTORS"
    query11 = "SELECT * FROM DISTRIBUTIONS"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute(query1)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute(query2)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute(query3)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute(query4)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute(query5)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute(query6)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute(query7)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute(query8)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute(query9)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute(query10)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.execute(query11)
    rows = cur.fetchall()
    for row in rows:
        print(row)



def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        insert()
    elif(ch == 2):
        delete()
    elif(ch == 3):
        update()
    elif(ch == 4):
        view()
    elif(ch == 5):
        Genre()
    elif(ch == 6):
        Actor()
    elif(ch == 7):
        Search()
    elif(ch == 8):
        printall()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hardcode username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user="root",
                              password=password,
                              db='CHALANACHITRAM',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world.
                print("1. Insertion")  # Insert new tuple.
                print("2. Deletion")  # Delete already present data.
                print("3. Updation")  # Update the tables and tuples.
                print("4. View Top 10 Rating and Budget")  # Show tuples based on rating and budget.
                print("5. Search Movie according to Genre") # We can search for movie of specific genres. 
                print("6. Actors Details")  # Print the details of actors.
                print("7. Searching Movie, Director")   # We print the movie and its respective Director.
                print("8. Print Every Table")
                print("9. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 9:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
