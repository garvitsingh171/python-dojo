def beautiful_permutation(n):
    result = []
    used = [False] * n

    arr = []
    for i in range(1, n + 1):
        arr.append(i)

    def backtrack(path):
        if len(path) == n:
            result.append(path[:])
            return

        for i in range(n):
            if used[i]:
                continue

            path.append(arr[i])
            used[i] = True

            backtrack(path)

            path.pop()
            used[i] = False

    backtrack([])
    # return result

    count = 0
    beauty = []

    for arr in result:
        valid = True
        for i in range(n):
            if arr[i] % (i+1) != 0 and (i+1) % arr[i] != 0:
                valid = False
                break

        if valid:
            count += 1
            beauty.append(arr)

    return count, beauty


n = int(input())

print(beautiful_permutation(n))
