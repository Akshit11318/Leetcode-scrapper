## Find the Maximum Length of Valid Subsequence II
**Problem Link:** https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/description

**Problem Statement:**
- Input format: You are given a binary string `s` and two integers `min0` and `max1`.
- Constraints: `1 <= s.length <= 1000`, `0 <= min0 <= max1 <= 1000`, and `min0 <= number of zeros in s` and `max1 >= number of ones in s`.
- Expected output format: The maximum length of a valid subsequence.
- Key requirements and edge cases to consider: A subsequence is valid if the number of zeros in the subsequence is at least `min0` and the number of ones in the subsequence is at most `max1`.
- Example test cases with explanations:
    - If `s = "10101"`, `min0 = 1`, and `max1 = 3`, the maximum length of a valid subsequence is `5` because the entire string satisfies the conditions.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible subsequences of `s`, count the number of zeros and ones in each subsequence, and check if it satisfies the conditions.
- Step-by-step breakdown of the solution:
    1. Generate all possible subsequences of `s`.
    2. For each subsequence, count the number of zeros and ones.
    3. Check if the number of zeros is at least `min0` and the number of ones is at most `max1`.
    4. If the conditions are satisfied, update the maximum length of a valid subsequence.

```cpp
#include <iostream>
#include <string>
#include <vector>

int findMaxForm(std::string s, int min0, int max1) {
    int n = s.size();
    int maxLen = 0;
    
    // Generate all possible subsequences
    for (int mask = 0; mask < (1 << n); mask++) {
        int zeros = 0, ones = 0;
        std::string subseq = "";
        
        // Count the number of zeros and ones in the subsequence
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subseq += s[i];
                if (s[i] == '0') zeros++;
                else ones++;
            }
        }
        
        // Check if the subsequence satisfies the conditions
        if (zeros >= min0 && ones <= max1) {
            maxLen = std::max(maxLen, (int)subseq.size());
        }
    }
    
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string `s`. This is because we generate all possible subsequences and for each subsequence, we count the number of zeros and ones.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we store the subsequence in a string.
> - **Why these complexities occur:** The brute force approach has high time complexity because we generate all possible subsequences, which is exponential in the length of the string. The space complexity is linear because we store the subsequence in a string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to solve this problem. We can define a 3D DP array `dp` where `dp[i][j][k]` represents the maximum length of a valid subsequence ending at index `i` with `j` zeros and `k` ones.
- Detailed breakdown of the approach:
    1. Initialize the DP array with zeros.
    2. For each index `i`, we have two options: include the current character in the subsequence or not.
    3. If we include the current character, we update the DP array accordingly.
    4. If we don't include the current character, we simply copy the value from the previous index.
    5. Finally, we return the maximum value in the DP array.

```cpp
#include <iostream>
#include <string>
#include <vector>

int findMaxForm(std::string s, int min0, int max1) {
    int n = s.size();
    int maxLen = 0;
    std::vector<std::vector<std::vector<int>>> dp(n + 1, std::vector<std::vector<int>>(min0 + 1, std::vector<int>(max1 + 1, 0)));
    
    // Initialize the DP array
    for (int i = 0; i <= n; i++) {
        for (int j = 0; j <= min0; j++) {
            for (int k = 0; k <= max1; k++) {
                if (i == 0) {
                    dp[i][j][k] = 0;
                } else {
                    if (s[i - 1] == '0') {
                        if (j > 0) {
                            dp[i][j][k] = std::max(dp[i][j][k], dp[i - 1][j - 1][k] + 1);
                        }
                        dp[i][j][k] = std::max(dp[i][j][k], dp[i - 1][j][k]);
                    } else {
                        if (k > 0) {
                            dp[i][j][k] = std::max(dp[i][j][k], dp[i - 1][j][k - 1] + 1);
                        }
                        dp[i][j][k] = std::max(dp[i][j][k], dp[i - 1][j][k]);
                    }
                }
            }
        }
    }
    
    // Return the maximum value in the DP array
    for (int i = 0; i <= n; i++) {
        for (int j = min0; j <= min0; j++) {
            for (int k = 0; k <= max1; k++) {
                maxLen = std::max(maxLen, dp[i][j][k]);
            }
        }
    }
    
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot min0 \cdot max1)$, where $n$ is the length of the string `s`. This is because we fill up the DP array.
> - **Space Complexity:** $O(n \cdot min0 \cdot max1)$, where $n` is the length of the string `s`. This is because we store the DP array.
> - **Optimality proof:** This solution is optimal because we consider all possible subsequences and count the number of zeros and ones in each subsequence. The DP array helps us to avoid redundant computation and store the maximum length of a valid subsequence ending at each index.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, bit manipulation.
- Problem-solving patterns identified: Counting, optimization.
- Optimization techniques learned: Memoization, tabulation.
- Similar problems to practice: Longest increasing subsequence, edit distance.

**Mistakes to Avoid:**
- Common implementation errors: Out-of-bounds access, incorrect initialization.
- Edge cases to watch for: Empty string, `min0` or `max1` is zero.
- Performance pitfalls: High time complexity, excessive memory usage.
- Testing considerations: Test with different inputs, edge cases, and boundary values.