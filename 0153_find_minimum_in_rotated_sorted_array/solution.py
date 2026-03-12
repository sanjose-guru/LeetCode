class Solution:
    def findMin(self, nums: List[int]) -> int:
        li, ri = 0, len(nums) - 1

        while li < ri:
            mid = (li + ri) // 2
            # if middle is greater than end, rotate min must be on right side.
            if nums[mid] > nums[ri]:
                li = mid + 1
            else:  # the min must be on left side (including mid)
                ri = mid
        return nums[li]
