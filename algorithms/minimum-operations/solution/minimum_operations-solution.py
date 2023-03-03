def minimum_operations(nums):
    '''
    You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.

    Return the minimum number of operations needed to make nums strictly increasing.
    '''
    result = 0

    for i in range(1, len(nums)):
        curr = nums[i]
        prev = nums[i - 1]

        if curr <= prev:
            min_difference = prev - curr + 1
            result += min_difference
            nums[i] = prev + 1

    return result