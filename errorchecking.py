import database_control as dbc


# Return select film
def film(pk):
    returned = dbc.film(pk)
    # If the film returned is a dict
    if(type(returned) == type({})):
        # Success
        return(returned, True, None)
    else:
        # Failure
        return(None, False, "Film does not exist...")

# Function to check value against defined parameters
def check_value(name, value):

    # Primary key
    if(name == "pk"):
        pk = value
        try:
            pk = int(pk)
        except:
            return(False, "Primary key is not an integer")
        # Check if primary key is integer
        if(type(pk) != type(0)):
            return(False, "Primary key is not an integer")
        # Check if primary key is positive
        if(pk < 0):
            return(False, "Primary key is not above 0")
        # Check if primary key already exists
        returned, flag, message = film(pk)
        if(flag == True):
            return(False, "Primary key already exists")

        # Success
        return(True, None)
    
    # Film name
    if(name == "name"):
        name = value 
        # Check if film name is a string
        if(type(name) != type("str")):
            return(False, "Film name is not of type string")
        # Check that the film name is not just whitespace/empty
        if(not name or name.isspace()):
            return(False, "Film name is either empty or is just whitespace")

        # Success
        return(True, None)

    # Year of release
    if(name == "yor"):
        yor = value  
        try:
            yor = int(yor)
        except:
            return(False, "Year of release is not an integer")
        # Check if year of release is integer
        if(type(yor) != type(1)):
            return(False, "Year of release is not of type integer")
        # Check if year of release is positive
        elif(yor < 0):
            return(False, "Year of release cannot be less then 0")

        # Success
        return(True, None)

    # Rating 
    if(name == "rating"):
        rating = value  
        # Check if rating is string
        if(type(rating) != type("string")):
            return(False, "Rating is not of type string")
        # Check that the rating is not just whitespace/empty
        if(not rating or rating.isspace()):
            return(False, "Rating is either empty or is just whitespace")

        # Success
        return(True, None)

    # Runtime
    if(name == "runtime"):
        runtime = value  
        try:
            runtime = int(runtime)
        except:
            return(False, "Runtime is not a positive integer")
        # Check if runtime is an integer
        if(type(runtime) != type(1)):
            return(False, "Runtime is not of type integer")
        # Check if runtime is positive
        if(runtime < 0):
            return(False, "Runtime is negative integer")

        # Success
        return(True, None)

    # Genre
    if(name == "genre"):
        genre = value 
        # Check if genre is a string
        if(type(genre) != type("string")):
            return(False, "Genre is not of type string")
        # Check that the genre is not just whitespace/empty
        if(not genre or genre.isspace()):
            return(False, "Genre is either empty or is just whitespace")
        # Success
        return(True, None)
                
        
# Insert film into database 
def insert(pk, name, yor, rating, runtime, genre):
    for i in range(0, 6):        
        if(i == 0):
            flag, reason = check_value("pk", pk)
        elif(i == 1):
            flag, reason = check_value("name", name)
        elif(i == 2):
            flag, reason = check_value("yor", yor)
        elif(i == 3):
            flag, reason = check_value("rating", rating)
        elif(i == 4):
            flag, reason = check_value("runtime", runtime)
        elif(i == 5):
            flag, reason = check_value("genre", genre)

        # Failure
        if(not flag):
            return(None, False, "Insert film falure, reason: "+reason)

    pk = int(pk)
    yor = int(yor)
    runtime = int(runtime)
    dbc.insert((pk, name, yor, rating, runtime, genre))

    # Success
    return(None, True, None)
    
# Amend film into database
def amend(primary_key, field, value):
    # Check if primary key is valid
    if(type(primary_key) != type(0)):
        return(None, False, "Primary key is not an integer")

    # Check if primary key exists
    returned, flag, message = film(primary_key)
    if(flag == False):
        return(None, False, "Amend failure as selected film does not exist")

    if(field == "PRIMARY_KEY"):
        flag, reason = check_value("pk", value)
        if(not flag):
            return(None, False, "Amend failure, reason: "+reason)
        dbc.amend(primary_key, field, value)
    elif(field == "MOVIE_NAME"):
        flag, reason = check_value("name", value)
        if(not flag):
            return(None, False, "Amend failure, reason: "+reason)
        dbc.amend(primary_key, field, value)
    elif(field == "YEAR_OF_RELEASE"):
        flag, reason = check_value("yor", value)
        if(not flag):
            return(None, False, "Amend failure, reason: "+reason)
        dbc.amend(primary_key, field, value)
    elif(field == "RATING"):
        flag, reason = check_value("rating", value)
        if(not flag):
            return(None, False, "Amend failure, reason: "+reason)
        dbc.amend(primary_key, field, value)
    elif(field == "RUNTIME"):
        flag, reason = check_value("runtime", value)
        if(not flag):
            return(None, False, "Amend failure, reason: "+reason)
        dbc.amend(primary_key, field, value)
    elif(field == "GENRE"):
        flag, reason = check_value("genre", value)
        if(not flag):
            return(None, False, "Amend failure, reason: "+reason)
        dbc.amend(primary_key, field, value)
    else:
         return(None, False, "Field does not exist")

    # Success
    return(None, True, None)
    
        
# Delete film from database
def delete(pk):
    # Check if primary key exists
    returned, flag, message = film(pk)
    if(flag == False):
        return(None, False, "Delete failure as selected film does not exist")
    else:
        dbc.delete(pk)

    # Success
    return(None, True, None)
