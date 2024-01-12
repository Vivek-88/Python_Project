#mutalbe

dict = {} # empty dict

b = set() # empty set

print(dict,type(dict))

print(b,type(b))

a = {"good":"bad","1":"one","2":"two","Vivek":53,"Vijay":75}

print(a)
print(len(a))

print(a["1"])

print(a["Vijay"])

a["Ram"]=100
print(a["Ram"])

print(a.get("Gita")==None)
# print(a["Gita"]) # it show error

print(a.keys())

for key in a :
    print(key," -> ",a[key])