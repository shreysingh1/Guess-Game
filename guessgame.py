import random
rannum=random.randrange(1,100)
guess=int(input("enter your guess between 1 and 100:"))
c=0
while(guess!=rannum):
        if guess < rannum:
            print("you need to guess higher number")
            guess=int(input("enter your guess between 1 and 100:"))
        elif guess > rannum:
            print("you need to guess lower number!")
            guess=int(input("enter your guess between 1 and 100:"))
        else:
            print("you guessed the correct number")
            break
        c=c+1
print("you took " + str(c) + " step to guess")
