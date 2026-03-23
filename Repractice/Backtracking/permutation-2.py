def permutation(arr):
    result = []
    used = [False] * len(arr)

    def backtrack(path):
        if len(path) == len(arr):
            result.append(path[:])
            return

        for i in range(len(arr)):
            if used[i]:
                continue

            if i > 0 and arr[i] == arr[i-1] and not used[i-1]:
                continue

            path.append(arr[i])
            used[i] = True

            backtrack(path)

            path.pop()
            used[i] = False

    backtrack([])
    return result


arr = list(map(int, input().split()))
arr.sort()

print(permutation(arr))
