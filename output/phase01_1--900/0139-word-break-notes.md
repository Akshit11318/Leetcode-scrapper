## Word Break
**Problem Link:** https://leetcode.com/problems/word-break/description

**Problem Statement:**
- Input format: A string `s` and a list of strings `wordDict`.
- Constraints: `1 <= s.length <= 300`, `1 <= wordDict.length <= 100`, `1 <= wordDict[i].length <= 20`, `s` and `wordDict[i]` consist of lowercase English letters.
- Expected output format: `true` if `s` can be segmented into words from `wordDict`, `false` otherwise.
- Key requirements: Determine if the input string `s` can be segmented into words from the given dictionary `wordDict`.
- Example test cases:
  - Input: `s = "leetcode", wordDict = ["leet","code"]`, Output: `true`
  - Input: `s = "applepenapple", wordDict = ["apple","pen"]`, Output: `true`
  - Input: `s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]`, Output: `false`

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible substring of `s` to see if it can be formed from words in `wordDict`.
- This approach comes to mind first because it directly addresses the requirement of segmenting `s` into words from `wordDict`.
- However, it's inefficient because it involves a lot of repeated work and does not utilize the structure of the problem efficiently.

```cpp
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<string> dict = wordDict;
        return helper(s, dict);
    }
    
    bool helper(string s, vector<string>& dict) {
        if (s.empty()) return true;
        for (int i = 1; i <= s.length(); ++i) {
            string substr = s.substr(0, i);
            if (find(dict.begin(), dict.end(), substr) != dict.end()) {
                if (helper(s.substr(i), dict)) return true;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ where $n$ is the length of `s`, because in the worst case, we are potentially checking every substring of `s`.
> - **Space Complexity:** $O(n)$ for the recursion stack.
> - **Why these complexities occur:** The brute force approach checks every possible segmentation of `s`, leading to exponential time complexity. The space complexity is due to the recursive call stack.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is using dynamic programming to store and reuse the results of subproblems.
- We create a boolean array `dp` where `dp[i]` is `true` if the substring `s[0...i]` can be segmented into words from `wordDict`.
- This approach is optimal because it avoids the repeated work of the brute force approach by storing the results of subproblems.

```cpp
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        vector<bool> dp(s.length() + 1, false);
        dp[0] = true;
        
        for (int i = 1; i <= s.length(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (dp[j] && dict.find(s.substr(j, i - j)) != dict.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        
        return dp[s.length()];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of `s`, because we are checking every substring of `s` once.
> - **Space Complexity:** $O(n + m)$ where $n$ is the length of `s` and $m` is the total length of all words in `wordDict`, for storing the `dp` array and the set of words.
> - **Optimality proof:** This is the best possible complexity because we must at least read the input, and the dynamic programming approach ensures we do not repeat work, making it optimal for this problem.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming in solving problems with overlapping subproblems.
- How to apply dynamic programming to string segmentation problems.
- The trade-off between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Not considering the exponential time complexity of brute force approaches.
- Failing to utilize dynamic programming to avoid repeated work.
- Not validating the input and edge cases properly.

By following the optimal approach, we can efficiently solve the Word Break problem with a significant reduction in time complexity compared to the brute force method.