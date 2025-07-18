# [1151. Minimum Swaps to Group All 1's Together](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/description/)

Given abinary array <code>data</code>, returnthe minimum number of swaps required to group all <code>1</code>’s present in the array together in **any place** in the array.

**Example 1:**

```
Input: data = [1,0,1,0,1]
Output: 1
Explanation: There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
```

**Example 2:**

```
Input: data = [0,0,0,1,0]
Output: 0
Explanation: Since there is only one 1 in the array, no swaps are needed.
```

**Example 3:**

```
Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
```

**Constraints:**

- <code>1 <= data.length <= 10^5</code>
- <code>data[i]</code> is either <code>0</code> or <code>1</code>.
