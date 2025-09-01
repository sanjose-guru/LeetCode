# [322. Coin Change](https://leetcode.com/problems/coin-change/description/)

Given an array of strings <code>words</code> (**without duplicates** ), return
all the **concatenated words** in the given list of <code>words</code>.

A **concatenated word** is defined as a string that is comprised entirely of at
least two shorter words (not necessarily distinct)in the given array.

**Example 1:**

````
Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
"dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".```

**Example 2:**

````

Input: words = ["cat","dog","catdog"] Output: ["catdog"]

```

**Constraints:**

- <code>1 <= words.length <= 10^4</code>
- <code>1 <= words[i].length <= 30</code>
- <code>words[i]</code> consists of only lowercase English letters.
- All the strings of <code>words</code> are **unique** .
- <code>1 <= sum(words[i].length) <= 10^5</code>
```
