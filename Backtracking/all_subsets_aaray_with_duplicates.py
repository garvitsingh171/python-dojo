def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):

            if nums[i] == nums[i-1]:
                continue

            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()

    backtrack(0, [])
    return result


arr = list(map(int, input().split()))
arr.sort()

print(subsets(arr))
