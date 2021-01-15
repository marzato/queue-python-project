import os, json 
from DataStructures import Queue
from sms import send

# there queue has to be declared globally (outside any other function)
# that way all methods have access to it
queue = Queue(mode="FIFO")
   
def print_queue():
    # you must print on the console the entire queue list
    print("Printing the entire list...")
    x = 0
    for i in queue.get_queue():
        name_to_show = queue.get_queue()[x]["name"]
        print(f"({x+1}) {name_to_show}")
        x+=1

def add(): 
    name = input("Introducir nombre del usuario: \n")
    phone_number = input("Introducir numero de telefono: \n")
    cliente = { 
        "name" : name,
        "phone_number" : phone_number
    }
    print(f"\nHola {name}, tienes {queue.enqueue(cliente)} persona/s por delante")

def dequeue():
    name_to_delete = queue.get_queue()[0]["name"]
    print(f"Hola, vas a borrar a {name_to_delete}")
    send("Te vamos a borrar " + name_to_delete.upper(), queue.get_queue()[0]["phone_number"])
    queue.dequeue()


def save():
    def write_json(data, filename='queue.json'): 
        # el archivo existe
        with open(filename,'w') as jsonFile: 
            json.dump(data, jsonFile, indent=4) 
            # el archivo no existe
    with open('queue.json') as json_file: 
        data = json.load(json_file) 
    write_json(queue.get_queue()) 

def load():
    #import json #must be avalaible
    # Opening JSON file 
    f = open('queue.json',) 
    # returns JSON object as a dictionary 
    data = json.load(f)
    queue.get_queue().clear()
    for index in data:
        queue.get_queue().append({"name":index["name"],"phone_number":index["phone_number"]})    
    # Closing file 
    f.close() 
    print("Se cargo el archivo queue.json!")
        
    
print("\nHello, this is the Command Line Interface for a Queue Managment application.")
stop = False
while stop == False:
    
    print('''
What would you like to do (type a number and press Enter)?
- Type 1: For adding someone to the Queue.
- Type 2: For removing someone from the Queue.
- Type 3: For printing the current Queue state.
- Type 4: To export the queue to the queue.json file.
- Type 5: To import the queue from the queue.json file.
- Type 6: To quit
    ''')

    option = int(input("Enter a number:"))
    # add your options here using conditionals (if)
    
    if option == 1:
        add()
    elif option == 2:
        dequeue()
    elif option == 3:
        print_queue()
    elif option == 4:
        save()
    elif option == 5:
        load()
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))
