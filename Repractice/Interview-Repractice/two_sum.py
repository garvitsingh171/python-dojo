"""Two Sum using a hash map of value -> index.

TC: O(n) single pass.
SC: O(n) for the hash map in the worst case.
"""


def two_sum(nums, target):
    hashmap = {}

    for i in range(len(nums)):
        comp = target - nums[i]

        if comp in hashmap:
            return [hashmap[comp], i]

        hashmap[nums[i]] = i


nums = list(map(int, input().split()))
target = int(input())

print(two_sum(nums, target))
