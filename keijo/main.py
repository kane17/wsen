# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

U = {0,1,2,3,4,5,6,7,8,9,10}
X = set({})
for x in U:
    if x>2 and x<6:
        X.add(x)
print(X)


Y = set({})
for y in U:
    if y % 2 == 0:
        Y.add(y)
print(Y)

print("Vereinigung / Union")
print(X.union(Y))


print("Schnittmenge / INtersection")
print(X.intersection(Y))

print("Differenz")
print(X.difference(Y))