import sqlite3

# update menu
#@eel.expose
#def update_men():
#eel.update_menu(menu)

# Connect to database
conn = sqlite3.connect("doctor.db")
cursor = conn.cursor()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def print_db(table_name):
    global cursor
    cursor.row_factory = dict_factory
    for row in cursor.execute('SELECT * FROM '+table_name):
        for key, value in row.items():
            print(key, value)


# Parse table name a tuple of values (name, id, etc)
def insert(table_name, values):
    global cursor, conn
    print("Successfully inserted")
    values = tuple(values)
    cursor.execute("INSERT INTO "+table_name+" VALUES (?,?,?,?,?,?)", values)
    conn.commit()

def amend(table_name, id):
    global cursor, conn
    val = cursor.execute('SELECT * FROM '+table_name+" WHERE ID="+id)
    print(val)
    
    field = input("Change which field? ").upper()
    newvalue = input("Enter the new value for this field: ")        

    cursor.execute("UPDATE "+table_name+" SET " + field + "=" + newvalue + " WHERE ID = " + id)
    conn.commit()
    
    print("\nRecord updated")
    print_db()

def delete(table_name, id):
    global cursor, conn
    cursor.execute("DELETE FROM "+table_name+" WHERE ID = " + id)
    conn.commit()
    
    print("\nRecord deleted")
    print_db()

def create_table():
    conn.execute('''CREATE TABLE patients
    (ID INTEGER,
    FIRST_NAME TEXT,
    LAST_NAME TEXT,
    SALARY TEXT,
    ADDRESS TEXT,
    JOIN_DATE TEXT);''')

#create_table()

table_name = "patients"
print_db(table_name)
user_ans = ""

#print(names)



"""while user_ans != "q":
    user_ans = input("Would you like to (p)rint, (i)nsert, (a)mend, (d)elete or (q)uit ").lower()
    if user_ans == "p":
        print_db(table_name)
    elif user_ans == "i":
        id = int(input("Patient ID: "))
        f_name = str(input("First name: "))
        l_name = str(input("Last name: "))
        salary = str(input("Salary: "))
        address = str(input("Address: "))
        join_date = str(input("Join date: "))
        insert(table_name, (id, f_name, l_name, salary, address, join_date))
    elif user_ans == "a":
        id = int(input("Enter the patient ID: "))
        amend(table_name, id)
    elif user_ans == "d":
        id = int(input("Enter the patient ID: "))
        delete(table_name, id)
    elif user_ans == "q":
        break

"""
# Commit table
conn.commit()

# Close database connection
conn.close()



