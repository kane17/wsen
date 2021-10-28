l = [1,2,3]
print(l)
print(l[1])
print(len(l))
for i in range(len(l)):
    print(l[i])
print(l[1:2])

l =[["Paris","Fr",350000],["Rom","It",420000]]
print(l[0])
print(l[1])
print(l[1][0] , "hat", l[1][2], "Einwohner")
print(l[0][0], "hat", l[0][2], "Einwohner")

fr = ["Paris", "Lyon", "Nizza"]
it = ["Rom", "Mailand"]
print(fr+it*2)
fr[2] = "lens"
print("replace",fr)
fr[2:3] =["Nancy","Metz"]
print(fr)
fr.insert(0,"Nantes")
print("insert",fr)

fr.sort()
print("sort",fr)
fr.reverse()
print("reverse",fr)
fr.remove("Nantes")
print("remove",fr)
fr.append("Montpellier")
print("append",fr)
fr.append("Metz")
print(fr.count("Metz"))

tup = (1,2,3,4)
print(tup)
tup = 1,2,3,4
print(tup)

for i in 1,2,3,4:
    print("i:", i)

x,*y,z = 1,2,"hi",3,4
print(x)
print(y)
print(z)