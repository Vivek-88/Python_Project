#mutable

a = {3,5,23,5,5,3,2,5,6,8,9,6,6,7}

print(a)

a.add(999)

print(a)
print(len(a))

print(a.pop())

b = {939,746,3,7,9,3,5}

print(a.union(b))

print(a.intersection(b))