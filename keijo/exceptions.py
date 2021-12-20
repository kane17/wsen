error = True
while error:
    try:
        num = float(input("eine positive Zahl: "))
        if num < 0:
            raise RuntimeError
        r = 1.0 / num
        error = False
    except:
        print("run time error")
        if error == False:
            print("The reciprocal of ", num, "is: ", r)


def summe(a,b):
    res = a +b
    return res


for i in range(5):
    sum = summe(10,i)
    #sum +=sum
    print(sum)