import eel


"""
@eel.expose
def create_combo(combo_name):
    menu[combo_name] = {}
    update_men()"""

# initalise the folder with web code
eel.init('./web')
# start the web page with index.html at 635px x 800px
eel.start('index.html', block=False) 

# keep the program running until force quitted or UI is closed
while True:
    eel.sleep(0.05)