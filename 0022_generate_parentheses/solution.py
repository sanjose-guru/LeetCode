from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []
        size = 2 * n

        def dfs(path: List[str], opened, closed: int):
            if len(path) == size:
                res.append("".join(path))
                return

            # we have 2 paths: one for '(' and one for ')'
            # So specifying it directly instead of using loop.
            if opened < n:
                path.append("(")
                dfs(path, opened + 1, closed)
                path.pop()
            if closed < opened:
                path.append(")")
                dfs(path, opened, closed + 1)
                path.pop()

        dfs([], 0, 0)
        return res
