class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        w_s, w_sum, res = 0, 0, float("inf")

        for w_e in range(len(nums)):
            w_sum += nums[w_e]
            while w_sum >= target:
                res = min(res, (w_e - w_s) + 1)
                w_sum -= nums[w_s]
                w_s += 1

        if res == float("inf"):
            return 0
        return res
