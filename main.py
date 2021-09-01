import eel
import errorchecking as ec 
import database_control as dbc


@eel.expose
def film(pk):
    returned, flag, reason = ec.film(pk)
    eel.load_page(returned, flag, reason)

@eel.expose 
def save(pk,name,yor,rating,runtime,genre):
    pk = int(pk)
    saved = [{'name':"MOVIE_NAME", 'value': name}, {'name':"YEAR_OF_RELEASE", 'value': yor}, {'name':"RATING", 'value': rating}, {'name':"RUNTIME", 'value': runtime}, {'name':"GENRE", 'value': genre}]
    for i in saved:
        returned, flag, reason  = ec.amend(pk, i["name"], i["value"])
        if(not flag):
            break

    eel.response(flag, reason)

@eel.expose
def search(query):
    results = dbc.search(query)
    eel.update_films(results)

@eel.expose
def delete_movie(pk):
    pk = int(pk)
    returned, flag, reason = ec.delete(pk)
    eel.response(flag, reason)

@eel.expose
def update_db():
    eel.update_films(dbc.whole_db())

@eel.expose
def next_pk():
    eel.next_pk(len(dbc.whole_db()) + 1)

@eel.expose
def add_film(pk,name,yor,rating,runtime,genre):
    name = str(name)
    rating = str(rating)
    genre = str(genre)

    returned, flag, reason = ec.insert(pk,name,yor,rating,runtime,genre)

    eel.response(flag, reason)


# initalise the folder with web code
eel.init('./web')
# start the web page with index.html at 635px x 800px
eel.start('index.html', block=False, size=(1435,800)) 

# keep the program running until force quitted or UI is closed
while True:
    eel.sleep(0.05)