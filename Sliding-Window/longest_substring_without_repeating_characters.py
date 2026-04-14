def maxLengthOfSubstring(s):
    seen_char = set()

    max_len = 0
    left = 0

    for right in range(len(s)):

        while s[right] in seen_char:
            seen_char.remove(s[left])
            left += 1

        seen_char.add(s[right])

        max_len = max(max_len, right - left + 1)

    return max_len


s = input()

print(maxLengthOfSubstring(s))
