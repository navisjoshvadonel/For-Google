def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2 = nums[0]              # best up to house 0
    prev1 = max(nums[0], nums[1]) # best up to house 1

    for i in range(2, len(nums)):
        curr = max(prev1, nums[i] + prev2)  # rob or skip
        prev2 = prev1
        prev1 = curr

    return prev1

# Test
print(rob([1, 2, 3, 1]))      # 4
print(rob([2, 7, 9, 3, 1]))   # 12
print(rob([2, 1, 1, 2]))      # 4