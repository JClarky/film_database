""" Testing script for modules

Step 1: Generate invalid and valid input values for all data inputs

Primary Keys, movie name, year of release, rating, runtime, genre

primary_keys = {
   1:{"valid":True, "value":1}
}
"""

import random, string
import database_control as dbc
import errorchecking as ec

last_added_pk = None

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
        return str(text)
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
    global last_added_pk
    # Check entire database

    returned = dbc.whole_db()
    # If returned is empty
    if returned == "":
        return(False, "Empty database")
    elif type(returned) != type({}):
        return(False, "Database not returned as dictionary, returned in "+str(type(returned)))
    
    # Check single film'

    preselected = returned[0]
    returned = dbc.film(preselected["PRIMARY_KEY"]) # Request first film
    # Compare the returned film, and the preselected film
    if returned == "":
        return(False, "Empty film returned")
    elif type(returned) != type({}):
        return(False, "Film returned not in dictionary format, returned in "+str(type(returned))+" returned: "+str(returned))
    elif preselected != returned:
        return(False, str("Film returned not the same as the requested film preselected: "+str(preselected)+" returned: "+str(returned)))

    # Add movie
    idx = random.randint(0,29)
    pk = len(dbc.whole_db())+1
    last_added_pk = pk
    name = data_inputs["primary_key"]["valid"][idx]
    yor = data_inputs["year_of_release"]["valid"][idx]
    rating = data_inputs["rating"]["valid"][idx]
    runtime = data_inputs["runtime"]["valid"][idx]
    genre = data_inputs["genre"]["valid"][idx]
    inserted_dict = {'PRIMARY_KEY': pk, 'MOVIE_NAME': str(name), 'YEAR_OF_RELEASE': yor, 'RATING': rating, 'RUNTIME': runtime, 'GENRE': genre}

    dbc.insert((pk,  name, yor, rating, runtime, genre))
    inserted = dbc.film(pk)
    if inserted == "":
        return(False, "Empty inserted film returned")
    elif str(inserted) != str(inserted_dict):
        return(False, "Film returned not matching inserted film")

    # Amend movie
    # Ensure the new value is actually different then the last value
    double_up = True
    while double_up:
        idx = random.randint(0,29)
        name = data_inputs["primary_key"]["valid"][idx]
        yor = data_inputs["year_of_release"]["valid"][idx]
        rating = data_inputs["rating"]["valid"][idx]
        runtime = data_inputs["runtime"]["valid"][idx]
        genre = data_inputs["genre"]["valid"][idx]
        new_random = [{'name':"PRIMARY_KEY", 'value': pk}, {'name':"MOVIE_NAME", 'value': str(name)}, {'name':"YEAR_OF_RELEASE", 'value': yor}, {'name':"RATING", 'value': rating}, {'name':"RUNTIME", 'value': runtime}, {'name':"GENRE", 'value': genre}]
        
        selected_to_change = random.randint(1,5)
        if inserted_dict[new_random[selected_to_change]["name"]] != new_random[selected_to_change]["value"]:
            break


    dbc.amend(pk,new_random[selected_to_change]["name"],new_random[selected_to_change]["value"])
    amended = dbc.film(pk)
    if amended == "":
        return(False, "Empty amended film returned")
    elif amended == inserted:
        return(False, "Film returned not matching amended film, amended="+str(new_random)+" returned= "+str(amended))

    # Delete movie
    dbc.delete(pk)
    if(type(dbc.film(pk)) == type({})):
        return(False, "Film has not been succesfully deleted")

    return(True, "Passed all tests")

