list = [1,2,3,4,5]

print("Actual List :-",list)

# print using loop

for x in list :
    print(x)

# asign new list using comprehension with multiplying it by 2
new_list = [val*2 for val in list]

print("multiple of 2:-",new_list)

# assign new list with power of 2

new_list1 = [val**2 for val in list]

print("Power :-",new_list1)

# Even number
new_list2 = [val for val in list if val%2==0]

print("Even Number :-",new_list2)

# Odd Number
new_list3 = [val for val in list if val%2==1]

print("Odd Number in list :-",new_list3)