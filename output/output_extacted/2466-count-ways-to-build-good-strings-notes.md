## Count Ways to Build Good Strings
**Problem Link:** https://leetcode.com/problems/count-ways-to-build-good-strings/description

**Problem Statement:**
- Input: Two integers `low` and `high`, and two strings `s1` and `s2`.
- Constraints: `1 <= low <= high <= 10^5`, `1 <= s1.length, s2.length <= 2`.
- Expected Output: The number of strings of length `n` that can be built using `s1` and `s2`, where `low <= n <= high`.
- Key Requirements:
  - A good string is one that can be formed by concatenating `s1` and `s2`.
  - The length of the good string should be between `low` and `high` (inclusive).
- Example Test Cases:
  - Input: `low = 3`, `high = 3`, `s1 = "aab"`, `s2 = "bbb"`. Output: `1`.
  - Input: `low = 2`, `high = 5`, `s1 = "a"`, `s2 = "a"`. Output: `4`.

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible strings of lengths between `low` and `high` by concatenating `s1` and `s2`, and then count the number of good strings.
- Step-by-step breakdown:
  1. Generate all possible combinations of `s1` and `s2` to form strings of lengths between `low` and `high`.
  2. Check each generated string to see if it can be formed by concatenating `s1` and `s2`.
  3. Count the number of good strings.

```cpp
int countGoodStrings(int low, int high, string s1, string s2) {
    int count = 0;
    for (int i = low; i <= high; i++) {
        for (int j = 0; j <= i / s1.length(); j++) {
            for (int k = 0; k <= i / s2.length(); k++) {
                if (j * s1.length() + k * s2.length() == i) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the string.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Why these complexities occur:** The time complexity is due to the three nested loops, and the space complexity is due to the fact that we only use a constant amount of space to store the count.

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to use dynamic programming to store the number of ways to form strings of each length.
- Detailed breakdown of the approach:
  1. Initialize a dynamic programming array `dp` of size `high + 1`, where `dp[i]` stores the number of ways to form a string of length `i`.
  2. Set `dp[0] = 1`, as there is one way to form an empty string.
  3. For each length `i` from `1` to `high`, calculate `dp[i]` by considering all possible ways to form a string of length `i` by concatenating `s1` and `s2`.
  4. Finally, calculate the total number of ways to form strings of lengths between `low` and `high` by summing up the values in the `dp` array.

```cpp
int countGoodStrings(int low, int high, string s1, string s2) {
    int dp[high + 1] = {0};
    dp[0] = 1;
    for (int i = 1; i <= high; i++) {
        if (i >= s1.length()) dp[i] += dp[i - s1.length()];
        if (i >= s2.length()) dp[i] += dp[i - s2.length()];
    }
    int count = 0;
    for (int i = low; i <= high; i++) {
        count += dp[i];
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string.
> - **Space Complexity:** $O(n)$, as we use a dynamic programming array of size `n`.
> - **Optimality proof:** This is the optimal solution because we only need to consider each length once, and we store the results in a dynamic programming array to avoid redundant calculations.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, string concatenation.
- Problem-solving patterns identified: using dynamic programming to store intermediate results, considering all possible ways to form a string.
- Optimization techniques learned: avoiding redundant calculations by storing intermediate results.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to initialize the dynamic programming array, not considering all possible ways to form a string.
- Edge cases to watch for: handling the case where `low` is greater than `high`, handling the case where `s1` or `s2` is empty.
- Performance pitfalls: using a brute force approach that has a high time complexity, not using dynamic programming to store intermediate results.
- Testing considerations: testing the function with different inputs, including edge cases, to ensure it works correctly.