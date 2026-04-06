def ranges_sum(nums):
    total = 0

    for i in range(len(nums)):
        curr_min = nums[i]
        curr_max = nums[i]

        for j in range(i, len(nums)):
            curr_min = min(curr_min, nums[j])
            curr_max = max(curr_max, nums[j])

            total += curr_max - curr_min

    return total


nums = list(map(int, input().split()))

print(ranges_sum(nums))
