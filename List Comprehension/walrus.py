# 0 to 9 added in list
list = [i for i in range(10)]
print("List value :-",list)

mean = sum(list)/len(list)

# walrus operator :-  ' := '
lesser_value = [val for val in list if (temp := val-mean)<0]

print("Lesser value :-",lesser_value)