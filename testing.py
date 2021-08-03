""" Testing script for modules

Step 1: Generate invalid and valid input values for all data inputs

Primary Keys, movie name, year of release, rating, runtime, genre

primary_keys = {
   1:{"valid":True, "value":1}
}
"""

import random, string

data_inputs = {
    "primary_key":{
        "valid":[],
        "invalid":[]
    },
    "movie_name":{
        "valid":[],
        "invalid":[]
    },
    "year_of_release":{
        "valid":[],
        "invalid":[]
    },
    "rating":{
        "valid":[],
        "invalid":[]
    },
    "runtime":{
        "valid":[],
        "invalid":[]
    },
    "genre":{
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


print(generate_invalid("int"))

# Generate valid & invalids
for input, values in data_inputs.items():
    if(input == "primary_key"):
        # Valid inputs
        for i in range(0, 30):
            pass



    
