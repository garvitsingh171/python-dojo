def subsequence(arr):
    result = []

    def backtrack(path, start):
        if len(path) >= 2:
            result.append(path[:])

        used = set()

        for i in range(start, len(arr)):

            if arr[i] in used:
                continue

            if not path or arr[i] >= path[-1]:
                used.add(arr[i])
                path.append(arr[i])
                backtrack(path, i+1)
                path.pop()

    backtrack([], 0)
    return result


arr = list(map(int, input().split()))

print(subsequence(arr))
