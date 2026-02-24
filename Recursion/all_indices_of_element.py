def allIndices(arr, x, i):
    if len(arr) == 0:
        return
    if arr[0] == x:
        print(i, end=' ')
    return allIndices(arr[1:], x, i+1)


n = int(input())
arr = list(map(int, input().split()))
x = int(input())
i = 0

allIndices(arr, x, i)
