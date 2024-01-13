def isEqual(s) :
    x=0
    o=0
    for i in range(0,len(s)) :
        if(s[i]=='X') :
            x+=1
        elif(s[i]=='O') :
            o+=1
    
    return x==o


s = input("Enter a String :-\n")


print("String",s,"is",isEqual(s))

