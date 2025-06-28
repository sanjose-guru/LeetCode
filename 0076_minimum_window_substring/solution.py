class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start, end, left = 0, 0, 0
        min_len = float("inf")

        charFreq = Counter(t)
        charsNeeded = len(charFreq)

        for right, c in enumerate(s):
            # If we stepped on a char in the frequency map
            # Check if we have found all chars, if so move left pointer
            # Until we dont have a matching substring and update start and end
            # if new substring is smaller
            if c in charFreq:
                charFreq[c] -= 1
                # If we have all of this char.
                if charFreq[c] == 0:
                    charsNeeded -= 1

                # While we have all the chars we needed, move left pointer (reduce string size).
                while charsNeeded == 0:
                    # if subtring is smaller
                    if min_len > (right - left):
                        start, end = left, right
                        min_len = right - left

                    if s[left] in charFreq:
                        charFreq[s[left]] += 1

                    # if we lost a needed char
                    if charFreq[s[left]] > 0:
                        charsNeeded += 1  # this will break out from the loop

                    left += 1  # reduce the substring size.

        if min_len == float("inf"):
            return ""
        return s[start : end + 1]  # include end index
