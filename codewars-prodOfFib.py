def productFib(prod):
    if prod == 0:
        return [0, 1, True]
    listOfAns = []
    i = 2
    num1 = 0
    num2 = 1
    while num1 * num2 < prod:
        num1 = fibRecur(i)
        num2 = fibRecur(i+1)
        if num1 * num2 == prod:
            listOfAns = [num1, num2, True]
        else:
            listOfAns = [num1, num2, False]
        i += 1
    return listOfAns


def calcFib(n):
    if n == 0:
        return 0
    num2 = 0  # n-2
    num1 = 1  # n-1
    theSum = 1
    i = 2
    while i < n:
        theSum = num1 + num2
        temp = num1
        num1 = theSum
        num2 = temp
        i += 1
    return theSum


def fibRecur(n):
    if n <= 1:
        return n
    else:
        return(fibRecur(n-1) + fibRecur(n-2))


print(productFib(5895))
