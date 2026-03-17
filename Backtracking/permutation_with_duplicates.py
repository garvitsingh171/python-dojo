def permutation(nums):
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums) and path[:] not in result:
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            path.append(nums[i])
            used[i] = True

            backtrack(path)

            path.pop()
            used[i] = False

    backtrack([])
    return result


arr = list(map(int, input().split()))

print(permutation(arr))
