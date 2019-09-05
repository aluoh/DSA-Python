def climbStairs(n):
    if n <= 1:
        return 1
    counter = 2
    a = 1
    b = 1
    rem = 0
    while counter <= n:
        rem = a + b
        a = b
        b = rem
        counter += 1
    return rem

def tribonacci(n):
    """ T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0. """
    
    if n == 0:
        return 0
    elif n > 0 and n <= 2:
        return 1
    return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)

print(tribonacci(25))