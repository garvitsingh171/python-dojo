def ranges_sum(n, nums):
    total = 0

    for i in range(n):
        curr_min = nums[i]
        curr_max = nums[i]

        for j in range(i, n):
            curr_min = min(curr_min, nums[j])
            curr_max = max(curr_max, nums[j])

            total += curr_max - curr_min

    return total


n = int(input())

nums = list(map(int, input().split()))

print(ranges_sum(n, nums))
