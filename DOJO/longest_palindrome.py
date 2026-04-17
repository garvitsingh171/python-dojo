def longest_palindrome(s):
    res = ""

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    for i in range(len(s)):
        if len(s) % 2 != 0:
            temp = expand(i, i)
        else:
            temp = expand(i, i+1)

        if len(temp) > len(res):
            res = temp

    return res


s = input()

print(longest_palindrome(s))
