def balance_check(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(")")
        elif i == "{":
            stack.append("}")
        elif i == "[":
            stack.append("]")
        else:
            if stack:
                peek = stack[-1]
                if i != peek:
                    return False
                else:
                    stack.pop()
    return not stack


print(balance_check("[[[]])]"))

