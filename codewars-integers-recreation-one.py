import math


def list_squared(m, n):
    ans = []
    mDivisor = calculateDivisors(m)
    nDivisor = calculateDivisors(n)
    currSum = 0
    for i in range(len(mDivisor)):
        if currSum < m:
            currSum += mDivisor[i]
        else:
            ans.append(m)
            ans.append(currSum ** 2)
    return ans


def calculateDivisors(x):
    ans = []
    for i in range(1, x+1):
        if x % i == 0:
            ans.append(i**2)
    return ans


print(list_squared(42, 250))
