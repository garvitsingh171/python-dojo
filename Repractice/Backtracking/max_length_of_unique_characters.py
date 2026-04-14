def maxLengthUnique(arr):

    def backtrack(i, used):
        if i == len(arr):
            return len(used)

        res = backtrack(i+1, used)

        while len(set(arr[i])) == len(arr[i]) and not (set(arr[i]) & used):
            res = max(res, backtrack(i+1, used | set(arr[i])))

        return res

    return backtrack(0, set())


n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

print(maxLengthUnique(arr))
