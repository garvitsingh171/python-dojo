def permutation(nums):
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            if nums[i] == nums[i-1] and not used[i-1]:
                continue

            path.append(nums[i])
            used[i] = True

            backtrack(path)

            path.pop()
            used[i] = False

    backtrack([])
    return result


arr = list(map(int, input().split()))
arr.sort()

print(permutation(arr))
