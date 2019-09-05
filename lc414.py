def thirdMax(nums):
    three = float("-inf")
    two = float("-inf")
    main = float("-inf")
    for i in nums:
        if i > main:
            two = main
            three = two
            main = i
        elif i > two:
            three = two
            two = i
        elif i > three:
            three = i
    return three


thirdMax([3, 2, 1])

