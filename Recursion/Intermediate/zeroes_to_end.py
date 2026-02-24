def zerosToEnd(arr, i=0):
    if len(arr) == 0:
        return []

    rest = zerosToEnd(arr[1:], i+1)

    if arr[0] == 0:
        return rest + [0]
    else:
        return [arr[0]] + rest


n = int(input())
arr = list(map(int, input().split()))
count = 0

print(*zerosToEnd(arr))
