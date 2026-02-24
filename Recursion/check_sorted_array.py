def checkSortedArray(arr, i):
    if i == len(arr) - 1:
        return True
    if arr[i] > arr[i+1]:
        return False
    return checkSortedArray(arr, i+1)


i = 0
n = int(input())
arr = list(map(int, input().split()))

print(checkSortedArray(arr, i))
