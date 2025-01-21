## Number of Ways to Form a Target String Given a Dictionary

**Problem Link:** https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/description

**Problem Statement:**
- Input: A string `target` and a list of strings `words`.
- Constraints: `1 <= target.length <= 10`, `1 <= words.length <= 6`, `1 <= words[i].length <= 10`, `target` and `words[i]` consist of lowercase English letters.
- Expected output: The number of ways to form the `target` string using the strings in `words`.
- Key requirements and edge cases: Each string in `words` can be used any number of times to form the `target` string. The order of characters in the `target` string must be maintained.
- Example test cases:
  - `target = "acbags", words = ["bag","cab","bag"]`, the output should be `3`.
  - `target = "abcd", words = ["abcd"]`, the output should be `1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible combinations of strings from `words` and check if any combination forms the `target` string.
- This approach involves recursively trying to form the `target` string by appending strings from `words` to the current combination.
- Why this approach comes to mind first: It's a straightforward way to explore all possibilities, but it's inefficient due to its high time complexity.

```cpp
class Solution {
public:
    int numWays(vector<string>& words, string target) {
        int result = 0;
        vector<string> current;
        numWaysHelper(words, target, 0, current, result);
        return result;
    }
    
    void numWaysHelper(vector<string>& words, string target, int index, vector<string>& current, int& result) {
        if (index == target.size()) {
            result++;
            return;
        }
        
        for (const auto& word : words) {
            if (index + word.size() <= target.size()) {
                bool match = true;
                for (int i = 0; i < word.size(); i++) {
                    if (word[i] != target[index + i]) {
                        match = false;
                        break;
                    }
                }
                if (match) {
                    current.push_back(word);
                    numWaysHelper(words, target, index + word.size(), current, result);
                    current.pop_back();
                }
            }
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{10} \cdot 6^{10})$, where $10$ is the maximum length of the `target` string and $6$ is the maximum number of words. This is because in the worst case, we might have to try all possible combinations of words to form the `target` string.
> - **Space Complexity:** $O(10)$, for the recursion stack and the `current` vector.
> - **Why these complexities occur:** The high time complexity occurs due to the recursive nature of the brute force approach, where we try all possible combinations of words. The space complexity is relatively low because we only need to store the current combination of words and the recursion stack.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use dynamic programming to store the number of ways to form each prefix of the `target` string.
- We can use a `dp` array where `dp[i]` represents the number of ways to form the first `i` characters of the `target` string.
- We iterate over each character in the `target` string and for each character, we iterate over each word in `words`. If the word matches the remaining characters in the `target` string, we update `dp[i]` accordingly.

```cpp
class Solution {
public:
    int numWays(vector<string>& words, string target) {
        int n = target.size();
        vector<int> dp(n + 1, 0);
        dp[0] = 1;
        
        for (int i = 1; i <= n; i++) {
            for (const auto& word : words) {
                if (i >= word.size()) {
                    bool match = true;
                    for (int j = 0; j < word.size(); j++) {
                        if (word[word.size() - 1 - j] != target[i - 1 - j]) {
                            match = false;
                            break;
                        }
                    }
                    if (match) {
                        dp[i] += dp[i - word.size()];
                    }
                }
            }
        }
        
        return dp[n];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the length of the `target` string, $m$ is the number of words, and $k$ is the maximum length of a word.
> - **Space Complexity:** $O(n)$, for the `dp` array.
> - **Optimality proof:** This is the optimal solution because we only need to iterate over each character in the `target` string and each word in `words` once. We also store the number of ways to form each prefix of the `target` string, which allows us to avoid redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, string matching.
- Problem-solving patterns identified: Using dynamic programming to store the number of ways to form each prefix of the `target` string.
- Optimization techniques learned: Avoiding redundant calculations by storing intermediate results.
- Similar problems to practice: Problems involving dynamic programming and string matching.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly, not initializing variables correctly.
- Edge cases to watch for: Empty `target` string, empty `words` list.
- Performance pitfalls: Using a brute force approach, not using dynamic programming to store intermediate results.
- Testing considerations: Testing with different inputs, including edge cases.