def combination(nums, target):
    result = []

    def backtrack(start, path, target):
        if target == 0:
            result.append(path[:])
            return

        if target < 0:
            return

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i, path, target - nums[i])
            path.pop()

    backtrack(0, [], target)
    return result


arr = list(map(int, input().split()))
target = int(input())

print(combination(arr, target))
