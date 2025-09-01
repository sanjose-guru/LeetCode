from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        str_len = len(s)

        def is_palindrome(ss: str) -> bool:
            return ss == ss[::-1]

        def comb_helper(start_index: int, path: List[str]):
            # base case
            # if the index has reached end of string we have a solution
            print(f"start_index: {start_index}, path: {path}")
            if start_index == str_len:
                res.append(path[:])  # append copy of path
                print(f"sol found: {path}")
                return

            # range will exclude last value so string_len+1
            for part_end in range(start_index + 1, str_len + 1):
                # continue the path only if current partition is palindrome
                if is_palindrome(s[start_index:part_end]):
                    print(
                        f"part found: {start_index}, {part_end}, {s[start_index:part_end]}"
                    )
                    path.append(s[start_index:part_end])  # Add combination
                    comb_helper(part_end, path)  # delegate for remaining string
                    path.pop()  # Remove comb: backtrack
                    print(f"popped: {path}")
                print(f"part_end: {part_end} p: {s[start_index:part_end]}")

        comb_helper(0, [])
        return res


if __name__ == "__main__":
    sol = Solution()
    print(f"{sol.partition('aeaba')}")
