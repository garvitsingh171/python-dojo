def combination(n, k):
    result = []

    def backtrack(path, start):
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(start, n+1):
            path.append(i)
            backtrack(path, i+1)
            path.pop()

    backtrack([], 1)
    return result


n = int(input())
k = int(input())

print(combination(n, k))
