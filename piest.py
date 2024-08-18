import random
import math



def mean(arr):
    
    sum = 0

    for a in arr:
        sum += a

    return sum/(len(arr))




def calculatePI(arr):
    return 4*(1-(sum(arr)/len(arr)))

def calculateOn(n):

    Xs = []
    Ys = []

    for i in range(n):
        Xs.append(random.random())
        Ys.append(random.random())

    Ds = [x**2 + y**2 for x, y in zip(Xs, Ys)]

    Bs = [0 if d <=1 else 1 for d in Ds]

    estPI = calculatePI(Bs)
    PI = math.pi

    err = (abs(estPI-PI)/PI) * 100

    return [estPI, err]




def main():

    res = []

    iterations = 10

    for i in range(iterations):
        res.append(calculateOn(10000000))

    estPIs = []
    errs = []

    for arr in res:
        estPIs.append(arr[0])
        errs.append(arr[1])

    ePI = mean(estPIs)
    ERR = mean(errs)

    print(str(ePI) + "   |   " + str(ERR) + "\n3.1415926535897932")





if __name__ == "__main__":
    main()