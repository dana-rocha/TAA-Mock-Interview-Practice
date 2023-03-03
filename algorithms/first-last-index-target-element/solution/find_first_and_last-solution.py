def find_bound(nums, target, isFirst):
    '''
    [1, 1, 1, 2]
    target = 1
    n = len(nums)
    begin, end = 0, N - 1

    while begin <= end:
        calculate the mid point (mid)
        if nums[mid] is the target:
            if isFirst:
                if mid == begin or the number to the left is < target:
                    return mid
                end = mid - 1
            else:
                if mid == end or the number to the right is > target:
                    return mid
                begin = mid + 1
        elif mid point is greater than the target:
            end = mid - 1
        else:
            begin = mid + 1
    '''
    n = len(nums)
    begin, end = 0, n - 1

    while begin <= end:
        mid = int((begin + end) / 2)

        if nums[mid] == target:
            if isFirst:
                if mid == begin or nums[mid - 1] < nums[mid]:
                    return mid
                end = mid - 1
            else:
                if mid == end or nums[mid + 1] > nums[mid]:
                    return mid
                begin = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            begin = mid + 1

def find_first_last(nums, target):
    '''
    Given an array of integers `nums` sorted in ascending order, find the starting and ending           position of a given `target` value as a list.
    
    If the target is not found in the array, return [-1,-1]
    '''
    lower_bound = find_bound(nums, target, True)
    if lower_bound is None: return [-1, -1]

    upper_bound = find_bound(nums, target, False)

    return [lower_bound, upper_bound]