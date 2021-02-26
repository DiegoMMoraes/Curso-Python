def has_33(nums):
    check33 = 0
    for num in nums:
        if num == 3:
            check33 = check33 + 1
            if check33 == 2:
                break
        else:
            check33 = 0
    if check33 == 2:
        return True
    else:
        return False