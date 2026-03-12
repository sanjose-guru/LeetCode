class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        li, ri, res = max(nums), sum(nums), 0

        while li <= ri:
            mid = (li + ri) // 2
            split, l_sum = self.can_split(nums, mid, k)
            if split:
                res = l_sum
                ri = mid - 1
            else:
                li = mid + 1

        return res

    def can_split(self, nums: List[int], target, k: int) -> (bool, int):
        sum, l_sum, count = 0, 0, 0

        for n in nums:
            if sum + n > target:
                l_sum = max(sum, l_sum)
                sum = n
                count += 1
                if count >= k:
                    return (False, 0)
            else:
                sum += n
        return (True, max(sum, l_sum))
