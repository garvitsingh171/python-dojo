def max_length(arr):
    def backtrack(i, used):
        if i == len(arr):
            return len(used)

        res = backtrack(i+1, used)

        if len(set(arr[i])) == len(arr[i]) and not (set(arr[i]) & used):
            res = max(res, backtrack(i+1, used | set(arr[i])))

        return res

    return backtrack(0, set())


arr = list(map(str, input().split()))

print(max_length(arr))
