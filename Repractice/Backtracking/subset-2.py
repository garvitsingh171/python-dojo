def subset(arr):
    result = []

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                continue

            path.append(arr[i])
            backtrack(i+1, path)
            path.pop()

    backtrack(0, [])
    return result


arr = list(map(int, input().split()))

print(subset(arr))
