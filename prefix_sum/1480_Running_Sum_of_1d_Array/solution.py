class Solution:

    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]
        return nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.runningSum([1, 2, 3, 4]))
