def calcRecurse(num):
    if num < 10:
        return num
    else:
        currMax = num % 10
        num2 = calcRecurse(num // 10)
        if num2 > currMax:
            currMax = num2
        return currMax


def calcRecurse2(num, currMax):
    newMax = num % 10
    if currMax > newMax:
        newMax = currMax
    if num < 10:
        return newMax
    return calcRecurse2(num // 10, newMax)


print(calcRecurse2(1, -1))
