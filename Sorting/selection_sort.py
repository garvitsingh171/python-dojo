def selectionSort(arr):
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return


n = int(input())

arr = list(map(int, input().split()))

selectionSort(arr)

for k in range(n):
    print(arr[k], end=' ')
