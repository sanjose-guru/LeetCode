from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []

        def dfs(s_index: int, path: List[int]) -> None:
            # Every path is a subset
            res.append(path[:])

            for i in range(s_index, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return res
