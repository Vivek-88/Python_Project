s = "Ram is a god"

# writting to a file

# 1st way
# with open("test.txt","w") as f:
#     f.write(s)

# # 2nd way
# fp = open("test.txt","w")
# fp.write(s)
# fp.close()

# appending to a file

with open("test.txt","a") as f:
    f.write(s)

# Reading a file

with open("test.txt","r") as f:
    s1 = f.read()
    print(s1)