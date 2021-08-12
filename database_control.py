import sqlite3

# Connect to database
conn = sqlite3.connect("film_database.db")
cursor = conn.cursor()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Return the whole database
def whole_db():
    global cursor
    cursor.row_factory = dict_factory
    db = {}
    i = 0
    for row in cursor.execute('SELECT * FROM FILMS'):
        db[i] = row
        i = i + 1

    return(db)

# Return specific film
def film(primary_key):
    global cursor
    selected_film = cursor.execute("SELECT * FROM FILMS WHERE PRIMARY_KEY="+str(primary_key))
    for row in selected_film:
        selected_film = row
    return(selected_film)

# Parse table a tuple of values (primary key, name, year of release, rating, runtime, genre)
def insert(values):
    global cursor, conn
    values = tuple(values)
    cursor.execute("INSERT INTO FILMS VALUES (?,?,?,?,?,?)", values)
    conn.commit()

# Amend film using primary key, field to amend and fields new value
def amend(primary_key, field, value):
    global cursor, conn
    selected_film = cursor.execute("SELECT * FROM FILMS WHERE PRIMARY_KEY="+str(primary_key))  
    if(type(value) == type(1)):
        cursor.execute("UPDATE FILMS SET " + field + "=" + str(value) + " WHERE PRIMARY_KEY = " + str(primary_key))
    else:
        cursor.execute("UPDATE FILMS SET " + field + "='" + value + "' WHERE PRIMARY_KEY = " + str(primary_key))
    conn.commit()

# Delete film using primary key
def delete(primary_key):
    global cursor, conn
    cursor.execute("DELETE FROM FILMS WHERE PRIMARY_KEY = " + str(primary_key))
    conn.commit()

# Create table (only used once)
def create_table():
    conn.execute('''CREATE TABLE FILMS
    (PRIMARY_KEY INTEGER,
    MOVIE_NAME TEXT,
    YEAR_OF_RELEASE INTEGER,
    RATING TEXT,
    RUNTIME INTEGER,
    GENRE TEXT);''')

#create_table()

# Commit table
#conn.commit()

# Close database connection
#conn.close()

#insert((1,'Ghostbusters',2016,'PG',116,'Comedy'))

