def isPalindrome(string, left, right):
    if left >= right:
        return True
    if string[left] != string[right]:
        return False
    return isPalindrome(string, left+1, right-1)


string = input()
left = 0
right = len(string)-1
print(isPalindrome(string, left, right))
