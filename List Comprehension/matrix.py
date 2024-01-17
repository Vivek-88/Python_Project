rows=4
cols=3

for i in range(rows) :
    for j in range(cols) :
        print("(",i,"",j,end=" )")
    print()

# same as above matrix
matrix = [[row*cols + col for col in range(cols)] for row in range(rows)]


print(matrix)