class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lookup = dict()
        for i, n in enumerate(nums):
            diff = target - n
            if diff in lookup:
                return [i, lookup[diff]]
            lookup[n] = i
