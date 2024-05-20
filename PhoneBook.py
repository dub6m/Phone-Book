import sqlite3

contacts = {}
isloaded = False
def menu():
        print("Press 1 to Add Contact");
        print("Press 2 to Update Contact");
        print("Press 3 to Delete Contact");
        print("Press 4 to Find Contact");
        print("Press 5 to Print Contacts");
        print("Press 6 to Load Contacts");
        print("Press 7 to Exit");

def getChoice():
        choice = int(input("Enter Choice:"))
        return choice; 
    
def execute(choice):
   
    global isloaded
    if  isloaded == False and choice != 6:        
        if choice == 7:
            print("exiting...")
        else:
            print("Load database")   
             
    else:   
        if choice == 1: 
            name = input("Enter Name:")
            phone = input("Enter Phone Number:")
            add(name, phone)
        elif choice == 2:
            name = input("Enter Name:")
            phone = input("Enter Phone Number:")
            update(name, phone)
        elif choice == 3:
            name = input("Enter Name:")        
            delete(name)        
        elif choice == 4:
            name = input("Enter Name:")
            find(name)
        elif choice == 5:
            printContact()
        elif choice == 6:
            
            if isloaded == False:
                load()
                print("loaded")
            else:
                print("Already loaded")
        elif choice == 7:
            print("exiting")
        else:
            print("invalid choice")  
       
def load():      
    global isloaded 
    isloaded = True
        
def printContact():

    conn = sqlite3.connect("phone.db")
    cursor = conn.cursor()   
    count = 0;
    
    for row in cursor.execute("SELECT * FROM contacts"):               
        print(row[0] + "\t" + row[1]) 
        count = count + 1
    if count== 0:
        print("Contact is Empty")    
    conn.close()
        
def update(name,phonenumber):
    conn = sqlite3.connect("phone.db")
    cursor = conn.cursor() 
    
    #check if contact exist before updating
    count = 0
    for row in cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
        count = count + 1
    if count > 0:     
        cursor.execute("UPDATE contacts SET phoneno = ?  WHERE name = ?",(phonenumber,name,))
        print("Updated")
    else:
        print("Name Does Not Exists")  
    
    conn.commit()
    conn.close()
def find(name):     
    conn = sqlite3.connect("phone.db")
    cursor = conn.cursor()   
    
    #check if contact exist before updating
    count = 0     
    for row in cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
        print(row[0] + "\t" + row[1]) 
        count = count + 1
    if count == 0:
        print("Not found")
        
    conn.close()
def add(name,phone):
   
    conn = sqlite3.connect("phone.db")
    cursor = conn.cursor()    
   
    #check for name exists before adding
    count = 0
    for row in cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
        count = count + 1
    if count== 0:     
        sql = ("INSERT INTO contacts (phoneno, name) VALUES (?, ?)")
        val = [(phone,name)]  
        cursor.executemany(sql,val)
        print("Added")
    else:
        print("Already Exists")
        
    conn.commit()
    conn.close()
    
        
    
def delete(name):
    conn = sqlite3.connect("phone.db")
    cursor = conn.cursor() 
    count = 0
    #check if contact exist before deleting
    for row in cursor.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
         count = count + 1
    if count > 0:     
        cursor.execute("DELETE FROM contacts WHERE name = ?",(name,))
        print("Deleted")
    else:
        print("Name Does Not Exists")
    
    conn.commit()
    conn.close()   
def createDB():
    conn = sqlite3.connect("phone.db")
    cursor = conn.cursor()         
    cursor.execute("CREATE TABLE IF NOT EXISTS contacts (name varchar(15) primary key, phoneno varchar(15))")
    conn.commit()
    conn.close()
        
    
    