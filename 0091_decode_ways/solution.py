from typing import Dict


class Solution:
    def numDecodings(self, s: str) -> int:
        memo: Dict[int, int] = {}
        s_len = len(s)

        def dfs(c_index):
            # short circuit with memo
            if c_index in memo:
                return memo[c_index]

            # If we are at end of string, which is one digit, we have only one way to decode it.
            if c_index == s_len:
                return 1

            # 0 is not valid
            if s[c_index] == "0":
                return 0

            # Decode one digit
            ways = dfs(c_index + 1)

            # branch out and decode two digits if it is in valid range
            # c_index + 2 -> as it is not included (exclusive)
            if c_index + 1 < s_len and 10 <= int(s[c_index : c_index + 2]) <= 26:
                ways += dfs(c_index + 2)

            # store memo and return
            memo[c_index] = ways
            return ways

        # call backtrack from starting index
        return dfs(0)
