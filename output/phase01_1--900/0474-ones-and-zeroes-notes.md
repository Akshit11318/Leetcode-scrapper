## Ones and Zeroes
**Problem Link:** https://leetcode.com/problems/ones-and-zeroes/description

**Problem Statement:**
- Input format: `vector<string> strs`, `int m`, `int n`
- Constraints: `1 <= strs.length <= 600`, `1 <= strs[i].length <= 100`, `1 <= m, n <= 6`
- Expected output format: The maximum number of strings that can be formed with `m` `1`s and `n` `0`s.
- Key requirements: Count the number of `1`s and `0`s in each string and find the optimal combination of strings that can be formed with the given constraints.
- Example test cases:
  - Input: `strs = ["10","0001","111001","1","0"]`, `m = 5`, `n = 3`
  - Output: `4`
  - Explanation: We can form `4` strings with the given constraints: `"10"`, `"0001"`, `"1"`, `"0"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible combinations of strings and check if the total number of `1`s and `0`s exceeds the given constraints.
- Step-by-step breakdown:
  1. Initialize a counter for the maximum number of strings that can be formed.
  2. Generate all possible combinations of strings using recursion or bit manipulation.
  3. For each combination, count the total number of `1`s and `0`s.
  4. If the total number of `1`s and `0`s does not exceed the given constraints, update the counter.

```cpp
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int maxCount = 0;
        int len = strs.size();
        for (int mask = 0; mask < (1 << len); mask++) {
            int ones = 0, zeros = 0;
            for (int i = 0; i < len; i++) {
                if ((mask & (1 << i)) != 0) {
                    for (char c : strs[i]) {
                        if (c == '1') ones++;
                        else zeros++;
                    }
                }
            }
            if (ones <= m && zeros <= n) {
                maxCount = max(maxCount, __builtin_popcount(mask));
            }
        }
        return maxCount;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n \cdot m)$, where $n$ is the number of strings and $m$ is the maximum length of a string.
> - **Space Complexity:** $O(1)$, excluding the input and output.
> - **Why these complexities occur:** The brute force approach generates all possible combinations of strings, which results in an exponential time complexity. The space complexity is constant because we only use a fixed amount of space to store the counter and the current combination.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use dynamic programming to store the maximum number of strings that can be formed for each possible number of `1`s and `0`s.
- Detailed breakdown:
  1. Initialize a 3D array `dp` of size `(len + 1) x (m + 1) x (n + 1)` to store the maximum number of strings that can be formed.
  2. Iterate over each string and update the `dp` array accordingly.
  3. Finally, return the value stored in `dp[len][m][n]`.

```cpp
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));
        for (string str : strs) {
            int ones = 0, zeros = 0;
            for (char c : str) {
                if (c == '1') ones++;
                else zeros++;
            }
            for (int i = m; i >= ones; i--) {
                for (int j = n; j >= zeros; j--) {
                    dp[i][j] = max(dp[i][j], dp[i - ones][j - zeros] + 1);
                }
            }
        }
        return dp[m][n];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot len)$, where $n$ is the number of strings, $m$ is the maximum number of `1`s, and $len$ is the maximum length of a string.
> - **Space Complexity:** $O(m \cdot n)$, excluding the input and output.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible combinations of strings and store the maximum number of strings that can be formed for each possible number of `1`s and `0`s.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Dynamic programming, bit manipulation, recursion.
- Problem-solving patterns: Counting, combinatorics, optimization.
- Optimization techniques: Memoization, dynamic programming.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect indexing, out-of-bounds access, incorrect initialization.
- Edge cases to watch for: Empty input, invalid input, boundary cases.
- Performance pitfalls: Exponential time complexity, high memory usage.
- Testing considerations: Test with different input sizes, test with edge cases, test with invalid input.