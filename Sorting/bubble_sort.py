def bubbleSort(arr):
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return


n = int(input())

arr = list(map(int, input().split()))

bubbleSort(arr)

for k in range(n):
    print(arr[k], end=' ')
