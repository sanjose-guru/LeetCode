from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 1: s -> should have all word in words
        # 2: all word in words are of same len!
        # 3: words can repeat!
        # from 1 & 2: concatenated string len should be num_words in words * word_len
        # Sliding window and at each slide check if we a matching word
        #
        # Important optimization
        # * Sliding the window by one char at a time will end will hit time exceed for
        #    large inputs
        # * So we will start the sliding window only for single word length, this should
        #    align all words chain

        if not s or not words:
            return []

        w_len = len(words[0])  # all words are same len, get len from 1st word
        num_words = len(words)  # this will include duplicate words.
        c_str_len = num_words * w_len  # length of concatenated string should be

        s_len = len(s)
        if s_len < c_str_len:
            return []

        word_counter = Counter(words)  # counter is a hash and give O(1) lookup
        res = []

        # *** Loop over w_len possible starting offsets ***
        for offset in range(w_len):
            left = offset
            right = offset
            seen_word = Counter()
            count = 0  # Number of valid words matched in current window

            while right + w_len <= s_len:
                word = s[right : right + w_len]
                right += w_len

                if word in word_counter:
                    seen_word[word] += 1
                    count += 1

                    # Too many of this word in window → shrink from left
                    while seen_word[word] > word_counter[word]:
                        left_word = s[left : left + w_len]
                        seen_word[left_word] -= 1
                        left += w_len
                        count -= 1

                    # All words matched exactly once
                    if count == num_words:
                        res.append(left)

                else:
                    # Reset if word not in word list
                    seen_word = Counter()
                    count = 0
                    left = right

        return res
