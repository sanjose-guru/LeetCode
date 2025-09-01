from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []

        a_len = len(nums)
        # To skip already add num to the path.
        used = [False] * a_len

        def dfs(path: List[int], used: List[bool]) -> None:
            # base case
            if len(path) == a_len:
                res.append(path[:])  # add a copy of path
                return

            for i, n in enumerate(nums):
                # trim path
                if used[i]:
                    continue

                # add to path
                path.append(n)
                used[i] = True
                dfs(path, used)  # delegate
                # remove from path
                path.pop()
                used[i] = False

        dfs([], used)
        return res
