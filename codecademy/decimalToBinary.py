decimalNumber = int(input("Enter a decimal number :-\n"))

binaryNumber = ""

temp=decimalNumber
while(temp>0) :
    if(temp%2==1) :
        binaryNumber+="1"
    else :
        binaryNumber+="0"
    temp//=2


binaryNumber=binaryNumber[::-1]
print("Binary Number of",decimalNumber,"is :-",binaryNumber)