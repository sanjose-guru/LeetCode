from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res: List[List[int]] = []

        def dfs(remaining: int, s_index: int, path: List[int]) -> None:
            # we have a solution copy the path to results.
            if remaining == 0:
                res.append(path[:])
                return

            # No solution for this path.
            if remaining < 0:
                return

            for i in range(s_index, len(candidates)):
                path.append(candidates[i])
                dfs(remaining - candidates[i], i, path)
                path.pop()

        dfs(target, 0, [])
        return res
