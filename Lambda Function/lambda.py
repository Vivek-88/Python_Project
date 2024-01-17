# Lambda function can have any number of arguments but it is restricted to a single expression. The single expression is evaluated and returned.

# Lambda function can be used wherever the function object is required.

# Normal function for addition 
def sum(x,y,z) :
    return (x+y+z)


# Using Lambda Function
add = lambda x,y:x+y

print(sum(2,3,5))

print(add(2,3))

# Comparison Using lambda

min = lambda x,y:x if x<y else y

print(min(10,3))

print(min(2,5))