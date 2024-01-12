#mutable

l1 = [3,4,7,33,662,2,"vivek",73,6.7,4,8]

print(type(l1))
print(l1)
l1.remove(4)
print(l1)

l2 = [6,3,9,7,5]
print(l2)
l2.sort()
print(l2)
l2.append(5)
print(l2)
l2.pop()
print(l2)

l2.extend(l1)
print(l2)
print(l1)
