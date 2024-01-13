cardNumber = input("Enter Credit Card Number :-\n")

hiddenNumber=""

for i in range(0,len(cardNumber)) :
    if(i<len(cardNumber)-4) :
        hiddenNumber+="X"
    else :
        hiddenNumber+=cardNumber[i]

print("Hidden Credit Card Number is :-",hiddenNumber)