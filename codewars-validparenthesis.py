def valid_parentheses(string):
    if string == "":
        return True
    elif string[0] == ')':
        return False
    else:
        stack = []
        for i in string:
            if i == '(':
                stack.append(i)
            elif stack and i == ')':
                stack.pop()
            elif not stack and i == ')':
                return False
        return not stack
    # your code here


ss = "wc(feemawuu(rgvnf)jh)aju)"
zz = valid_parentheses(ss)
print(zz)
