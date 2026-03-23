def threeSumClosest(nums, target):
    nums.sort()
    closest = float('inf')
    result = 0

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if abs(total - target) < closest:
                closest = abs(total - target)
                result = total

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return total

    return result


nums = list(map(int, input().split()))

target = int(input())

print(threeSumClosest(nums, target))
