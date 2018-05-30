#Guess The Number
import random
import simplegui
import math
secret_number = 0
count = 1
def new_game():
    print "new game starts"
    global secret_number
    secret_number = random.randrange(0,100)
    global count
    count = 0
n = 0

def range100():
    global secret_number
    secret_number = random.randrange(0,100)
    a = math.log(100)
    b = math.log(2)
    c = a/b
    global n
    n = math.ceil(c)
    print "Maximum choices available = \t",n
    new_game()
    
def range1000():
    global secret_number
    secret_number = random.randrange(0,1000)
    a = math.log(1000)
    b = math.log(2)
    c = a/b
    global n
    n = math.ceil(c)
    print "Maximum choices available = \t",n
    new_game()
    
def input_guess(guess):
    global count
    global n
    print "count is " , count
    global secret_number
    guess = float(guess)
    print "guess was",guess
    
    if (count < n):
        count = count + 1
        if secret_number > guess:
            print "higher"
        elif secret_number < guess:
            print "lower"
        elif secret_number == guess:
            print "that's it. played well!"
            new_game()
        print ("number of chances left", (n-count))
    else:
        print "chances over, you lose"
        new_game()
    
        
    

frame = simplegui.create_frame("Guess The Number",300,300)

frame.add_button("Range from [0,100)",range100,200)
frame.add_button("Range from [0,1000)",range1000,200)
frame.add_input("Enter guess",input_guess,100)
frame.start()
new_game()