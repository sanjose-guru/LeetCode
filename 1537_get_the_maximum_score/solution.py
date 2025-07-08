class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1_idx, n2_idx = 0, 0
        n1_sum, n2_sum = 0, 0
        MOD = 10**9 + 7

        while n1_idx < len(nums1) and n2_idx < len(nums2):
            if nums1[n1_idx] < nums2[n2_idx]:
                n1_sum += nums1[n1_idx]
                n1_idx += 1
            elif nums2[n2_idx] < nums1[n1_idx]:
                n2_sum += nums2[n2_idx]
                n2_idx += 1
            else:
                # num is same on both array, we can teleport
                # find the max so far and store it to both sums
                n1_sum = n2_sum = max(n1_sum, n2_sum) + nums1[n1_idx]
                n1_idx += 1
                n2_idx += 1

        while n1_idx < len(nums1):
            n1_sum += nums1[n1_idx]
            n1_idx += 1

        while n2_idx < len(nums2):
            n2_sum += nums2[n2_idx]
            n2_idx += 1

        return max(n1_sum, n2_sum) % MOD
