def spy_game(nums):
    checar007 = ""

    for num in nums:
        if num == 0 or num == 7:
            checar007 = checar007 + str(num)

    if checar007 == '007':
        return True
    else:
        return False