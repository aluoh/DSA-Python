def create_phone_number(n):
    curr = '('
    for i in n:
        if len(curr) == 4:
            curr += ') '
        elif len(curr) == 9:
            curr += '-'
        curr += str(i)

    # your code here
    return curr


test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
fin = create_phone_number(test)
print(fin)
