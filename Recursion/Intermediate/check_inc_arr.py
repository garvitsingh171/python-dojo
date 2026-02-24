def isIncreasing(arr):
    if len(arr) == 1:
        return True
    if arr[0] > arr[1]:
        return False
    return isIncreasing(arr[1:])


n = int(input())
arr = list(map(int, input().split()))

print(isIncreasing(arr))
