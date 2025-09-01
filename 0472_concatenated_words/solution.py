from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def canFormWord(
        self, word: str, cur_index: int, words_count: int, mem: dict
    ) -> bool:
        # short circuit if we have already evals the word till cur_inde.
        if cur_index in mem:
            return mem[cur_index]

        node = self.root
        for i in range(cur_index, len(word)):
            ch = word[i]
            if ch not in node.children:
                mem[cur_index] = False
                return False

            node = node.children[ch]
            if node.is_word:
                if i == len(word) - 1:
                    mem[cur_index] = words_count >= 1  # At least 2 subwords used
                    return mem[cur_index]
                if self.canFormWord(word, i + 1, words_count + 1, mem):
                    mem[cur_index] = True
                    return True
        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            if word:  # skip empty strings
                trie.addWord(word)

        result = []
        for word in words:
            if not word:
                continue
            # Temporarily remove word if needed, or just be careful in search logic (here .search won't use word itself)
            if trie.canFormWord(word, 0, 0, {}):
                result.append(word)
        return result

    # this is better solution.
    def findAllConcatenatedWordsInADict_dp(self, words: List[str]) -> List[str]:
        memo = {}

        # sets are faster for lookup as they are stored as hash.
        word_set = set(words)

        def canFormWord(word):
            if word in memo:
                return memo[word]

            # concated word has to be formed by 2 words, so split as prefix and suffix
            for i in range(1, len(word)):  # no point in prefix with 0 chars
                prefix = word[:i]
                suffix = word[i:]

                if prefix in word_set and (suffix in word_set or canFormWord(suffix)):
                    memo[word] = True
                    return True

            memo[word] = False
            return False

        res = []
        for word in words:
            word_set.remove(word)  # Dont match against what we are checking
            if canFormWord(word):
                res.append(word)
            word_set.add(word)  # Add the word back for next iteration

        return res
