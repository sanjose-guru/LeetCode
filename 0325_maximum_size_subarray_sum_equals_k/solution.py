class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        max_len, prefix_sum = 0, 0
        prefix_sum_map = {0: -1}  # for result 0, we can start from begining of array.

        for i, num in enumerate(nums):
            prefix_sum += num

            # if we found a match
            if (prefix_sum - k) in prefix_sum_map:
                max_len = max(max_len, i - prefix_sum_map[prefix_sum - k])

            # Store the left most (1st) index for prefix_sum.
            # If the prefix_sum key already exist, we have left most index
            #  already, so dont update.
            if prefix_sum not in prefix_sum_map:
                prefix_sum_map[prefix_sum] = i

        return max_len
