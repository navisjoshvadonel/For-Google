def lengthOfLongestSubstring(s):
    char_set = set()       # characters currently in our window
    left = 0                # left edge of window
    max_len = 0              # best answer so far

    for right in range(len(s)):
        # if duplicate found, shrink window from the left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])               # add current char to window
        max_len = max(max_len, right - left + 1)  # update best length

    return max_len

# Test
print(lengthOfLongestSubstring("abcabcbb"))  # 3
print(lengthOfLongestSubstring("bbbbb"))     # 1
print(lengthOfLongestSubstring("pwwkew"))    # 3