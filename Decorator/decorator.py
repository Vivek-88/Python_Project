# provide extra functanality to function

# Python Decorators is a powerful tool to add functionality to functions or 
# classes without modifying their original code. A decorator is essentially 
# a function that takes another function as an input and adds some functionality 
# to it and then returns the original function with the added behavior.

def check(func) :
    def inside(a,b) :
        if b==0 :
            print("Operation can't proceed")
            return
        func(a,b)
    return inside

@check
def div(a,b) :
    return a/b

# without using decorator , we get error

# we can update div by check function
# div = check(div)

# We can either annotate div function with check, called decorator here
print(div(20,0))