## Strange Printer

**Problem Link:** [https://leetcode.com/problems/strange-printer/description](https://leetcode.com/problems/strange-printer/description)

**Problem Statement:**
- Input: A string `s` containing only lowercase letters.
- Output: The minimum number of turns required to print the string.
- Key requirements and edge cases to consider: The printer can print a character in a single turn if the previous character is the same. Otherwise, it requires two turns.
- Example test cases with explanations:
  - Input: `"aaabbb"` Output: `2`
  - Input: `"aba"` Output: `2`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The problem seems to require a recursive approach where we try to divide the string into smaller parts and solve each part separately.
- Step-by-step breakdown of the solution: We start by trying to divide the string at each possible position and recursively find the minimum number of turns required for the left and right parts.
- Why this approach comes to mind first: This approach is intuitive because it breaks down the problem into smaller sub-problems and tries to solve each sub-problem independently.

```cpp
class Solution {
public:
    int strangePrinter(string s) {
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        for (int i = n - 1; i >= 0; i--) {
            dp[i][i] = 1;
            for (int j = i + 1; j < n; j++) {
                dp[i][j] = dp[i + 1][j] + 1;
                for (int k = i + 1; k <= j; k++) {
                    if (s[i] == s[k]) {
                        dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + dp[k][j]);
                    }
                }
            }
        }
        
        return dp[0][n - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string. This is because we have a nested loop structure with three layers, each of which iterates over the string.
> - **Space Complexity:** $O(n^2)$, where $n$ is the length of the string. This is because we use a 2D array to store the dynamic programming state.
> - **Why these complexities occur:** The time complexity is cubic because we have a nested loop structure, and the space complexity is quadratic because we use a 2D array to store the dynamic programming state.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved using dynamic programming with a 2D array to store the minimum number of turns required for each sub-string.
- Detailed breakdown of the approach: We start by initializing the 2D array with base cases, and then fill in the rest of the array using a bottom-up approach.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible divisions of the string and find the minimum number of turns required.
- Why further optimization is impossible: The dynamic programming approach has a time complexity of $O(n^3)$, which is optimal for this problem because we need to consider all possible divisions of the string.

```cpp
class Solution {
public:
    int strangePrinter(string s) {
        int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n, 0));
        
        for (int i = n - 1; i >= 0; i--) {
            dp[i][i] = 1;
            for (int j = i + 1; j < n; j++) {
                dp[i][j] = dp[i + 1][j] + 1;
                for (int k = i + 1; k <= j; k++) {
                    if (s[i] == s[k]) {
                        dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + dp[k][j]);
                    }
                }
            }
        }
        
        return dp[0][n - 1];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string. This is because we have a nested loop structure with three layers, each of which iterates over the string.
> - **Space Complexity:** $O(n^2)$, where $n$ is the length of the string. This is because we use a 2D array to store the dynamic programming state.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible divisions of the string and find the minimum number of turns required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursion, and memoization.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and solving each sub-problem independently.
- Optimization techniques learned: Using dynamic programming to avoid redundant computation and improve performance.
- Similar problems to practice: Other dynamic programming problems, such as the Fibonacci sequence and the knapsack problem.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the dynamic programming array correctly, not considering all possible divisions of the string, and not using memoization to avoid redundant computation.
- Edge cases to watch for: Empty strings, strings with a single character, and strings with duplicate characters.
- Performance pitfalls: Not using dynamic programming, not using memoization, and not considering all possible divisions of the string.
- Testing considerations: Testing the function with different input strings, including empty strings, strings with a single character, and strings with duplicate characters.