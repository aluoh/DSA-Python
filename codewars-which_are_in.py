def in_array(array1, array2):
    if not array1 or not array2:
        return []
    r = []
    for i in range(len(array1)):
        for j in range(len(array2)):
            if array1[i] in array2[j]:
                if array1[i] not in r:
                    r.append(array1[i])
    r.sort()
    return r


a1 = ["arp", "live", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
print(in_array(a1, a2))
