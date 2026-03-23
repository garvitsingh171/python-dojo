def subset(arr):
    result = []

    def backtrack(path, start):
        result.append(path[:])

        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(path, start+1)
            path.pop()

    backtrack([], 0)
    return result


arr = list(map(int, input().split()))

print(subset(arr))
