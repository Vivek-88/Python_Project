a = input("Enter a list of number and string with space seperated :-\n").split(" ")

list = []

for b in a :
    if(b.isnumeric()) :
        list.append(b)

print("After removing string list will be :-",list)