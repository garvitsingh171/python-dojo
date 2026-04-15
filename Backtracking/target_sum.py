def target_sum(nums, target):
    memo = {}

    def backtrack(i, curr_sum):
        if i == len(nums):
            if curr_sum == target:
                return 1
            else:
                return 0

        if (i, curr_sum) in memo:
            return memo[(i, curr_sum)]

        plus = backtrack(i + 1, curr_sum + nums[i])

        minus = backtrack(i + 1, curr_sum - nums[i])

        memo[(i, curr_sum)] = plus + minus
        return memo[(i, curr_sum)]

    return backtrack(0, 0)


nums = list(map(int, input().split()))
target = int(input())

print(target_sum(nums, target))
