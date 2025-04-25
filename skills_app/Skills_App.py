################################################
#        Skills App --> SQL Training           #
################################################

# Import SQLite Module
import sqlite3

# Create Database and connect
db = sqlite3.connect("Skills_App.db")

# Setup The cursor
cr = db.cursor()

# create table
cr.execute("CREATE TABLE IF NOT EXISTS skills(name text, progress text, user_id integer)")

# commit and close method
def commit_and_close() :
    # Save (commit) Changes
    db.commit()

    # close Database
    db.close()
    print("Connection to Database was closed Seccesfully...!!")

# My User ID
uid = 1

# input message
input_message = """
What Do You Want To Do ?
"s" --> Show All Skills
"a" --> Add a New Skill
"d" --> Delete  a Skill
"u" --> Update skill Progress
"q" --> Quit The App
Choose Option : 
"""
# Input Option Choose
choice  =  input(input_message).strip().lower()


# command list
Valid = ("a", "s", "d", "u", "q")

# Define Methods

def show_skills():

    cr.execute(f"SELECT * FROM skills WHERE user_id = {uid}")

    result = cr.fetchall()

    print(f"you have {len(result)} skills")

    if len(result) > 0 :
        print("Showing skills with progress ...")

    for row in result :

        print(f"Skill --> {row[0]}")
        print(f"progress --> {row[1]}%")
        print("------------------")
    

    commit_and_close() 

def add_skills():
    sk = input("Enter the skill's name ").strip().capitalize()

    cr.execute(f"SELECT name FROM skills WHERE name = '{sk}' AND user_id = {uid}")

    result = cr.fetchone()

    if result != None:
        
        print("skill is already exists , you cant Add it")
        
        choice = input("would you like to update it? (yes/no)").strip().lower()

        if choice == "yes" :

            prog = input("Enter the new Skill Progress : ")

            cr.execute(f"UPDATE skills SET progress = '{prog}' WHERE name = '{sk}' AND user_id = {uid}")

            commit_and_close()

            return
        
        else :

            return

    prog = input("Enter the skill progress ").strip()

    cr.execute(f"INSERT INTO skills(name, progress, user_id) VALUES('{sk}', {prog}, {uid})")

    commit_and_close()
    
def delete_skills():

    sk = input("please select the skill you want to delete ").strip().capitalize()

    cr.execute(f"DELETE FROM skills WHERE name = '{sk}' AND user_id = {uid}")

    commit_and_close() 

def update_progress():

    sk = input("what is the skill you wish to update it's progress ? ").strip().capitalize()

    prog = input("Enter the new Skill Progress : ")

    cr.execute(f"UPDATE skills SET progress = \"{prog}\" WHERE name = '{sk}' and user_id = {uid}")
    commit_and_close() 





# Check if command not exists
while choice not in Valid:
    print(f"Invalid Choice \"{choice}\".. Please choose A Valid Option")
    choice  =  input(input_message).strip().lower()

if choice == "s" :
    show_skills()

elif choice == "a":
    add_skills()

elif choice == "d":
    delete_skills()

elif choice == "u":
    update_progress()

else :
    print("app is closed")
    commit_and_close() 
