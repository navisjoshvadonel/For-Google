def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2   # find middle index

        if nums[mid] == target:
            return mid               # found it!
        elif nums[mid] < target:
            left = mid + 1           # search right half
        else:
            right = mid - 1          # search left half

    return -1   # target not found

# Test
print(search([-1, 0, 3, 5, 9, 12], 9))   # 4
print(search([-1, 0, 3, 5, 9, 12], 2))   # -1