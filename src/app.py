import json
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
    phoneNumber = input("Introducir numero de telefono: \n")

    cliente = { 
        "name" : name,
        "phoneNumber" : phoneNumber
    }

    queue.enqueue(cliente)

def dequeue():
    name_to_delete = queue.get_queue()[0]["name"]
    print(f"Hola, vas a borrar a {name_to_delete}")

    queue.get_queue().pop(0)
    print("borraste")


        
        #   def serialize(self): return { 
        #   "id": self.id, 
        #   "user_list_id": self.user_list_id, 
        #   "label": self.label, "done": self.done, 
        #   "result": self.result if self.result is not None else "" }      

def save():
    pass

def load():
    pass 
        
    
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
        print("cliente agregado")
    elif option == 2:
        dequeue()
    elif option == 3:
        print_queue()
    elif option == 6:
        print("Bye bye!")
        stop = True
    else:
        print("Not implemented yet or invalid option "+str(option))
