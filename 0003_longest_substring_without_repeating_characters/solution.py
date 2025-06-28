class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        win_start, win_end, max_len = 0, 0, 0

        for win_end, c in enumerate(s):
            # if we find a duplicate char
            # update start if we have to (if old index is with in our window)
            if c in char_index and char_index[c] >= win_start:
                win_start = char_index[c] + 1
            char_index[c] = win_end
            max_len = max(max_len, (win_end - win_start + 1))

        return max_len


if __name__ == "__main__":
    sol = Solution()
    print(f"{sol.lengthOfLongestSubstring(' ')}")
    print(f"{sol.lengthOfLongestSubstring('')}")
