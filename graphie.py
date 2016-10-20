import time

string = input("Character to use?")
counter = 1
limit = int (input ("How many times to repeat?" ))

while True:  
    
    # going to the right
    while (counter < limit):
        print (string * counter)
        counter = counter + 1
        time.sleep(.01)
        
    # and back to the left  
    while (counter > 0):
        counter = counter - 1
        print (string * counter)
        time.sleep(.05)
