class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        comb_len = len(digits)
        res = []

        def comb_helper(index: int, comb: list[str]) -> None:
            if len(comb) == comb_len:
                res.append("".join(comb))
                return

            # One digit per recursion.
            for c in char_map[digits[index]]:
                comb.append(c)  # Add choice
                comb_helper(index + 1, comb)  # Delegate
                comb.pop()  # remove choice

        comb_helper(0, [])
        return res
