def twoSum(nums, target):
    seen = {}  # stores { number: index }

    for i, num in enumerate(nums):
        complement = target - num  # what we need

        if complement in seen:
            return [seen[complement], i]  # found it!

        seen[num] = i  # remember this number

# Test it
print(twoSum([2, 7, 11, 15], 9))   # [0, 1]
print(twoSum([3, 2, 4], 6))        # [1, 2]
print(twoSum([3, 3], 6))           # [0, 1]