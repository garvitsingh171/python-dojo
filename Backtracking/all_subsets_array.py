def subsets(arr, i, curr):
    if i == len(arr):
        print(curr)
        return

    curr.append(arr[i])
    subsets(arr, i+1, curr)
    curr.pop()

    subsets(arr, i+1, curr)


n = int(input())
arr = list(map(int, input().split()))
curr = []
i = 0

subsets(arr, i, curr)
