## Number of Good Binary Strings
**Problem Link:** https://leetcode.com/problems/number-of-good-binary-strings/description

**Problem Statement:**
- Given an integer `n`, return the number of good binary strings of length `n`. A good binary string is a string consisting of the characters `0` and `1` where no two consecutive characters are `1`.
- Input format and constraints: `n` is an integer between 1 and 10^6 (inclusive).
- Expected output format: The number of good binary strings of length `n`.
- Key requirements and edge cases to consider: The string must consist only of `0` and `1`, and no two consecutive characters can be `1`.

### Brute Force Approach
**Explanation:**
- Initial thought process: To generate all possible binary strings of length `n` and count the ones that meet the condition.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for good strings.
  2. Generate all possible binary strings of length `n`.
  3. For each generated string, check if any two consecutive characters are `1`.
  4. If not, increment the counter.
- Why this approach comes to mind first: It directly addresses the problem by checking every possible scenario.

```cpp
int countGoodStrings(int n) {
    // Initialize count of good strings
    int count = 0;
    // Generate all possible binary strings of length n
    for (int i = 0; i < (1 << n); i++) {
        string str;
        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) {
                str += '1';
            } else {
                str += '0';
            }
        }
        // Check if the string is good
        bool isGood = true;
        for (int k = 0; k < n - 1; k++) {
            if (str[k] == '1' && str[k + 1] == '1') {
                isGood = false;
                break;
            }
        }
        // If the string is good, increment the count
        if (isGood) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the string. This is because we generate all possible binary strings of length $n$ ($2^n$) and for each string, we check if it's good, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, as we need to store each generated string of length $n$.
> - **Why these complexities occur:** The brute force approach involves generating an exponential number of strings and then checking each one, leading to high time complexity.

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: This problem can be solved using dynamic programming. The idea is to build up a solution by considering how a string of length `n` can be formed from strings of length `n-1` and `n-2`.
- Detailed breakdown of the approach:
  1. Initialize a dynamic programming table `dp` where `dp[i]` represents the number of good binary strings of length `i`.
  2. The base cases are `dp[1] = 2` (since there are two good strings of length 1: "0" and "1") and `dp[2] = 3` (since there are three good strings of length 2: "00", "01", and "10").
  3. For `i > 2`, a good binary string of length `i` can be formed by appending "0" to any good string of length `i-1` or by appending "01" to any good string of length `i-2`. Thus, `dp[i] = dp[i-1] + dp[i-2]`.
- Proof of optimality: This dynamic programming approach ensures that each good binary string of length `n` is counted exactly once, and it does so in linear time relative to `n`, making it optimal.

```cpp
int countGoodStrings(int n) {
    if (n == 1) return 2;
    if (n == 2) return 3;
    vector<int> dp(n + 1);
    dp[1] = 2;
    dp[2] = 3;
    for (int i = 3; i <= n; i++) {
        dp[i] = dp[i-1] + dp[i-2];
    }
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, as we fill up the `dp` table iteratively.
> - **Space Complexity:** $O(n)$, for storing the `dp` table.
> - **Optimality proof:** The dynamic programming approach ensures a linear time complexity, which is optimal for this problem since we must at least consider each length up to `n` once.

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming for solving problems with overlapping subproblems.
- Problem-solving patterns identified: Breaking down a problem into smaller subproblems and solving them only once.
- Optimization techniques learned: Using dynamic programming to reduce exponential time complexity to linear.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect base cases or transition formulas in dynamic programming.
- Edge cases to watch for: Handling the cases when `n` is 1 or 2 separately.
- Performance pitfalls: Not using dynamic programming for problems with overlapping subproblems, leading to exponential time complexity.