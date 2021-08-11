""" Testing script for modules

Step 1: Generate invalid and valid input values for all data inputs

Primary Keys, movie name, year of release, rating, runtime, genre

primary_keys = {
   1:{"valid":True, "value":1}
}
"""

import random, string
import database_control as dbc

data_inputs = {
    "primary_key":{
        "type":"int",
        "valid":[],
        "invalid":[]
    },
    "movie_name":{
        "type":"str",
        "valid":[],
        "invalid":[]
    },
    "year_of_release":{
        "type":"int",
        "valid":[],
        "invalid":[]
    },
    "rating":{
        "type":"str",
        "valid":[],
        "invalid":[]
    },
    "runtime":{
        "type":"int",
        "valid":[],
        "invalid":[]
    },
    "genre":{
        "type":"str",
        "valid":[],
        "invalid":[]
    }
}

def generate_valid(type, max_length=50, max_value=10000, min_value=0):
    if(type == "str"):
        text = ''.join(random.choices(string.ascii_letters, k=max_length))
        return text
    if(type == "int"):
        n = random.randint(min_value,max_value)
        return n

def generate_invalid(type, max_length=50, max_value=10000, min_value=0):
    if(type == "str"):
        flt = random.uniform(min_value, max_value)
        n = random.randint(min_value,max_value)
        emp = ""
        chosen = random.randint(0,2)
        if(chosen == 0):
            return flt 
        elif(chosen == 1):
            return n 
        else:
            return emp
    if(type == "int"):
        negative = random.randint(-max_value,min_value)
        flt = random.uniform(min_value, max_value)
        emp = ""
        text = ''.join(random.choices(string.ascii_letters, k=max_length))
        chosen = random.randint(0,3)
        if(chosen == 0):
            return negative 
        elif(chosen == 1):
            return flt 
        elif(chosen == 2):
            return emp
        else:
            return text

def generate_values():
    # Generate valid & invalids
    for input, values in data_inputs.items():
        if(values["type"] == "int"):
            # Valid inputs
            for i in range(0, 30):
                t = generate_valid("int")
                values["valid"].append(t)
            # Invalid inputs
            for i in range(0, 30):
                t = generate_invalid("int")
                values["invalid"].append(t)
        else:
            # String
            # Valid inputs
            for i in range(0, 30):
                t = generate_valid("str")
                values["valid"].append(t)
            # Invalid inputs
            for i in range(0, 30):
                t = generate_invalid("str")
                values["invalid"].append(t)

def database_control_test():
    # Check entire database
    try:

        returned = dbc.whole_db()

        # If returned is empty
        if returned == "":
            return(False, "Empty database")
        elif type(returned) != type({}):
            return(False, "Database not returned as dictionary, returned in "+str(type(returned)))
        
        # Check single film'

        preselected = returned[0]
        returned = dbc.film(1) # Request first film
        # Compare the returned film, and the preselected film
        if returned == "":
            return(False, "Empty film returned")
        elif type(returned) != type({}):
            return(False, "Film returned not in dictionary format, returned in "+str(type(returned)))
        elif preselected != returned:
            return(False, "Film returned not the same as the requested film")
    except:
        return(False, "Database control module error")

    return(True, "Passed all tests")

while True:
    ans = input("Test which module: database control (d), error checking (e) or both (b)")

    # Test database_control module
    if(ans == 'd'):
        flag, reason = database_control_test()
        print(reason)
    
