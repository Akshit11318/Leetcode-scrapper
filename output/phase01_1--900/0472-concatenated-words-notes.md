## Concatenated Words

**Problem Link:** https://leetcode.com/problems/concatenated-words/description

**Problem Statement:**
- Input: a list of non-empty strings `words`
- Constraints: $1 \leq \text{number of words} \leq 1000$, $1 \leq \text{length of each word} \leq 30$, $1 \leq \text{total length of all words} \leq 1000$
- Expected output: a list of all words in `words` that are concatenated words
- Key requirements and edge cases to consider:
  - A concatenated word is defined as a word that can be formed by concatenating the parts of two or more words in the given list.
  - Each part must be a non-empty string.
  - The same word should not be used more than once.
- Example test cases with explanations:
  - `words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatsdogcat"]`: The concatenated words are `["catsdogcats","dogcatsdog","ratcatsdogcat"]`.
  - `words = ["cat","dog","catdog"]`: The concatenated word is `["catdog"]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible combination of words to see if they can form a concatenated word.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of words.
  2. For each combination, concatenate the words and check if the result is in the original list of words.
  3. If it is, add it to the result list.
- Why this approach comes to mind first: It's a straightforward approach that checks all possibilities, but it's inefficient and has a high time complexity.

```cpp
class Solution {
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        unordered_set<string> dict(words.begin(), words.end());
        vector<string> result;
        
        for (const string& word : words) {
            vector<bool> dp(word.size() + 1, false);
            dp[0] = true;
            
            for (int i = 1; i <= word.size(); i++) {
                for (int j = 0; j < i; j++) {
                    if (dp[j] && dict.count(word.substr(j, i - j))) {
                        dp[i] = true;
                        break;
                    }
                }
            }
            
            if (dp[word.size()]) {
                result.push_back(word);
            }
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M^3)$, where $N$ is the number of words and $M$ is the maximum length of a word. This is because we're using a nested loop to generate all possible combinations of words.
> - **Space Complexity:** $O(N \cdot M)$, where $N$ is the number of words and $M$ is the maximum length of a word. This is because we're storing the result list and the dynamic programming table.
> - **Why these complexities occur:** The time complexity is high because we're generating all possible combinations of words, and the space complexity is moderate because we're storing the result list and the dynamic programming table.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store the intermediate results and avoid redundant computation.
- Detailed breakdown of the approach:
  1. Create a set of words for efficient lookup.
  2. For each word, use dynamic programming to check if it can be formed by concatenating other words in the set.
  3. If it can, add it to the result list.
- Proof of optimality: This approach has a time complexity of $O(N \cdot M^2)$, which is optimal because we need to check all possible combinations of words.

```cpp
class Solution {
public:
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        unordered_set<string> dict(words.begin(), words.end());
        vector<string> result;
        
        for (const string& word : words) {
            vector<bool> dp(word.size() + 1, false);
            dp[0] = true;
            
            for (int i = 1; i <= word.size(); i++) {
                for (int j = 0; j < i; j++) {
                    if (dp[j] && dict.count(word.substr(j, i - j))) {
                        dp[i] = true;
                        break;
                    }
                }
            }
            
            if (dp[word.size()]) {
                result.push_back(word);
            }
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M^2)$, where $N$ is the number of words and $M$ is the maximum length of a word. This is because we're using dynamic programming to store the intermediate results.
> - **Space Complexity:** $O(N \cdot M)$, where $N$ is the number of words and $M$ is the maximum length of a word. This is because we're storing the result list and the dynamic programming table.
> - **Optimality proof:** This approach is optimal because we need to check all possible combinations of words, and the dynamic programming approach avoids redundant computation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, set lookup, and string manipulation.
- Problem-solving patterns identified: Breaking down a problem into smaller sub-problems and using dynamic programming to store intermediate results.
- Optimization techniques learned: Using a set for efficient lookup and avoiding redundant computation using dynamic programming.
- Similar problems to practice: Word Break, Word Break II, and Concatenated Words II.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not using dynamic programming to avoid redundant computation, and not using a set for efficient lookup.
- Edge cases to watch for: Empty strings, single-character strings, and strings with repeated characters.
- Performance pitfalls: Using a brute force approach with a high time complexity, not using dynamic programming to store intermediate results, and not using a set for efficient lookup.
- Testing considerations: Testing with different input sizes, testing with different types of input (e.g., strings with repeated characters), and testing with edge cases.