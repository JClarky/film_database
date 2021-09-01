import errorchecking as ec 
import database_control as dbc
import time

def print_db():
    for key, value in dbc.whole_db().items():
        for keyy, valuee in value.items():
            print(keyy, valuee)
        print("\n")

def add_db():
    input("Name: ")
    input("Year of release: ")
    input("Rating: ")
    input("Runtime: ")
    input("Genre: ")

def change_db(d):
    input("Would you like to edit the name, yor, rating, runtime or genre? ")
    input("Enter the fields new value: ")

def search_db():
    input("Enter the movie name or primary key: ")
    return 1

# Introduce database
print("\nWelcome to Jaydens Film Database")
time.sleep(1)
print("This is the current database:")
time.sleep(1)
print_db()

#
# MAIN LOOP
#

while True: 
    # Get user input on what they would like to do
    loop_ans = input("\nWould you like to (e)dit, (a)dd, (p)rint the database or (q)uit ").lower()

    # If the user wants to edit the database
    if loop_ans == "e": 
        # Search for movie to edit
        pk = search_db() 
            
        # Check if they would like to edit or delete movie  
        while True:
            edit_ans = input("\nWould you like to (e)dit this movie, (d)elete this movie? or (c)ancel ").lower()  
            # User wants to edit movie 
            if(edit_ans == "e"): 
                change_db(pk)        
                print("Succesfully edited movie")
                break
            # User wants to delete movie
            elif(edit_ans == "d"): 
                print("Succesfully deleted movie")
                break    
            # User wants to movie  
            elif(edit_ans == "c"): 
                break    
            else:
                print("Invalid input, try again (e, d or c)")
                
    # If the user wants to add to the database
    elif loop_ans == "a": 
        add_db()
        print("Succesfully added movie")
    # If the user wants to print the database
    elif loop_ans == "p": 
        print_db()
    # If the user want to quit the program   
    elif loop_ans == "q": 
        print("Thanks for using Jaydens Film Database")
        break
    # If the user entered an invalid input
    else:
        print("Invalid input, try again  (e, a, p or q)")


