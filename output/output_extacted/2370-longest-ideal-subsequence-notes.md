## Longest Ideal Subsequence
**Problem Link:** https://leetcode.com/problems/longest-ideal-subsequence/description

**Problem Statement:**
- Input format and constraints: Given a string `s` and an integer `k`, return the length of the longest ideal subsequence of `s`.
- Expected output format: The length of the longest ideal subsequence.
- Key requirements and edge cases to consider: 
    - An ideal subsequence is a subsequence where the difference between any two consecutive characters is at most `k`.
    - The input string `s` will only contain lowercase letters.
- Example test cases with explanations:
    - For `s = "acfgbd"`, `k = 2`, the longest ideal subsequence is `"acfgbd"` with length `6`.
    - For `s = "abcd"`, `k = 3`, the longest ideal subsequence is `"abcd"` with length `4`.

### Brute Force Approach

**Explanation:**
- Initial thought process: Check all possible subsequences of `s` and verify if they are ideal.
- Step-by-step breakdown of the solution:
    1. Generate all possible subsequences of `s`.
    2. For each subsequence, check if the difference between any two consecutive characters is at most `k`.
    3. If the subsequence is ideal, update the maximum length.
- Why this approach comes to mind first: It is a straightforward way to solve the problem, but it has a high time complexity due to generating all possible subsequences.

```cpp
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int longestIdealSubsequenceBrute(string s, int k) {
    int n = s.size();
    int maxLen = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        string sub = "";
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                sub += s[i];
            }
        }
        if (isIdeal(sub, k)) {
            maxLen = max(maxLen, (int)sub.size());
        }
    }
    return maxLen;
}

bool isIdeal(string s, int k) {
    for (int i = 1; i < s.size(); i++) {
        if (abs(s[i] - s[i-1]) > k) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string `s`. This is because we generate all possible subsequences of `s` and check each one.
> - **Space Complexity:** $O(n)$, as we need to store the current subsequence.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to generating all possible subsequences.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to keep track of the longest ideal subsequence ending at each position.
- Detailed breakdown of the approach:
    1. Initialize a dynamic programming table `dp` of size `n`, where `dp[i]` will store the length of the longest ideal subsequence ending at index `i`.
    2. For each position `i` in the string `s`, check all previous positions `j` such that the difference between `s[i]` and `s[j]` is at most `k`.
    3. Update `dp[i]` to be the maximum of its current value and `dp[j] + 1`.
- Proof of optimality: This approach is optimal because it considers all possible ideal subsequences and keeps track of the longest one ending at each position.

```cpp
int longestIdealSubsequenceOptimal(string s, int k) {
    int n = s.size();
    vector<int> dp(n, 1);
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (abs(s[i] - s[j]) <= k) {
                dp[i] = max(dp[i], dp[j] + 1);
            }
        }
    }
    return *max_element(dp.begin(), dp.end());
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of the string `s`. This is because we have two nested loops.
> - **Space Complexity:** $O(n)$, as we need to store the dynamic programming table `dp`.
> - **Optimality proof:** This approach is optimal because it considers all possible ideal subsequences and keeps track of the longest one ending at each position.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming and string manipulation.
- Problem-solving patterns identified: Using dynamic programming to keep track of the longest ideal subsequence ending at each position.
- Optimization techniques learned: Avoiding the generation of all possible subsequences and using dynamic programming instead.
- Similar problems to practice: Other problems involving dynamic programming and string manipulation.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the difference between characters correctly.
- Edge cases to watch for: Empty strings and strings with a single character.
- Performance pitfalls: Generating all possible subsequences instead of using dynamic programming.
- Testing considerations: Testing with different values of `k` and strings of varying lengths.