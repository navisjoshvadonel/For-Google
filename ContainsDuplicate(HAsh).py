def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:      # already seen this number
            return True
        seen.add(num)        # add to memory

    return False             # no duplicates found

# Test
print(containsDuplicate([1, 2, 3, 1]))        # True
print(containsDuplicate([1, 2, 3, 4]))        # False
print(containsDuplicate([1,1,1,3,3,4,3,2]))  # True