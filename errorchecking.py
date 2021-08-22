import database_control as dbc


# Return select film
def film(pk):
    returned = dbc.film(pk)
    # If the film returned is a tuple
    if(type(returned) == type(())):
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
        # Check if primary key is integer
        if(type(pk) != type(0)):
            return(False, "Primary key is not an integer")
        # Check if primary key already exists
        returned, flag, message = film(pk)
        if(flag == False):
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
        if(not name or not name.isspace()):
            return(False, "Film name is either empty or is just whitespace")

        # Success
        return(True, None)

    # Year of release
    if(name == "yor"):
        yor = value  
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
        if(not rating or not rating.isspace()):
            return(False, "Rating is either empty or is just whitespace")

        # Success
        return(True, None)

    # Runtime
    if(name == "runtime"):
        runtime = value  
        # Check if runtime is an integer
        if(type(runtime) != type(1)):
            return(False, "Runtime is not of type integer")
        # Check if runtime is positive
        if(runtime < 0):
            return(False, "Runtime is negative integer")

        # Success
        return(True, None)

    # Genre
    if(name == "Genre"):
        genre = value 
        # Check if genre is a string
        if(type(genre) != type("string")):
            return(False, "Genre is not of type string")
        # Check that the genre is not just whitespace/empty
        if(not genre or not genre.isspace()):
            return(False, "Genre is either empty or is just whitespace")

        # Success
        return(True, None)
                
        
        


def insert(pk, name, yor, rating, runtime, genre):
    # Insert film into database 
    if(check_value("pk", pk) and check_value("name", name) and check_value("yor", yor) and check_value("rating", rating) and check_value("runtime", runtime) and check_value("genre", genre)):
        print("sucess")


def amend():
    # Amend film into database
    pass

def delete(pk):
    # Delete film from database
    pass
