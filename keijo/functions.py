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

def max_of_two(x, y):
    highestOfTwo = 0
    if x > y:
        highestOfTwo = x
    else:
        highestOfTwo = y
    return highestOfTwo

def max_of_three(x, y, z):
    highestOfThemAll = max_of_two(x, max_of_two(y, z))
    # maxOfFirstAndSecond = max_of_two(x, y)
    # maxOfSecondAndThird = max_of_two(y, z)
    # maxOfFirstAndThird = max_of_two(x, y)
    # if maxOfFirstAndSecond > maxOfSecondAndThird:
    #     highestOfThemAll = maxOfFirstAndSecond
    # else:
    #     highestOfThemAll = maxOfSecondAndThird
    #
    # if maxOfSecondAndThird > highestOfThemAll:
    #     highestOfThemAll = maxOfSecondAndThird
    print("Die höchste Zahl ist: " + str(highestOfThemAll))

max_of_three(4999999, 876656543323, 300700)


def f(x):
    y = x**0.5
    return y

print(f(-3))

def g(x):
    y = 4*x+3
    return y

print(g(3))