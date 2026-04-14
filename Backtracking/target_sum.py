def target_sum(nums, target):

    def backtrack(i, curr_sum):
        if i == len(nums):
            if curr_sum == target:
                return 1
            else:
                return 0

        plus = backtrack(i + 1, curr_sum + nums[i])

        minus = backtrack(i + 1, curr_sum - nums[i])

        return plus + minus

    return backtrack(0, 0)


nums = list(map(int, input().split()))
target = int(input())

print(target_sum(nums, target))
