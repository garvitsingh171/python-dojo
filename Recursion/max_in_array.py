# Way-01
def maxElementInArray(arr):
    if len(arr) == 1:
        return arr[0]

    max_of_rest = maxElementInArray(arr[1:])

    if arr[0] > max_of_rest:
        return arr[0]
    else:
        return max_of_rest


# Way-02
def maxEleInArray(arr, i):
    if i == len(arr):
        return arr[i]
    return max(arr[0], maxEleInArray(arr[1:]))


i = 0
n = int(input())
arr = list(map(int, input().split()))

print(maxElementInArray(arr))
print(maxEleInArray(arr, i))
