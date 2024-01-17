# Task :- Genrate a new file with 10 line written "Vivek" and in next 10 line "Kumar" is written



text_to_write = ""
for i in range(10) :
    text_to_write+="vivek\n"

for i in range(10) :
    text_to_write+="kumar\n"


with open("text.txt",'a') as f:
    print(text_to_write)
    f.write(text_to_write)








# s = "Ram is a god"

# # writting to a file

# # 1st way
# # with open("test.txt","w") as f:
# #     f.write(s)

# # # 2nd way
# # fp = open("test.txt","w")
# # fp.write(s)
# # fp.close()

# # appending to a file

# with open("test.txt","a") as f:
#     f.write(s)

# # Reading a file

# with open("test.txt","r") as f:
#     s1 = f.read()
#     print(s1)



# Note :- 'a' ka use tbb kre, jbb file mai kuch likhna ho, or 'w' means file mai sirf joo likhege ohi rhega, history clean kr deta hai


