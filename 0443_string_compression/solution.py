class Solution:
    def compress(self, chars: List[str]) -> int:
        insert, l = 0, 0

        for r in range(len(chars)):
            # if we are at last char or next char is different we have to compress
            if r + 1 == len(chars) or chars[r] != chars[r + 1]:
                chars[insert] = chars[r]
                insert += 1

                c_len = r - l + 1
                if c_len > 1:
                    for c in str(c_len):
                        chars[insert] = c
                        insert += 1
                l = r + 1
        return insert
