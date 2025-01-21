## Decode Ways II
**Problem Link:** https://leetcode.com/problems/decode-ways-ii/description

**Problem Statement:**
- Input: A string `s` containing digits.
- Constraints: `1 <= s.length <= 5 * 10^4`, `s[i]` is a digit from 0 to 9.
- Expected Output: The number of ways to decode the string `s` modulo `10^9 + 7`.
- Key Requirements: A digit is considered valid if it is greater than 0. Two digits are considered valid if the first digit is 1 or 2, and the second digit is less than or equal to 6 if the first digit is 2.
- Example Test Cases:
  - Input: `s = "12"` Output: `2`
  - Input: `s = "226"` Output: `3`
  - Input: `s = "0"` Output: `0`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible combinations of valid digits and count them.
- However, this approach quickly becomes impractical due to the large number of possible combinations.

```cpp
int numDecodings(string s) {
    int mod = 1e9 + 7;
    int count = 0;
    function<void(int)> dfs = [&](int idx) {
        if (idx == s.size()) {
            count++;
            return;
        }
        if (s[idx] != '0') {
            dfs(idx + 1);
        }
        if (idx + 1 < s.size() && (s[idx] == '1' || (s[idx] == '2' && s[idx + 1] <= '6'))) {
            dfs(idx + 2);
        }
    };
    dfs(0);
    return count % mod;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$ where $n$ is the length of the string `s`. This is because in the worst case, we are making two recursive calls for each character in the string.
> - **Space Complexity:** $O(n)$ due to the recursion stack.
> - **Why these complexities occur:** The recursive nature of the solution and the fact that we are exploring all possible combinations lead to these complexities.

---

### Optimal Approach (Required)
**Explanation:**
- We can use dynamic programming to optimize the solution. The idea is to maintain two arrays, `dp1` and `dp2`, where `dp1[i]` represents the number of ways to decode the string up to index `i` using a single digit, and `dp2[i]` represents the number of ways to decode the string up to index `i` using two digits.
- We can then use these arrays to calculate the number of ways to decode the entire string.

```cpp
int numDecodings(string s) {
    int mod = 1e9 + 7;
    int n = s.size();
    long long dp[n + 1];
    dp[0] = 1;
    if (s[0] != '0') dp[1] = 1;
    for (int i = 2; i <= n; i++) {
        if (s[i - 1] != '0') dp[i] = (dp[i] + dp[i - 1]) % mod;
        if (s[i - 2] == '1' || (s[i - 2] == '2' && s[i - 1] <= '6')) {
            dp[i] = (dp[i] + dp[i - 2]) % mod;
        }
    }
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string `s`. This is because we are making a single pass through the string.
> - **Space Complexity:** $O(n)$ due to the `dp` array.
> - **Optimality proof:** This solution is optimal because it uses dynamic programming to avoid redundant calculations and has a linear time complexity.

---

### Final Notes

**Learning Points:**
- The importance of dynamic programming in solving problems with overlapping subproblems.
- How to use dynamic programming to optimize a recursive solution.
- The concept of modulo arithmetic and its application in avoiding integer overflow.

**Mistakes to Avoid:**
- Not considering the base cases properly.
- Not using modulo arithmetic to avoid integer overflow.
- Not optimizing the solution using dynamic programming.

---