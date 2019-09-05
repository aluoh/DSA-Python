def majorityElement(nums):
    myDict = {}
    ans = []
    for i in nums:
        if i in myDict:
            myDict[i] += 1
        else:
            myDict[i] = 1
    for k, v in myDict.items():
        if myDict[k] > len(nums)/3:
            ans.append(k)
    return ans


nums = [1, 1, 1, 3, 3, 2, 2, 2]
print(majorityElement(nums))
