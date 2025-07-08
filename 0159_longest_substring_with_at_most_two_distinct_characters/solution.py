class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        distinct_chars = dict()
        max_len, l = 0, 0

        for r, c in enumerate(s):
            # update last known index of a char
            distinct_chars[c] = r

            # if we have more number of distinct chars,
            # move l to index after left most char.
            if len(distinct_chars) > 2:
                # get left most char (lowest index)
                leftmost_index = min(distinct_chars.values())
                l = leftmost_index + 1  # move left pointer after the the left most char
                del distinct_chars[s[leftmost_index]]  # remove the char from window
            # keep updating of max_len as we iterate
            max_len = max(max_len, r - l + 1)
        return max_len
