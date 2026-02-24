def minInArray(arr):
    if len(arr) == 1:
        return arr[0]
    return min(arr[0], minInArray(arr[1:]))


arr = list(map(int, input().split()))
print(minInArray(arr))
