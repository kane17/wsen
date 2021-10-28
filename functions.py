def greet(name):
    """This function greets to the person passed in as a parameter"""
    print("Hello, " + name + ". Good morning!")


greet("Staehli")
print(greet.__doc__)

def evenOdd ( x ):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

evenOdd(3)