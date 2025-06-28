# [325. Maximum Size Subarray Sum Equals k](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/)

Given an integer array `nums` and an integer `k`, return the maximum length of a
<button type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="radix-:rs:" data-state="closed" class="">subarray</button>
that sums to `k`. If there is not one, return `0` instead.

**Example 1:**

```
Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
```

**Example 2:**

```
Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
```

**Constraints:**

- `1 <= nums.length <= 2 \* 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `-10^9<= k <= 10^9`