def error_checking_test():
    global last_added_pk
    whole_db = dbc.whole_db()
    
    # Check entire module on valid values first
    # Then, if passed, select data entry to be invalid (cycle through)
    # Test Entire module 30 times
    
    #
    # VALID DATA CHECK
    #

    # Repeat 30 times
    for i in range(0,30):
        # Check single film
        preselected = whole_db[random.randint(0,len(whole_db))]
        returned = ec.film(preselected["PRIMARY_KEY"])[0] # Request first film
        # Compare the returned film, and the preselected film
        if returned == "":
            return(False, "Empty film returned")
        elif type(returned) != type({}):
            return(False, "Film returned not in dictionary format, returned in "+str(type(returned))+" returned: "+str(returned))
        elif preselected != returned:
            return(False, str("Film returned not the same as the requested film preselected: "+str(preselected)+" returned: "+str(returned)))

        # Add movie
        idx = random.randint(0,29)
        pk = len(dbc.whole_db())+1
        last_added_pk = pk
        name = data_inputs["movie_name"]["valid"][idx]
        yor = data_inputs["year_of_release"]["valid"][idx]
        rating = data_inputs["rating"]["valid"][idx]
        runtime = data_inputs["runtime"]["valid"][idx]
        genre = data_inputs["genre"]["valid"][idx]
        inserted_dict = {'PRIMARY_KEY': pk, 'MOVIE_NAME': str(name), 'YEAR_OF_RELEASE': yor, 'RATING': rating, 'RUNTIME': runtime, 'GENRE': genre}

        returned, flag, reason = ec.insert(pk, name, yor, rating, runtime, genre)

        if(not flag):
            return(False, "Insert failure, reason: "+reason)
        inserted = ec.film(pk)
        if inserted == "":
            return(False, "Empty inserted film returned")
        elif str(inserted) != str(inserted_dict):
            print(inserted, inserted_dict)
            return(False, "Film returned not matching inserted film")

        # Amend movie
        # Ensure the new value is actually different then the last value
        double_up = True
        while double_up:
            idx = random.randint(0,29)
            name = data_inputs["primary_key"]["valid"][idx]
            yor = data_inputs["year_of_release"]["valid"][idx]
            rating = data_inputs["rating"]["valid"][idx]
            runtime = data_inputs["runtime"]["valid"][idx]
            genre = data_inputs["genre"]["valid"][idx]
            new_random = [{'name':"PRIMARY_KEY", 'value': pk}, {'name':"MOVIE_NAME", 'value': str(name)}, {'name':"YEAR_OF_RELEASE", 'value': yor}, {'name':"RATING", 'value': rating}, {'name':"RUNTIME", 'value': runtime}, {'name':"GENRE", 'value': genre}]
            
            selected_to_change = random.randint(1,5)
            if inserted_dict[new_random[selected_to_change]["name"]] != new_random[selected_to_change]["value"]:
                break


        ec.amend(pk, new_random[selected_to_change]["name"], new_random[selected_to_change]["value"])
        amended = ec.film(pk)
        if amended == "":
            return(False, "Empty amended film returned")
        elif amended == inserted:
            return(False, "Film returned not matching amended film, amended="+str(new_random)+" returned= "+str(amended))

        # Delete movie
        ec.delete(pk)
        if(type(ec.film(pk)) == type({})):
            return(False, "Film has not been succesfully deleted")

    #
    # INVALID DATA CHECK
    #
    
    # Cycle through all data inputs
    for key, value in data_inputs.items():
        # Test 30 times
        for i in range(0,30):
            created_values = {'primary_key': data_inputs["primary_key"]["valid"][random.randint(0,29)], 
                            'movie_name': data_inputs["movie_name"]["valid"][random.randint(0,29)], 
                            'year_of_release': data_inputs["year_of_release"]["valid"][random.randint(0,29)], 
                            'rating': data_inputs["rating"]["valid"][random.randint(0,29)], 
                            'runtime': data_inputs["runtime"]["valid"][random.randint(0,29)], 
                            'genre': data_inputs["genre"]["valid"][random.randint(0,29)]}

            created_values[key] = data_inputs[key]["invalid"][random.randint(0,29)]
            
            # Check single film
            if(key == "pk"):
                returned, flag, reason = ec.film(created_values["primary_key"])
                if(flag):
                    return(False, "Film has been returned, but primary_key was invalid")
            
            # Check deleting film
            if(key == "pk"):
                selected_invalid_idx = random.randint(0,29)
                returned, flag, reason = ec.delete(created_values["primary_key"])
                if(flag):
                    return(False, "Film has been deleted, but primary_key was invalid")
            
            # Check add film
            returned, flag, reason = ec.insert(created_values["primary_key"], created_values["movie_name"], created_values["year_of_release"], created_values["rating"], created_values["runtime"], created_values["genre"])
            if(flag):
                return(False, "Inserted film to database with invalid value for "+key+" reason was: "+reason)

            # Check inseting film
            returned, flag, reason = ec.amend(created_values["primary_key"], key.upper(), created_values[key])
            if(flag):
                return(False, "Amended film with invalid value for "+key+" reason was: "+reason)

        
    return(True, "Passed all tests")

while True:
    ans = input("Test which module: database control (d), error checking (e) or both (b)")
    generate_values()

    # Test database_control module
    if(ans == 'd'):
        for g in range(1,101):
            flag, reason = database_control_test()
            print(reason)
            if(flag == False):
                if(last_added_pk):
                    dbc.delete(last_added_pk)
                    last_added_pk = None
                break     
            print(g)
            if(g == 100):
                print("Sucessfully ran 100 times")
    # Error checking module
    elif(ans == "e"):
        flag, reason = error_checking_test()
        if(flag):
            print("Success!!!!")
        else:
            if(last_added_pk):
                dbc.delete(last_added_pk)
                last_added_pk = None  
            print("Failure, reason was: "+reason)
    
