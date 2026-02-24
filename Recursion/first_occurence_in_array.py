def firstOccurence(arr, x, i):
    if len(arr) == 0:
        return -1
    if arr[1] == x:
        return i
    return firstOccurence(arr[1:], x, i+1)


n = int(input())
arr = list(map(int, input().split()))
x = int(input())
i = 0

print(firstOccurence(arr, x, i))
