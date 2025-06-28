class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_cntr, w_cntr = [0] * 26, [0] * 26
        res, w_len = [], len(p)
        a = ord("a")

        for i in range(w_len):
            p_cntr[ord(p[i]) - a] += 1
            w_cntr[ord(s[i]) - a] += 1

        if w_cntr == p_cntr:
            res.append(0)

        for i in range(w_len, len(s)):
            w_cntr[ord(s[i]) - a] += 1
            w_cntr[ord(s[i - w_len]) - a] -= 1

            if w_cntr == p_cntr:
                res.append(i - w_len + 1)

        return res
