a = 25
print("dec", a)
print("dual", bin(a))
print("oktal", oct(a))
print("hexadez", hex(a))
import math

x = 12 / 7
print(x)

print(math.factorial(4))

"""t1 = "part 1"
t2 = "part 2"
t = t1 + ", "+ t2
t3 = "-oooo-"
t4= "****"
tl = t4 + t3 *3 + t4
print(t)
print(tl)"""

test = "Da ist ein Beispiel"
such = "ei"
anz = test.count(such)
erstPos = test.find(such)
nextPos = test.find(such, erstPos + 1)
endPos = test.rfind(such)
test = test.replace("ist", "war")

if test.startswith("Da"):
    print("ja")
else:
    print("nein")
# Zerlegung
teile = test.partition("ei")
for i in range(len(teile)):
    print(teile[i])


result = True
for x in range(11):
    for y in range(11):
        result = result and not (x in Black and y in Orange and (x,y) in T)
print(result)