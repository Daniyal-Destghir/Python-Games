import time
import random

#Intro
print("Find Jack 2")
Q1 =input("What is your name: ")
time.sleep(1)
print(Q1 + " and Jack decided to go somewhere else.")
time.sleep(1)
print("But, you stumbled upon a place that is not yet discovered by mankind.")
time.sleep(1)
print("Here we go...")
time.sleep(2)
print("Help: In the options 1= to the first choice and 2= the second choice")
time.sleep(1)
Q2 =input("Where should be go? in to a pit of tigers or in to a put of wood pecker: ")

#Question 2
if Q2 == "2":
    print("You died cause the wood pecker thought you were a tree...")
    time.sleep(2)

if Q2 == "1":
    print("You survived...")
    time.sleep(1)
    print("Somehow...")
    time.sleep(2)
    #Question 3

    Q3 =input("Now, this is very simple, should you eat a berry or should you eat fungus: ")
    time.sleep(1)
    if Q3 == "2":
        print("Dead")
        time.sleep(2)
    if Q3 == "1":
        print("You survived.. YAYYYYYYYYYYYYY")
        time.sleep(2)
        print("Now the final question...")
        time.sleep(1)
        #Question 4

        Q4 = input("What is 1+1? is it 11 or is it 2? : ")

        if Q4 == "2":
            print("YAYYYYYYYYYYYYYYYY")
            time.sleep(1)
            print("You survived!!!")
            time.sleep(1)
            print("Give this man a degree")
            time.sleep(2)
        
        if Q4 == "1":
            print("...")
            time.sleep(2)
            print("ARE YOU STUPID???????")
            time.sleep(2)