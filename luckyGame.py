import random as rnd

name = input("Enter Your Name : ")
print("Welcome",name,"in Lucky Game")
# print("Rule of Game :- \n 1. You are given maximum of 5 chance.\n 2. In ever step, you need to enter a number and you get ")

while(input("Enter 1 to play again or any key to exit : ")=="1") :
    luckyNumber = rnd.randrange(5)

    isWinner=False
    for i in range(0,5) :
        val = int(input("Enter a number to guess Lucky Number : "))
        if(val<luckyNumber) :
            print("Entered number is smaller then Lucky number.")
        elif(val==luckyNumber) :
            isWinner=True
            break
        else :
            print("Entered number is greater then Lucky number.")


    if(isWinner) :
        print("Congrat !!",name,"You win the game")
    else :
        print("Sorry !!",name,"You loss the game,Try again")

print("Thanks for Playing !! Game is over")