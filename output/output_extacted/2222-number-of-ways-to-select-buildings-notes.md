## Number of Ways to Select Buildings
**Problem Link:** https://leetcode.com/problems/number-of-ways-to-select-buildings/description

**Problem Statement:**
- Input: A string `s` consisting of characters `0`, `1`, and `2`, where `0` represents an empty plot, `1` represents a building that can be selected, and `2` represents a building that cannot be selected.
- Expected Output: The number of ways to select buildings such that no two adjacent plots have selected buildings.
- Key Requirements:
  - The input string `s` is non-empty and contains only the characters `0`, `1`, and `2`.
  - The output should be an integer representing the number of valid ways to select buildings.
- Example Test Cases:
  - Input: `s = "00110"`
    - Output: `3`
    - Explanation: There are three ways to select buildings: `0`, `1`, and `2` are not adjacent, so we can select either the first, second, or third `1`.
  - Input: `s = "110"`
    - Output: `1`
    - Explanation: We can only select one of the two `1`s, as they are adjacent.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible combinations of selecting buildings and then filter out the invalid ones.
- We can use a recursive approach to generate all possible combinations.
- However, this approach is inefficient due to the large number of combinations.

```cpp
int numberOfWays(string s) {
    int n = s.size();
    int count = 0;

    // Generate all possible combinations of selecting buildings
    for (int mask = 0; mask < (1 << n); mask++) {
        bool valid = true;

        // Check if the current combination is valid
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) && s[i] == '1') {
                if (i > 0 && (mask & (1 << (i - 1))) && s[i - 1] == '1') {
                    valid = false;
                    break;
                }
                if (i < n - 1 && (mask & (1 << (i + 1))) && s[i + 1] == '1') {
                    valid = false;
                    break;
                }
            }
        }

        // If the current combination is valid, increment the count
        if (valid) {
            count++;
        }
    }

    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input string. This is because we generate all possible combinations of selecting buildings and then check each combination for validity.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count and the mask.
> - **Why these complexities occur:** The time complexity is high due to the recursive nature of generating all possible combinations, and the space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use dynamic programming to store the number of ways to select buildings up to each position.
- We can use a bottom-up approach to fill up the dynamic programming table.
- This approach is optimal because it avoids the overhead of generating all possible combinations and instead uses a systematic approach to count the number of valid ways to select buildings.

```cpp
int numberOfWays(string s) {
    int n = s.size();
    vector<int> dp(n + 1, 0);

    dp[0] = 1;

    for (int i = 1; i <= n; i++) {
        if (s[i - 1] == '0' || s[i - 1] == '2') {
            dp[i] = dp[i - 1];
        } else {
            dp[i] = dp[i - 1] + (i >= 2 ? dp[i - 2] : 1);
        }
    }

    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we fill up the dynamic programming table in a single pass.
> - **Space Complexity:** $O(n)$, as we use a dynamic programming table of size $n + 1$ to store the number of ways to select buildings up to each position.
> - **Optimality proof:** This approach is optimal because it uses a systematic approach to count the number of valid ways to select buildings, avoiding the overhead of generating all possible combinations. The dynamic programming table is filled up in a single pass, and the space complexity is linear in the size of the input string.

---

### Final Notes

**Learning Points:**
- The problem demonstrates the use of dynamic programming to solve a combinatorial problem.
- The key insight is to identify the overlapping subproblems and store the solutions to subproblems in a table to avoid redundant computation.
- The problem also highlights the importance of considering edge cases, such as the case where the input string is empty or contains only one character.

**Mistakes to Avoid:**
- One common mistake is to generate all possible combinations of selecting buildings and then filter out the invalid ones, which leads to an inefficient solution.
- Another mistake is to use a recursive approach without memoization, which can lead to redundant computation and stack overflow errors.
- It is also important to consider edge cases and handle them correctly to avoid incorrect results.