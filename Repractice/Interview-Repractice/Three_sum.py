"""3Sum using sorting + two pointers.

TC: O(n^2) after sorting.
Sorting is O(n log n), which is dominated by two-pointer scanning.
SC: O(1) auxiliary if sort is in-place (excluding output storage).
"""


def threeSum(nums):
    nums.sort()
    res = []

    for i in range(len(nums) - 2):
        left = i+1
        right = len(nums) - 1

        if i > 0 and nums[i] == nums[i-1]:
            continue

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                res.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return res


nums = list(map(int, input().split()))

print(threeSum(nums))
