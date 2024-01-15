a = int(input("Enter an Integer :-\n"))
type = input("Enter operator :-\n")
b = int(input("Enter an Integer :-\n"))

ans=0
if(type=='+') :
    ans = a+b
elif(type=='-') :
    ans=a-b
elif(type=='*') :
    ans=a*b
elif(type=='/') :
    ans=a/b

print(a,type,b,"is",ans)