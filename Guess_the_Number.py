import random

Number=random.randint(1,100)
counter =0
while True:
    counter=counter+1
    try:
        Guess=int(input("Guess a number from 1 to 100 "))
        if Guess > Number:
            print("too high")
        elif Guess < Number:
            print("too low")
        else  :
            print("Congrats your Guess is right")
            print("You Guess the number after",counter,"Trials")
            break
            
    except ValueError :
        print('please enter an intger')
   
  
