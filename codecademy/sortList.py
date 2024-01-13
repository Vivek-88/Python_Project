list = input("Enter space seperated list of numbers :- \n").split(" ")

for i in range(0,len(list)) :
    list[i]=int(list[i])

sortType = input("Enter 'asc' to sort in ascending order, 'desc' to sort in descending order or 'none' for remains same :-\n")

if(sortType=="asc") :
    list.sort()
elif(sortType=="desc") :
    list.sort(reverse=True)

print(list)