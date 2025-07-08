class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        nums_len = len(nums)
        res = []

        # We have 2 more numbers to consider, so -2
        for i in range(nums_len - 2):
            # skip duplicates
            # checking nums[i] == nums[i+1] may skip a solution like [-1, -1, 2]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Now this is a 2 sum problem
            l, r = i + 1, nums_len - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]

                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:  # we have a triplet answer
                    res.append([nums[i], nums[l], nums[r]])

                    # skip duplicates
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
