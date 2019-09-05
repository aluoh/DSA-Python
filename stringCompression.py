def compress(n):
    """Compress a given string aabbbccc to a2b3c3"""
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    result = []
    if len(n) == 1:
        return n
    counter = 1
    for i in range(0, (len(n) - 1)):
        currChar = n[i]
        nextChar = n[i + 1]
        if currChar == nextChar:
            counter += 1
        else:
            result.append(currChar)
            if counter != 1:
                result.append(str(counter))
                counter = 1
            currChar = nextChar
        if i + 1 == len(n) - 1:
            result.append(currChar)
            if counter != 1:
                result.append(str(counter))
    ans = ""
    for i in result:
        ans += i
    return ans


def compress2(n):
    """ Prints a2b1a1c1d1 """
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    result = []
    if len(n) == 1:
        return n
    counter = 1
    for i in range(0, (len(n) - 1)):
        currChar = n[i]
        nextChar = n[i + 1]
        if currChar == nextChar:
            counter += 1
        else:
            result.append(currChar)
            result.append(str(counter))
            counter = 1
            currChar = nextChar
        if i + 1 == len(n) - 1:
            result.append(currChar)
            result.append(str(counter))
    ans = ""
    for i in result:
        ans += i
    return ans


print(compress(["a", "a", "b", "b", "c", "c", "c"]))
print(compress("ba"))
print(compress("aba"))
print(compress2("aab"))
print(compress("aabacd"))
