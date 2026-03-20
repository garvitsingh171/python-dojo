def combination_sum(arr, target):
    result = []
    arr.sort()

    def backtrack(start, path, target):
        if target == 0:
            result.append(path[:])
            return

        if target < 0:
            return

        for i in range(start, len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                continue

            path.append(arr[i])
            backtrack(i+1, path, target - arr[i])
            path.pop()

    backtrack(0, [], target)
    return result


arr = list(map(int, input().split()))

target = int(input())

print(combination_sum(arr, target))
