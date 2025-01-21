## Decode Ways

**Problem Link:** https://leetcode.com/problems/decode-ways/description

**Problem Statement:**
- Input: a string of digits
- Constraints: `1 <= s.length <= 100`
- Expected output: the number of ways to decode the string
- Key requirements: consider each digit or pair of digits as a potential character in the decoded string
- Edge cases: empty string, strings starting with 0, strings with invalid pairs (e.g., 30-39, 80-89)
- Example test cases:
  - Input: `"12"`; Output: `2` (`"ab"` or `"l"`)
  - Input: `"226"`; Output: `3` (`"baa"`, `"ba"`, or `"bb"`)

---

### Brute Force Approach

**Explanation:**
- Initial thought process: try all possible combinations of single and double digits
- Step-by-step breakdown:
  1. Initialize a counter for the number of ways to decode
  2. Define a recursive function to explore all possible combinations
  3. In the recursive function, try decoding the current character or the current character and the next one
  4. If the decoding is valid, recursively call the function with the remaining string
  5. If the decoding is not valid, return 0
- Why this approach comes to mind first: it's a straightforward way to explore all possibilities

```cpp
class Solution {
public:
    int numDecodings(string s) {
        if (s.empty() || s[0] == '0') return 0;
        return helper(s, 0);
    }
    
    int helper(string& s, int index) {
        if (index == s.length()) return 1;
        int res = 0;
        // Try decoding one character
        if (s[index] != '0') {
            res += helper(s, index + 1);
        }
        // Try decoding two characters
        if (index + 1 < s.length() && (s[index] == '1' || (s[index] == '2' && s[index + 1] <= '6'))) {
            res += helper(s, index + 2);
        }
        return res;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the string, because in the worst case, we try all possible combinations
> - **Space Complexity:** $O(n)$, because of the recursive call stack
> - **Why these complexities occur:** the recursive function tries all possible combinations, leading to exponential time complexity

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: use dynamic programming to store the number of ways to decode the string up to each position
- Detailed breakdown:
  1. Initialize a DP array with the same length as the input string
  2. Set the base case: if the string is empty or starts with '0', return 0
  3. Fill the DP array: for each position, try decoding one character and two characters, and store the sum of the results
- Proof of optimality: this approach avoids redundant calculations and has a linear time complexity

```cpp
class Solution {
public:
    int numDecodings(string s) {
        if (s.empty() || s[0] == '0') return 0;
        int n = s.length();
        vector<int> dp(n + 1);
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            // Try decoding one character
            if (s[i - 1] != '0') {
                dp[i] += dp[i - 1];
            }
            // Try decoding two characters
            if (s[i - 2] == '1' || (s[i - 2] == '2' && s[i - 1] <= '6')) {
                dp[i] += dp[i - 2];
            }
        }
        return dp[n];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string
> - **Space Complexity:** $O(n)$, because of the DP array
> - **Optimality proof:** this approach avoids redundant calculations and has a linear time complexity, making it the most efficient solution

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, recursion
- Problem-solving patterns identified: avoiding redundant calculations, using base cases
- Optimization techniques learned: using DP to store intermediate results
- Similar problems to practice: `Climbing Stairs`, `Fibonacci Number`

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle edge cases, not initializing DP arrays correctly
- Edge cases to watch for: empty strings, strings starting with '0', strings with invalid pairs
- Performance pitfalls: using recursive functions without memoization, not using DP to store intermediate results
- Testing considerations: test with different input lengths, test with different input values (e.g., '0', '1', '2', etc.)