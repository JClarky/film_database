import database_control as dbc

def film(pk):
    # Return film
    returned = dbc.film(pk)
    if(type(returned) == type(())):
        # Success
        return(returned, True, None)
    else:
        # Failure
        return(returned, False, "Film does not exist...")

def insert():
    # Insert film into database
    pass

def amend():
    # Amend film into database
    pass

def delete(pk):
    # Delete film from database
    pass
