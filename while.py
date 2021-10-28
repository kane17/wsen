# coding=utf-8
# n = input("You're in the Lost Forest. Go left or right?")
# while n == "right":
#     n = input("You're in the Lost Forest. Go left or right? ")
# print("You got out of the Lost Forest!")


# i = 1
# while i < 10:
#     print(i)
#     i=i+1

# j = 1
# while j < 10:
#     print(j)
#     j = j+1
#     if j > 5:
#         break


# for i in range(6):
#     print(i)
# print("Fertig")
#     print(x)
# routine = ['Arbeiten', 'Erschöpft sein', 'Ins Bett gehen', 'Erholen']
# for y in routine:
#     print(y)

# while True:
#     try:
#         i = int(input("please enter an integer"))
#         break
#     except:
#         print("no valid integer")
# print("good job, congrets")

A = {2,3,4}
# # print(len(A))
# # print({1,2} == {2,1})
B = {3, 4, 6, 8}
#
AxB = set(())
for a in A:
    for b in B:
        AxB.add((a,b))

print(len(A))
print(len(B))
print(len(AxB))

for i in AxB:
    print(i)

