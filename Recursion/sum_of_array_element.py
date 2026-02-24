def sumOfArrayElement(arr, i):
    if i == len(arr):
        return 0
    return arr[i] + sumOfArrayElement(arr, i+1)


i = 0
n = int(input())
arr = list(map(int, input().split()))

print(sumOfArrayElement(arr, i))
