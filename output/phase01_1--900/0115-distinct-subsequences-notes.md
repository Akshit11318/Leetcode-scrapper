## Distinct Subsequences
**Problem Link:** https://leetcode.com/problems/distinct-subsequences/description

**Problem Statement:**
- Input format: Two strings `s` and `t`, where `s` is the original string and `t` is the target string.
- Constraints: $1 \leq s.length, t.length \leq 85$.
- Expected output format: The number of distinct subsequences of `s` that are equal to `t`.
- Key requirements and edge cases to consider: 
    - Handling empty strings.
    - Considering the case where `t` is longer than `s`.
- Example test cases with explanations:
    - For `s = "rabbbit"` and `t = "rabbit"`, the output should be `3` because there are three different ways to form "rabbit" from "rabbbit" by removing characters.
    - For `s = "abc"` and `t = "abc"`, the output should be `1` because there is only one way to form "abc" from "abc" without removing any characters.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To generate all possible subsequences of `s` and check if they match `t`.
- Step-by-step breakdown of the solution:
    1. Generate all possible subsequences of `s`.
    2. For each subsequence, compare it with `t`.
    3. If a match is found, increment the count of distinct subsequences.
- Why this approach comes to mind first: It's straightforward to think of generating all possible subsequences and then filtering those that match `t`.

```cpp
int numDistinct(string s, string t) {
    int count = 0;
    int n = s.length();
    int m = t.length();
    
    // Function to generate all subsequences
    function<void(int, string)> generateSubsequences = 
        [&](int index, string sub) {
            if (index == n) {
                if (sub == t) {
                    count++;
                }
                return;
            }
            generateSubsequences(index + 1, sub);
            generateSubsequences(index + 1, sub + s[index]);
        };
    
    generateSubsequences(0, "");
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ because we are generating all possible subsequences of `s`, and there are $2^n$ possible subsequences for a string of length $n$.
> - **Space Complexity:** $O(n + m)$ due to the recursion stack and the space required to store the current subsequence being generated.
> - **Why these complexities occur:** The exponential time complexity comes from the recursive generation of all possible subsequences, and the space complexity is due to the maximum depth of the recursion tree and the storage needed for the subsequence strings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using dynamic programming to store and reuse the counts of subsequences that match the target string up to a certain point.
- Detailed breakdown of the approach:
    1. Create a 2D array `dp` where `dp[i][j]` represents the number of distinct subsequences of the first `i` characters of `s` that match the first `j` characters of `t`.
    2. Initialize `dp[0][0] = 1` because there is exactly one way to match an empty string with another empty string.
    3. For `i` from `1` to `n` and `j` from `1` to `m`, update `dp[i][j]` based on whether the current character in `s` matches the current character in `t`. If they match, add the number of distinct subsequences without considering the current character in `s` to `dp[i][j]`. Always consider the case where the current character in `s` is not used in the subsequence.
- Proof of optimality: This approach ensures that each subproblem is solved only once and stored for future reference, reducing the time complexity significantly.
- Why further optimization is impossible: The problem inherently requires considering all characters in both strings, and the dynamic programming approach optimally utilizes the information from previously computed subproblems.

```cpp
int numDistinct(string s, string t) {
    int n = s.length();
    int m = t.length();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    
    // Initialize base case
    for (int i = 0; i <= n; i++) {
        dp[i][0] = 1;
    }
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            // If current characters match, consider including the current character in s
            if (s[i - 1] == t[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
            } else {
                // If current characters do not match, do not include the current character in s
                dp[i][j] = dp[i - 1][j];
            }
        }
    }
    
    return dp[n][m];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ because we are filling up a 2D array of size $(n + 1) \times (m + 1)$.
> - **Space Complexity:** $O(n \cdot m)$ for storing the 2D `dp` array.
> - **Optimality proof:** This approach is optimal because it avoids redundant computation by storing and reusing the results of subproblems, leading to a polynomial time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming for solving problems with overlapping subproblems.
- Problem-solving patterns identified: Breaking down a problem into smaller subproblems and solving them only once to store and reuse their results.
- Optimization techniques learned: Avoiding redundant computation by using memoization or tabulation in dynamic programming.
- Similar problems to practice: Other dynamic programming problems like the *Longest Common Subsequence* or *Edit Distance* problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect initialization of the `dp` array or incorrect update logic for `dp[i][j]`.
- Edge cases to watch for: Handling empty strings or strings of different lengths.
- Performance pitfalls: Failing to utilize dynamic programming, leading to exponential time complexity.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases like empty strings or strings with repeating characters.