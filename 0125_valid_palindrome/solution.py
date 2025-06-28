class Solution:
    def isPalindrome(self, s: str) -> bool:
        li, ri = 0, len(s) - 1
        while li < ri:
            if not s[li].isalnum():
                li += 1
                continue

            if not s[ri].isalnum():
                ri -= 1
                continue

            if s[li].lower() != s[ri].lower():
                return False

            li += 1
            ri -= 1
        return True
