## Edit Distance

**Problem Link:** https://leetcode.com/problems/edit-distance/description

**Problem Statement:**
- Input format: Two strings `word1` and `word2`.
- Constraints: `1 <= word1.length, word2.length <= 500`.
- Expected output format: The minimum number of operations (insertions, deletions, and substitutions) required to change `word1` into `word2`.
- Key requirements and edge cases to consider:
  - Handling empty strings.
  - Considering all possible operations (insertions, deletions, substitutions) to find the minimum.
- Example test cases with explanations:
  - `word1 = "horse"`, `word2 = "ros"`, Output: `3` (delete "h", delete "o", delete "e").
  - `word1 = "intention"`, `word2 = "execution"`, Output: `5` (replace "i" with "e", replace "n" with "x", replace "n" with "x", delete "t", delete "i").

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of operations (insertions, deletions, substitutions) and find the minimum number of operations required to change `word1` into `word2`.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of operations.
  2. For each combination, apply the operations to `word1` and check if the result is equal to `word2`.
  3. Keep track of the minimum number of operations required.
- Why this approach comes to mind first: It's a straightforward approach that considers all possible solutions.

```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        return dfs(word1, word2, m - 1, n - 1);
    }

    int dfs(string& word1, string& word2, int i, int j) {
        if (i < 0) return j + 1; // insert all characters of word2
        if (j < 0) return i + 1; // delete all characters of word1
        if (word1[i] == word2[j]) return dfs(word1, word2, i - 1, j - 1);
        return 1 + min(min(dfs(word1, word2, i - 1, j), dfs(word1, word2, i, j - 1)), dfs(word1, word2, i - 1, j - 1));
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(3^{m+n})$, where $m$ and $n$ are the lengths of `word1` and `word2`, respectively. This is because in the worst case, we have three choices (insert, delete, substitute) for each character in both strings.
> - **Space Complexity:** $O(m+n)$, due to the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of operations, resulting in exponential time complexity. The recursive call stack contributes to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use dynamic programming to store the results of subproblems and avoid redundant calculations.
- Detailed breakdown of the approach:
  1. Create a 2D array `dp` of size $(m+1) \times (n+1)$, where `dp[i][j]` represents the minimum number of operations required to change the first `i` characters of `word1` into the first `j` characters of `word2`.
  2. Initialize the base cases: `dp[0][j] = j` (insert all characters of `word2`) and `dp[i][0] = i` (delete all characters of `word1`).
  3. Fill in the rest of the `dp` array using the recurrence relation: `dp[i][j] = min(dp[i-1][j-1] + (word1[i-1] != word2[j-1]), dp[i-1][j] + 1, dp[i][j-1] + 1)`.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible operations and find the minimum number of operations required.

```cpp
class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size(), n = word2.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= n; j++) {
                if (i == 0) dp[i][j] = j;
                else if (j == 0) dp[i][j] = i;
                else if (word1[i-1] == word2[j-1]) dp[i][j] = dp[i-1][j-1];
                else dp[i][j] = 1 + min(min(dp[i-1][j], dp[i][j-1]), dp[i-1][j-1]);
            }
        }
        return dp[m][n];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(mn)$, where $m$ and $n$ are the lengths of `word1` and `word2`, respectively. This is because we fill in the `dp` array once.
> - **Space Complexity:** $O(mn)$, due to the `dp` array.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible operations and find the minimum number of operations required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, memoization.
- Problem-solving patterns identified: Breaking down the problem into smaller subproblems, using a 2D array to store the results of subproblems.
- Optimization techniques learned: Using dynamic programming to avoid redundant calculations.
- Similar problems to practice: Longest common subsequence, shortest common supersequence.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the base cases correctly, not filling in the `dp` array correctly.
- Edge cases to watch for: Empty strings, strings of different lengths.
- Performance pitfalls: Using a brute force approach, not using memoization.
- Testing considerations: Test the function with different input strings, including edge cases.