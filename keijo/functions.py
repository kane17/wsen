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

print(bin(5 | 6))

R = {(1, 4),(1, 3),(1, 2),(3, 6),(3, 5),(6, 7),(5, 7),(1, 6),(4, 7),(1, 5),(1, 7)}
result2 = True
for x in {1,2,3,4,5,6,7}:
    if x in {1,4}:
        result1 = False
        for y in {2,7}:
            result1 = result1 or (( x , y ) in R )
    result2 = result2 and result1
print ( result2)


sum = 0
for i in range(1, 11):
    print(i)
    sum += i*i
    print()
print(sum)

salary = 8000

def printSalary():
    salary = 12000
    print("salary: ", salary)

printSalary()

def drucke_zk_liste():
    userInputs = []
    userEnteredStop = False
    print(not userEnteredStop)

drucke_zk_liste()

def SumFunk(num):
    sum = 0
    for i in range(10):
        print(i)

SumFunk(100)

x = 15

def print_f():
    x = 27
    print(x)

print_f()
print(x)