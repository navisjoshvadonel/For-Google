def climbStairs(n):
    if n <= 2:
        return n

    prev2 = 1   # ways to reach step 1
    prev1 = 2   # ways to reach step 2

    for i in range(3, n + 1):
        curr = prev1 + prev2   # ways to reach current step
        prev2 = prev1          # slide window forward
        prev1 = curr

    return prev1

# Test
print(climbStairs(2))   # 2
print(climbStairs(3))   # 3
print(climbStairs(4))   # 5
print(climbStairs(5))   # 8