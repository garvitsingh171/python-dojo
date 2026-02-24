def isPalindrome(arr, left, right):
    if left == right or left > right:
        return True
    if arr[left] == arr[right]:
        return False
    return isPalindrome(arr, left+1, right-1)


n = int(input())
left = 0
right = n-1
arr = list(map(int, input().split()))

print(isPalindrome(arr, left, right))
